from os import path

import pandas as pd
from sklearn.metrics import median_absolute_error
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neural_network import MLPRegressor

from mAcHinE_LeArnInG.machine_learning_parent_class import *


class MLPRegressorModel(MachineLearningModel):
    data_df: pd.DataFrame  # used during data fetch
    lookup_year: datetime.date.year  # used during data fetch
    time_series_cross_validation: object  # used during model training and testing
    param_grid: {}  # used during model training and testing
    cv_results: {}  # used during model training and testing

    def fetch_data(self):
        # Sets up numpy array X and list y
        self.X, self.y, self.combined_data = super().fetch_data()

        # Creates temporary dataframe for manipulating data into place before sending to the numpy array
        self.data_df = pd.DataFrame()

        for i in range(self.data_depth, 0, -1):
            logging.debug(
                f'fetching data; for loop iteration: {self.data_depth - i}; lookup_year: {self.prediction_year - i}')
            with open(path.abspath(f"../master_{self.prediction_year - i}.csv"), 'r') as file:
                data = pd.read_csv(file)
                if i == self.data_depth:
                    self.data_df = data[['county_code', 'zasp_index']]
                else:
                    self.data_df = pd.merge(self.data_df, data[['county_code', 'zasp_index']], on='county_code')
                self.data_df = self.data_df.rename(columns={'zasp_index': f'zasp_index_{self.prediction_year - i}'})

        self.data_df = self.data_df.dropna()
        self.county_codes = self.data_df.iloc[:, 0]
        self.combined_data = self.data_df.iloc[:, 1:].to_numpy()
        logging.debug(f'combined_data: \n {self.combined_data} \n')
        self.X = self.data_df.iloc[:, 1:-1].to_numpy()
        logging.debug(f'X data: \n {self.X} \n')
        self.y = self.data_df.iloc[:, -1].tolist()
        logging.debug(f'y data: \n {self.y} \n')

        return self.X, self.y, self.combined_data,self.county_codes

    def train_and_test(self, X, y):
        self.model = super().train_and_test(X, y)

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, random_state=self.random_state)

        # if you had more than 1 year to train on, you would use this for time series cross validation
        # self.time_series_cross_validation = TimeSeriesSplit(n_splits=self.data_depth)

        self.model = MLPRegressor()

        self.param_grid = {'hidden_layer_sizes': [(110, 110, 110, 110, 110, 110, 110, 110)],
                           'shuffle': [False],
                           'max_iter': [5000],
                           'solver': ['lbfgs'],
                           'random_state': [self.random_state]}

        self.cv_results = GridSearchCV(self.model,
                                       self.param_grid,
                                       n_jobs=-1,  # uses all CPU cores available
                                       # cv=self.time_series_cross_validation,
                                       verbose=int(self.debug)
                                       ).fit(self.X_train, self.y_train)

        self.model = self.cv_results.best_estimator_
        logging.info(f' Test results: \n(R^2) {self.model.score(self.X_test, self.y_test)} (closer to 1 is better) \n(Med) {median_absolute_error(self.y_test, self.model.predict(self.X_test))} (closer to 0 is better)')
        return self.model

    def predict(self, combined_data, model):
        if np.size(self.combined_data, 1) == self.data_depth:
            self.predictions = super().predict(combined_data, model)
            self.predictions = model.predict(combined_data[:, -1].reshape(-1, 1)).reshape(-1, 1)
            self.combined_data = np.append(combined_data, self.predictions.reshape(-1, 1), axis=1)
        else:
            self.predictions = np.append(self.predictions,
                                         model.predict(self.combined_data[:, -1].reshape(-1, 1)).reshape(-1, 1), axis=1)
            self.combined_data = np.append(self.combined_data, self.predictions[:, -1].reshape(-1, 1), axis=1)
        logging.debug(f'\n\n Predictions: \n {self.predictions} \nCombined Data: \n {self.combined_data} \n')

        if self.prediction_depth != 0:
            self.prediction_depth -= 1
            logging.debug(f'creating predictions; iteration: {self.prediction_depth}')
            self.predict(self.combined_data, model)

        return self.predictions

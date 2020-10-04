"""
* A parent class with built in methods useful when working with a model *
"""
import datetime
import logging
from sys import stderr

import numpy as np
import pandas as pd


class MachineLearningModel:
    X: np.array  # returned by data fetch, used during training
    y: []  # returned by data fetch, used during training
    X_train: np.array  # used during training
    y_train: []  # used during training
    X_test: np.array  # used during testing
    y_test: []  # used during testing
    display_df: pd.DataFrame  # used for displaying results
    predictions: []  # used for storing predictions

    def __init__(self, data_depth=14, prediction_year=datetime.date.today().year, prediction_depth=7, random_state=1, debug=False):
        """
        Initializes attributes relevant to all models.
        :param data_depth: How many years 'back' should data be looked up for (not including prediction year)
        :param prediction_year: What year should the prediction be created for
        :param prediction_depth: How many years into the future should predictions be created for
        :param random_state: What random state should be used whenever one is employed
        :param debug: If set to true, enables debug logging
        """
        self.data_depth = data_depth
        self.prediction_year = prediction_year
        self.random_state = random_state
        self.debug = debug
        self.model = None  # will be the trained model that is returned by the train_and_test method

        # Set up logging:
        logging.basicConfig(stream=stderr, level=logging.DEBUG if debug else logging.INFO)
        logging.info(f' --------------- RUNNING {self.__module__.split(".")[-1]} MODEL --------------- ')

    def fetch_data(self):
        """
        Fetches and prepares data for the training and testing phase.
        :return: returns numpy array X and list y to be used during machine learning
        Each different model subclass overrides this method in order to get it's relevant data.
            Note: The extended method should make use of prediction_year and data_depth.
        After data is fetched it is split into X, y; and if necessary the data is normalized.
        """
        logging.info(f' Fetching data for a {self.prediction_year} prediction year using a data depth of {self.data_depth} years...')
        self.X = np.array  # the input data that will be fed to the machine learning model
        self.y = []  # the output data that the machine learning model produces
        return self.X, self.y

    def train_and_test(self, X, y):
        """
        Conducts training and testing on data to prepare model for the prediction phase.
        :param X: the input data that will be fed to the machine learning model
        :param y: the output data that the machine learning model produces
        :return model: returns a trained and tested machine learning model
        TODO: Improve explanation (below) of what this method does
        Trains the model, performing time series splits as necessary
        Tests the model
        """
        logging.info(f' Training and testing {self.__module__.split(".")[-1]} model...')

        return self.model

    def predict(self, model, X, y, prediction_depth):
        """
        Creates predictions based on the best available trained model created in the train_and_test method.
        :param model: a trained model to use when creating predictions
        :param X: Data leading up to the year before the prediction year
        :param y: Data for the year before the prediction year
        :param prediction_depth: How many years into the future should predictions be created for
        :return: Predictions for the prediction year(s)
        """
        logging.info(f' Creating predictions for {self.prediction_year}...')
        self.predictions = np.array([])
        return self.predictions

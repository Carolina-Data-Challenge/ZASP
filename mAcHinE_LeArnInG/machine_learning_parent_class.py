"""
* A parent class with built in methods useful when working with a ML model *
"""
import datetime
import logging
from sys import stderr

import numpy as np


class MachineLearningModel:
    X: np.array  # returned by data fetch, used during training/testing
    y: []  # returned by data fetch, used during training/testing
    combined_data: np.array  # combined X and y data returned by data fetch, used during training/testing
    X_train: np.array  # used during training
    y_train: []  # used during training
    X_test: np.array  # used during testing
    y_test: []  # used during testing
    predictions: np.array  # used for storing predictions

    def __init__(self, data_depth=14, prediction_year=datetime.date.today().year, prediction_depth=7, random_state=1, debug=False):
        """
        Initializes attributes relevant to all models.
        :param data_depth: How many years 'back' should data be looked up for (not including prediction year)
        :param prediction_year: What year should the prediction be created for
        :param prediction_depth: How many years into the future should predictions be created for
        :param random_state: What random state should be used whenever one is employed
        :param debug: If set to true, enables debug logging
        """
        self.data_depth = data_depth  # TODO implement "-1" to use all available data
        self.prediction_year = prediction_year
        self.prediction_depth = prediction_depth - 1  # since prediction_year predictions are always returned
        self.random_state = random_state
        self.debug = debug
        self.model = None  # will be the trained model that is returned by the train_and_test method

        # Set up logging:
        logging.basicConfig(stream=stderr, level=logging.DEBUG if debug else logging.INFO)
        logging.info(f' --------------- RUNNING {self.__module__.split(".")[-1]} MODEL --------------- ')

    def fetch_data(self):
        """
        Fetches and prepares data for the training/testing phase and the predictions phase.
        :return: returns np array X, list y, and np array combined_data to be used during machine learning
        The model subclass overrides this method in order to get it's relevant data.
            Note: The extended method should make use of prediction_year and data_depth.
        After data is fetched it is split into X, y; and if necessary the data is normalized.
        """
        logging.info(f' Fetching data for a {self.prediction_year} prediction year using a data depth of {self.data_depth} years...')
        self.X = np.array  # the 'input' data that will be fed to the machine learning model uses training/testing
        self.y = []  # the 'output' data that the machine learning model uses during training/testing
        self.combined_data = np.array  # combined X and y data, used when model creates predictions
        return self.X, self.y, self.combined_data

    def train_and_test(self, X, y):
        """
        Conducts training and testing on data to prepare model for the prediction phase.
        :param X: the input data that will be fed to the machine learning model
        :param y: the output data that the machine learning model produces
        :return model: returns a trained and tested machine learning model
        Trains the model, performing time series splits as necessary
        Tests the model against most recent known year's data
        """
        logging.info(f' Training and testing {self.__module__.split(".")[-1]} model...')
        return self.model

    def predict(self, combined_data, model):
        """
        Creates predictions based on the best available trained model created in the train_and_test method.
        :param combined_data: all available data, and will be used if recursively creating multi year predictions
        :param model: a trained model to use when creating predictions
        :return: Predictions for the prediction year(s)
        """
        logging.info(f' Creating predictions...')
        self.predictions = np.array([])
        return self.predictions

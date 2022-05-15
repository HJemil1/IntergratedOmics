from sklearn.model_selection import train_test_split, cross_val_score, RepeatedKFold
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.linear_model import ElasticNet
import numpy as np
import logging
import sys
import os
import Logging

__author__ = "Rik van de Pol"
__license__ = "MIT"
__email__ = "rikvdpol93@gmail.com"
__status__ = "Version 1.0"

class Elasticnet:
    def __init__(self, file, labelname):
        self.file = file
        self.labelname = labelname
        self.labels = None

    def extract_labels(self):
        sep = os.path.sep
        self.file = self.file.dropna(axis=0)
        logs = Logging.Logging()
        try:
            self.labels = self.file[self.labelname]
            msg = (f"Columnname {self.labelname} used as predictor label")
            logs.create_logs(self.__class__.__name__, msg)

        except KeyError as e:
            msg = f"{e}: Labelname {self.labelname} not present in data"
            logs.create_logs(self.__class__.__name__, msg)
            sys.exit(0)

        self.file = self.file.drop([self.labelname, "Pseudo", "Antibody_batch"], axis=1)

    def split_data(self, test_size=0.3, random_state=None):
        #splits the model. test.size determines the proportion of data
        #to be used as test data, the remaining us used for training. Random state is automatically set to None
        #The user can provide any integer to this, which ensures the same distribution of training and test data as long 
        #as the number remains the same.
        X_train, X_test, y_train, y_test = train_test_split(self.file,
                                                            self.labels,
                                                            test_size=test_size,
                                                            random_state=random_state)

        return X_train, X_test, y_train, y_test

    def define_model(self, alpha=1.0, l1_ratio=0.5, n_splits=10, n_repeats=3, random_state=None):
        model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio)
        cv = RepeatedKFold(n_splits=n_splits, n_repeats=n_repeats, random_state=random_state)
        return model, cv

    def train_model(self, X_train, y_train):
        elastic_model = ElasticNet().fit(X_train, y_train)
        return elastic_model

    def predict(self, elastic_model, X_test):
        predictions = elastic_model.predict(X_test)
        return predictions

    def evaluate_model(self, model, cv):
        scores = cross_val_score(model, self.file, self.labels, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
        scores = np.absolute(scores)
        return scores
        # print('Mean MAE: %.3f (%.3f)' % (np.mean(scores), np.std(scores)))
        # print("All scores:", scores)

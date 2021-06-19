
import pandas as pd
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

import pickle

target_feature = ['result']
categorical_predictors = ['c1', 'c2', 'c3', 'c4',  # unused
                          'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'gamemode']
numerical_predictors = ['s6ts', 's7r', 's5ts', 's4ts', 's3ts', 's2ts', 's5r', 's8ts',
                        's3r', 's4r', 's1r', 's2r', 's1ts', 's10r', 's8r', 's6r', 's7ts', 's10ts', 's9r', 's9ts']

gamemode_label_map = {"gamemode": {"ARAM": 1, "ranked": 0}}


class NN():

    def __init__(self, filename: str):
        self.df = pd.read_csv(filename)

    # train model on data within filename
    def train_model(self):
        X_train, X_test, y_train, y_test = self._preprocess_data()

        mlp = MLPClassifier(hidden_layer_sizes=(8, 8, 8),
                            activation='relu', solver='adam', max_iter=500)

        mlp.fit(X_train, y_train)

        predict_train = mlp.predict(X_train)
        predict_test = mlp.predict(X_test)

        print(confusion_matrix(y_train, predict_train))
        print(classification_report(y_train, predict_train))

        print(confusion_matrix(y_test, predict_test))
        print(classification_report(y_test, predict_test))

        # save model into file
        with open('ml/models/NN.model', 'wb') as model_file:
            pickle.dump(mlp, model_file)

    # preprocesses the data
    # 1. normalize numerical predictors
    # 2. encode numerical categorical predictors (champion id) to categorical type
    # 3. split data to test and training sets
    # the split data sets are returned
    def _preprocess_data(self):

        # normalize
        self.df[numerical_predictors] /= self.df[numerical_predictors].max()

        # encode our numerical champion data to be categorical
        self.df = self.df.replace(gamemode_label_map)
        for pred in categorical_predictors:
            self.df[pred] = self.df[pred].astype('category')

        # split data
        # just using the numerical predictors
        X = self.df[numerical_predictors].values
        y = self.df[target_feature].values
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.30, random_state=40)
        # print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

        return (X_train, X_test, y_train, y_test)


class Predictor():
    def __init__(self, model):
        self.model = model

    def predict(self, entry):
        df = pd.DataFrame.from_dict(entry, orient='index').T

        X = df[numerical_predictors].values
        return self.model.predict(X)[0]


# n = NN('ml/datasets/lol_data_850.csv')
# n.train_model()

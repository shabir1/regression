# Linear Regression
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets

class MultipleRegression(object):
    def __init__(self):
        self.regr = LinearRegression()

    def train(self, X_train, Y_train):
        self.regr.fit(X_train, Y_train)
        model = {}
        model['coef'] = self.regr.coef_
        model['intercept'] = self.regr.intercept_
        print(model)
        return model

    def evaluate(self, X_train, Y_train, X_test, Y_test):
        self.train(X_train, Y_train)

        print("actual  :  predict")
        c = self.regr.predict(X_test)
        for i in range(0, Y_test.__len__()):
            print(i, " : ", Y_test[i], "  :  ", c[i])

        print("predict mean")
        p = np.mean((self.regr.predict(X_test) - Y_test) ** 2)
        print(p)



    def predict(self, X_test):
        return self.regr.predict(X_test)


def main():
    diabetes = datasets.load_diabetes()
    diabetes_X_train = diabetes.data[:-20]
    diabetes_X_test = diabetes.data[-20:]
    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test = diabetes.target[-20:]

    reg = MultipleRegression()
    reg.evaluate(diabetes_X_train, diabetes_y_train, diabetes_X_test, diabetes_y_test)

if __name__ == '__main__':
    main()

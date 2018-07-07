# Linear Regression
import numpy as np
from sklearn.linear_model import LinearRegression

class Regression(object):
    def __init__(self):
        self.regr = LinearRegression()

    def train(self, X_train, Y_train):
        self.regr.fit(X_train, Y_train)

    def evaluate(self, X_train, Y_train, X_test, Y_test):
        self.train(X_train, Y_train)

        print("Coef")
        print(self.regr.coef_)

        print("actual  :  predict")
        c = self.regr.predict(X_test)
        for i in range(0, Y_test.__len__()):
            print(Y_test[i], "  :  ", c[i])

        print("predict mean")
        p = np.mean((self.regr.predict(X_test) - Y_test) ** 2)
        print(p)

    def predict(self, X_test):
        return self.regr.predict(X_test)


def main():
    reg = Regression()


if __name__ == '__main__':
    main()

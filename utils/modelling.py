from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import pandas as pd



def splitting(data):
    test_size = 0.2
    x=data.iloc[:,:-1]
    y=data.iloc[:,-1]

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=test_size)
    return X_train, X_test, Y_train, Y_test

def model_RF(X_train, X_test, Y_train, Y_test):
    Rf = RandomForestRegressor()
    model = Rf.fit(X_train, Y_train)
    pred = model.predict(X_test)

    mse = mean_squared_error(Y_test, pred)
    mae = mean_absolute_error(Y_test, pred)

    data_uji = X_test
    print(f"Hasil MSE = {mse}, Hasil MAE = {mae}")

    return model, data_uji, mae, mse


def model_RF_HP(X_train, X_test, Y_train, Y_test):
    params = {
        "n_estimators": [50,100,200],
        "max_depth":[3,5,10]
    }
    Rf = RandomForestRegressor()
    grid = GridSearchCV(Rf, params)
    grid.fit(X_train, Y_train)
    model = grid.best_estimator_
    pred = model.predict(X_test)

    mse = mean_squared_error(Y_test, pred)
    mae = mean_absolute_error(Y_test, pred)

    data_uji = X_test
    print(f"Hasil MSE = {mse}, Hasil MAE = {mae}")

    return model, data_uji, mae, mse, params



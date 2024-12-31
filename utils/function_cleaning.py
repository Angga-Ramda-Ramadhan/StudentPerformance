import seaborn as sns
import pandas as pd


def check_dp(data):
    dp = data.duplicated().sum()
    return print("Jumlah Duplikat Data: ", dp)

def check_mv(data):
    mv = data.isnull().sum()
    return print("Jumlah Missing Value: ", mv)

def checkoutlier(data, kolom):
    Q1 = data[kolom].quantile(0.25)
    Q3 = data[kolom].quantile(0.75)
    IQR = Q3 - Q1

    lower_bond = Q1 - 1 * IQR
    upper_bond = Q3 + 1 * IQR

    outlier = data[(data[kolom]<lower_bond) | (data[kolom]>upper_bond)]
    print("Jumlah Outlier dalam kolom {kolom}= ", outlier)
    data_clean = data[(data[kolom]>lower_bond)&(data[kolom]<upper_bond)]

    return data_clean

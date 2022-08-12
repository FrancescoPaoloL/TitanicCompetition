import pandas as pd

def showPercentageNan(colName, dtFrame):
    perc = (dtFrame[colName].isnull().sum() / dtFrame.shape[0])
    print(f"Percent of missing '{colName}' records is {round(perc * 100,3)} %")
    return

def makeDummies(df, colummnName):
    dummy = pd.get_dummies(df[colummnName], prefix=f"{colummnName}_")
    return pd.concat([df, dummy], axis=1).drop(colummnName, axis=1)

def delColumn(df, name):
    if name in df.columns:
        df.drop(name, axis=1, inplace=True)
    return
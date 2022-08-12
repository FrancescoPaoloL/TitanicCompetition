from IPython.display import display, Markdown
from utils import *

def basicEDA(df, title):
    display(Markdown("**Just first five rows**"))
    display(df.head())
    display(f"The {title} data set consists of {df.shape[1]} different features which for {df.shape[0]} samples.")
    display(Markdown("**Info about the index dtype and columns, non-null values and memory usage.**"))
    display(df.info())
    display(Markdown("**Check all of the values in the data frame which holds my data.**"))
    display(df.applymap(type))

    # isnull() is just an alias of the isna() method as shown in pandas source code.
    nrNa = df.isna().sum()
    display(Markdown("**Count na values**"))
    display(nrNa)

    if nrNa.any() > 0:
        colNan = list(df[df.columns[df.isna().any()]].columns)
        display(f"The columns with missing data are: {colNan}")

        for col in colNan:
            showPercentageNan(col, df)

    display(Markdown("**Show the statistic report of the numeric features of the dataset**"))
    display(df.describe().transpose())

    display(Markdown("**Show the statistic report of the categorical features of the dataset**"))
    display(df.describe(include=['O']).transpose())
    return
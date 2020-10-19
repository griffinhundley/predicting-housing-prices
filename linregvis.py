from statsmodels.formula.api import ols
import pandas as pd
def run_lr(variables, X, y):
    formula = variables
    data_ols = pd.concat([X, y], axis = 1)
    model = ols(formula= formula, data= data_ols).fit()
    return model
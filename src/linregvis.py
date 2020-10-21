# Takes the statsmodels formula, X data, and y data and does an OLS fit
from statsmodels.formula.api import ols
import pandas as pd
def run_lr(variables, X, y):
    formula = variables # This should be in the statsmodels format 'y~x1+x2+...'
    data_ols = pd.concat([X, y], axis = 1) # The X and y data are joined 
    model = ols(formula= formula, data= data_ols).fit() # Fitted sm least squares regression
    print(model.summary())
    return model

# Takes an ax and adds dollar formatting to the ticks
import matplotlib.ticker as mtick
def dollar_ticks(ax):
    fmt = '${x:,.0f}'
    tick = mtick.StrMethodFormatter(fmt)
    ax.yaxis.set_major_formatter(tick) 
    ax.tick_params(labelsize='large')
# import required libraries
import pandas as pd # pandas library for data manipulation and analysis
import numpy as np  # numpy library for scientific computing 
from scipy.optimize import minimize # minimize function from scipy that minimizes a given function
import cvxopt as opt # convex optimization library, used to solve quadratic programming problems
from cvxopt import blas, solvers # blas and solvers module from cvxopt
solvers.options['show_progress'] = False # setting option for solver to not show progress

# create a DataFrame to store returns of 3 stocks
returns = pd.DataFrame({'stock1': [0.05, 0.06, 0.04], 'stock2': [0.07, 0.09, 0.11], 'stock3': [0.06, 0.05, 0.04]})

print(f"Stock data:\n \n{returns}")
# calculate the covariance matrix of the returns
cov_matrix = returns.cov()
returns = np.matrix(returns)
# define an objective function that calculates the portfolio risk given weights
def objective(weights):
    global returns
    weights = np.matrix(weights) # convert weights into numpy matrix
    port_returns = np.sum(returns.mean() * weights.T) # calculate expected portfolio returns
    port_SD = np.sqrt(np.dot(weights, np.dot(cov_matrix, weights.T))) # calculate portfolio standard deviation
    return port_SD / port_returns # return the Sharpe ratio

# define a constraint function that ensures sum of weights equals to 1 - this represents budget constraint
def constraint(weights):
    return np.sum(weights) - 1

# set initial weights as equal allocation of 3 stocks 
init_weights = np.ones((len(returns))) / len(returns)

# optimize the objective function with SLSQP method and equality type constraints using minimize function
opt_results = minimize(objective, init_weights, method='SLSQP', constraints={'type': 'eq', 'fun': constraint})

# print the optimized weights that minimizes the objective function 
print(f"\nThe optimal weights to diversify and minimize the risk on this portfolio are:\n\n{opt_results['x']}")

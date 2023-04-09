### Portfolio Optimization using Quadratic Programming

This code demonstrates how to use quadratic programming to optimize a portfolio of stocks based on the Sharpe ratio. The following libraries are used in this code:

* `pandas` for data manipulation and analysis
* `numpy` for scientific computing 
* `scipy.optimize.minimize` function from scipy that minimizes a given function
* `cvxopt` for convex optimization, used to solve quadratic programming problems

The code starts by creating a `DataFrame` to store returns of 3 different stocks. Then it calculates the covariance matrix of the returns.

It then defines an objective function that calculates the portfolio risk given weights. The `objective` function takes in a set of weights for the three stocks and returns the inverse of the Sharpe ratio (because we are using the minimize function).

Next, a constraint function is defined to ensure that the sum of weights adds up to 1, which represents the budget constraint.

The initial weights are set to be an equal allocation of the 3 stocks, and the `minimize` function is used to optimize the objective function with SLSQP method and equality type constraints. 

Finally, the optimized weights that minimize the objective function are printed to the console.

This code can be modified to suit specific requirements and input data. Please if you notice any inconsistencies or potential code optimizations feel free to reach out. I'm always open to learn.

# Custom-Function-Regressor
------------------------------

Custom Function Regressor using Stochastic Gradient in pure Python.

Usage:
-------
At the time of writing,you have to hard code your function.You also have to type the partial derivatives of the function with respect to all parameters.

Parameters are represented as w matrix where:

a=w[0],
b=w[1],
c=w[2],
d=w[3],
e=w[4],
.
.
.
etc.


You also have to give the no. of parameters in the coeff variable.

The function has to written to the pred variable.

dw matrix is the weight update matrix for each w index.


Terms introduced in version 1.9:
---------------------------------

<h3>Lookup Multiplier:</h3>
It is the step size at which the direction of the slope of the cost function wil be checked.This can be used when the algorithm is stuck inside a local minima.It will help the curve fitter algo to "see the bigger picture" such that even though it may be stuck in the local minima but it will be able to see the slope which is far from its current location and then decide where it wants to go.For normal behaviour, you can set this value to 1. 

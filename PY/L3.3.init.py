"""object oriented programming"""

# Example: Evaluate a Regression Model
# A model predicts numerical values, such as the price of a house or the tomorrow’s temperature. We want to build a Python class to compare the predicted values with the observed values.
# The `RegressionResults` class:
## accepts lists of observed and predicted values;
## verifies that the lists are of equal length, are not empty, and contain only finite numbers;
## stores the data in two attributes;
## provides the following methods:
### mae(): mean absolute error;
### mse(): mean squared error;
### rmse(): root mean square error;
### mean_error(): mean signed error, calculated as predicted − observed.
### If the mean signed error is positive, the model tends to overestimate; if it is negative, it tends to underestimate.


import math

class RegressionResults:
    def __init__(self, actual=[], predicted=[]):
        if len(actual) != len(predicted):
            raise ValueError(
                "Actual and predicted values must be the same number."
            )

        if len(actual) == 0:
            raise ValueError("The value lists cannot be empty.")

        # complete the checks

        # the object stores copies of the input lists
        self.actual = list(actual)
        self.predicted = list(predicted)

    def _errors(self):
        """Returns errors: expected values - observed value."""


    def mae(self):
        """Mean Absolute Error."""
 

    def mse(self):
        """Mean Squared Error."""


    def rmse(self):
        """Root Mean Squared Error."""


    def mean_error(self):
        """Mean signed error: positive means overestimation; negative means underestimation."""


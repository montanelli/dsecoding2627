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

        for value in actual + predicted:
            valid_number = (
                isinstance(value, (int, float))
                and math.isfinite(value)
            )

            if not valid_number:
                raise ValueError(
                    "All the values must be finite numbers."
                )

        # the object stores copies of the input lists
        self.actual = list(actual)
        self.predicted = list(predicted)

    def _errors(self):
        """Returns errors: expected values - observed value."""
        return [
            predicted - actual
            for actual, predicted in zip(self.actual, self.predicted)
        ]

    def mae(self):
        """Mean Absolute Error."""
        errors = self._errors()
        return sum(abs(error) for error in errors) / len(errors)

    def mse(self):
        """Mean Squared Error."""
        errors = self._errors()
        return sum(error ** 2 for error in errors) / len(errors)

    def rmse(self):
        """Root Mean Squared Error."""
        return math.sqrt(self.mse())

    def mean_error(self):
        """Mean signed error: positive means overestimation; negative means underestimation."""
        errors = self._errors()
        return sum(errors) / len(errors)


# main
observed = [3, -0.5, 2, 7]
predicted = [2.5, 0, 2, 8]

results = RegressionResults(observed, predicted)

print("MAE:", round(results.mae(), 2))
print("MSE:", round(results.mse(), 3))
print("RMSE:", round(results.rmse(), 3))
print("Mean signed error:", round(results.mean_error(), 2))

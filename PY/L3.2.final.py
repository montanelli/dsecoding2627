"""object oriented programming"""

# Example: evaluate the quality of a binary classifier
# A classification model assigns a label to each element: 1 indicates the positive class and 0 indicates the negative class.
# We want to create a Python class that compares the actual labels with the labels predicted by the model and calculates some evaluation metrics.

# The `ClassificationResults` class must:
## accept two lists in its constructor: actual labels and predicted labels;
## verify that the lists are of equal length, are not empty, and contain only 0s and 1s;
## store the two lists as attributes;
## provide the following methods:
### confusion_matrix(), which returns the counts of true positives, false positives, true negatives, and false negatives;


### accuracy(), which calculates the proportion of correct predictions;
### precision(), which calculates the proportion of correct positive predictions;
### recall(), which calculates the proportion of positive items detected;
### f1_score(), which calculates the harmonic mean of precision and recall.
### return 0.0 for precision, recall, or F1 when the corresponding denominator is zero.


class ClassificationResults:
    VALID_LABELS = (0, 1)

    def __init__(self, actual=[], predicted=[]):
        ## verify that the lists are of equal length, are not empty;
        if len(actual) != len(predicted) or len(actual) == 0:
            raise ValueError("Two non-empty lists of same size are required.")

        # lists must contain only 0s and 1s
        for label in actual + predicted:
            if label not in self.VALID_LABELS:
                raise ValueError("Only 0 and 1 are valid labels.")

        self.actual = actual
        self.predicted = predicted

    # internal method
    def _counts(self):
        # computes the confusion matrix elements
        tp = 0
        tn = 0
        fp = 0
        fn = 0

        for a, p in zip(self.actual, self.predicted):
            if a == 1 and p == 1:
                tp += 1
            elif a == 1 and p == 0:
                fn += 1
            elif a == 0 and p == 0:
                tn += 1
            else:
                fp += 1

        return tp, tn, fp, fn

    def confusion_matrix(self):
        # Returns the values of the confusion matrix
        tp, tn, fp, fn = self._counts()

        return {"TP": tp, "TN": tn, "FP": fp, "FN": fn}

    def accuracy(self):
        """Returns the ratio of correct labels."""
        tp, tn, fp, fn = self._counts()
        return (tp + tn) / len(self.actual)

    def precision(self):
        """Returns the number of tp on the overall number of predicted labels."""
        tp, tn, fp, fn = self._counts()
        denominator = tp + fp

        if denominator == 0:
            return 0.0

        return tp / denominator

    def recall(self):
        """Returns the number of tp on the overall number of expected labels."""
        tp, tn, fp, fn = self._counts()
        denominator = tp + fn

        if denominator == 0:
            return 0.0

        return tp / denominator

    def f1_score(self):
        """Returns the armonic mean of precision and recall."""
        precision = self.precision()
        recall = self.recall()

        if precision + recall == 0:
            return 0.0

        return 2 * precision * recall / (precision + recall)

# main

actual = [1, 0, 0, 1, 1, 0]
predicted = [1, 0, 1, 0, 1, 0]

cr1 = ClassificationResults(actual, predicted)
cm = cr1.confusion_matrix()
for i in cm:
    print(i + ": " + str(cm[i]))

print("Accuracy:", round(cr1.accuracy(), 2))
print("Precision:", round(cr1.precision(), 2))
print("Recall:", round(cr1.recall(), 2))
print("F1-score:", round(cr1.f1_score(), 2))
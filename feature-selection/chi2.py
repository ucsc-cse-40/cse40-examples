#!/usr/bin/env python3

import pandas
import sklearn.feature_selection

DATA = {
    'Seen Slug': [
        True, True, True, True, False, False, False, False,
    ],
    'Has Rained': [
        True, True, False, True, False, False, False, False,
    ],
    'Before Noon': [
        True, False, True, True, False, False, True, False,
    ],
    'Had Coffee this Morning': [
        True, False, True, False, True, False, False, True,
    ],
}

FEATURE_COLUMNS = ['Has Rained', 'Before Noon', 'Had Coffee this Morning']
LABEL_COLUMN = 'Seen Slug'

def main():
    frame = pandas.DataFrame(DATA)
    print(frame)

    features = frame[FEATURE_COLUMNS]
    labels = frame[LABEL_COLUMN]

    # Compute the chi-squared values.
    chi2_scores, p_values = sklearn.feature_selection.chi2(features, labels)

    # Compute Pearson's R (aka Pearson correlation coefficient).
    pearson_scores = sklearn.feature_selection.r_regression(features, labels)

    for i in range(len(FEATURE_COLUMNS)):
        print("Column: '%s', chi2 Score: %f, p-value: %f, Pearson Correlation: %f" % (
            FEATURE_COLUMNS[i], chi2_scores[i], p_values[i], pearson_scores[i]))

if (__name__ == '__main__'):
    main()

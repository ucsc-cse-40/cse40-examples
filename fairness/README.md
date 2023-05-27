# Fairness

An example that looks into bias, fairness, and what we can do to make machine learning models that are more ethical.

## Data

The source data for this example is the [UCI Adult/Census dataset](https://archive.ics.uci.edu/ml/datasets/Adult).
This is one of the most widely used and explored datasets in the fairness community.

For narrative purposes, a single column (`zipcode`) has been added to the dataset.
To maintain realism, all the other quirks of the dataset have been kept and the `zipcode` column has been added before the label column.
The `uci-census/add-zip.py` script handles adding the `zipcode` column (but this repository will already have data that is the output of that script).

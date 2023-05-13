#!/usr/bin/env python3

import numpy
import pandas

BIN_EDGESS = [numpy.NINF, 30, 60, numpy.PINF]
BIN_LABELS = ['small', 'medium', 'large']

frame = pandas.DataFrame([
    ['male',   82, 'graduate'],
    ['female', 54, 'postgraduate'],
    ['female', 42, 'highschool'],
    ['female', 28, 'highschool']
])
frame.columns = ['gender', 'weight', 'degree']

# Binning with a vanilla Python list.

data = list(frame['weight'])
bins = ['small' if (value < 30) else ('medium' if (value < 60) else 'large') for value in data]

print("Python List with comprehension:")
print(bins)
print()

# Dinning with Pandas (pandas.cut()).

bins = pandas.cut(frame['weight'], bins = BIN_EDGESS, labels = BIN_LABELS)

print("Pandas DataFrame with pandas.cut():")
print(bins)
print()

# Binning with Numpy (numpy.digitize()).

data = frame['weight'].to_numpy()
bins = numpy.digitize(data, bins = BIN_EDGESS, right = True)

print("numpy.ndarray with numpy.digitize():")
print(bins)

# Map indexes to label names.
print("Map the indexes from numpy.digitize() to labels.")
print([BIN_LABELS[index - 1] for index in bins])

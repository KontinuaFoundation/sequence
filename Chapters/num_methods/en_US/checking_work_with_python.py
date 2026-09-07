"""
Numerical Methods of Describing Data
"Checking Your Work with Python" 

Verifies the ten quiz-score example: mean, sample variance, and sample
standard deviation, using the built-in statistics module.
"""
import statistics

scores = [8, 9, 0, 10, 10, 8, 7, 9, 10, 5]

print("mean:    ", statistics.mean(scores))
print("variance:", statistics.variance(scores))   # divides by n - 1
print("stdev:   ", statistics.stdev(scores))       # divides by n - 1

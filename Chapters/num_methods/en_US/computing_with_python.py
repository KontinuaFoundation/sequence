"""
Numerical Methods of Describing Data
"Computing with Python" 
Computes mean, median, variance, standard deviation, and quartiles for
the car dealership data set used throughout the chapter.
"""
import statistics

sales = [14, 9, 23, 7, 11, 23, 17, 11, 3, 24, 21, 2, 20, 20]

print("mean:    ", statistics.mean(sales))
print("median:  ", statistics.median(sales))
print("variance:", round(statistics.variance(sales), 2))
print("stdev:   ", round(statistics.stdev(sales), 2))

q1, q2, q3 = statistics.quantiles(sales, n=4)
print("Q1, Q2, Q3:", q1, q2, q3)

import numpy as np
import scipy as sp

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def complex_add(a, b):
    return np.add(a, b)

def complex_subtract(a, b):
    return np.subtract(a, b)

def complex_multiply(a, b):
    return np.multiply(a, b)

def complex_divide(a, b):
    return np.divide(a, b)

def logarithm(a, base):
    return np.log(a) / np.log(base)

def mean(data):
    return np.mean(data)

def median(data):
    return np.median(data)

def standard_deviation(data):
    return np.std(data)

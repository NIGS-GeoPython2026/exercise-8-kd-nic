"""Functions used in Exercise 8 of Geol 197 GDAM"""

# Import any modules needed in your functions here
import math


# Define your new functions below
def mean(x):
    return sum(x) / len(x)


def stddev(x):
    #These define the N and mean to be used
    n = len(x)
    ave = mean(x)
    #This makes the squared differences a list, so each item can be used by the function
    squared_diff = [(i - ave) ** 2 for i in x]
    
    return math.sqrt(1/n * sum(squared_diff))

def sem(x):
    return stddev(x) / math.sqrt(len(x))


def gaussian(gauss_mean, gauss_stddev, gauss_x):
    #This calls on the predetermined variables gauss_mean and gauss_stddev, while gauss_x is a list whose individual contents must be called upon
    return [(1/(gauss_stddev * math.sqrt(2*math.pi))) * math.e ** (-1*(((n - gauss_mean)**2) / ((2*gauss_stddev) **2))) for n in gauss_x]


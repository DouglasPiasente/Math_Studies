from math import exp

p = 1000 #principal starting amount
r = .05 #interest rate by year
t = 3 # time, number of years
n = 12 # compound every month in a year, 365 if I want to compound by day


# simple compound interest in python
a = p * (1 + (r/n))**(n * t)

# continuous interest (python uses Euler as exponent)
e = p * exp(r*t)

print(a, e)

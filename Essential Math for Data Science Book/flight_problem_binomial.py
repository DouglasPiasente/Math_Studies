""" 
You have 137 passengers booked on a flight from Las Vegas to Dallas. 
However, it is Las Vegas on a Sunday morning and you estimate each passenger is 40% likely to not show up.

You are trying to figure out how many seats to overbook so the plane does not fly empty.

How likely is it at least 50 passengers will not show up?
"""

# The binomial distribution is used here because it models the number of successes 
# in a fixed number of independent Bernoulli trials (events with only two possible outcomes).

from scipy.stats import binom 

n = 137 # otal number of passengers (137 in this case).
p = .40 # probability that a passenger will not show up (40% or 0.40).


# This line initializes a variable p_50_or_more_noshows to 0.0. 
# This variable will be used to accumulate the probability that 50 or more passengers will not show up.
p_50_or_more_noshows = 0.0


# This is a for loop that iterates over values of x from 50 to 137 (inclusive). 
# For each value of x, it calculates the probability mass function (pmf) for the binomial distribution with parameters n and p. 
# The pmf gives the probability of getting exactly x successes. 
# The calculated probability is then added to the variable p_50_or_more_noshows.
for x in range(50,138):
    p_50_or_more_noshows += binom.pmf(x, n, p)

print(p_50_or_more_noshows) # 0.822095588147425

""" 
In summary, the code is using the binomial distribution to model the probability of at least 50 passengers not showing up on a flight, 
given the total number of passengers (137) and the probability of an individual passenger not showing up (40%).
"""
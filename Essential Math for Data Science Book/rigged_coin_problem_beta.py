""" 
You flipped a coin 19 times and got heads 15 times and tails 4 times.

Do you think this coin has any good probability of being fair? Why or why not?
"""

from scipy.stats import beta

heads = 8
tails = 2

# This line calculates the probability that the underlying probability of getting heads is less than or equal to 0.5. 
# It uses the cumulative distribution function (cdf) of the beta distribution. 
# The formula 1.0 - beta.cdf(0.5, heads, tails) calculates the probability that the coin is biased towards heads.
p = 1.0 - beta.cdf(.5, heads, tails)

print(p) # 0.98046875

""" 
In summary, the code is using the beta distribution to assess the probability that a coin is biased towards heads 
based on the observed number of heads (8) and tails (2) in 19 coin flips. 
The high probability (0.98046875) suggests that, given the observed data, 
there is strong evidence that the coin is biased towards showing heads.

A higher value of p suggests stronger evidence that the coin is biased towards heads.
"""
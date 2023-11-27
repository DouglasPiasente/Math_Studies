""" 
Let´s consider a sample of 50 golden retrievers, we got their weight and we are trying to find the probability
of having a golden retriever in between 62 and 66 pounds
"""

from scipy.stats import norm # that´s because we are cnsidering them to have a normal distribution

mean = 64.43
std_dev = 2.99

# here we calculate the probability of them up to 66 pounds and subtracting the probability up to 62, to get the value in between
x = norm.cdf(66, mean, std_dev) - norm.cdf(62, mean, std_dev) 
#0.4920450147062894 this is the probability of the dogs are between 62 and 66


# to look up the probability and then returning the x-value in scipy we use the norm.ppf() function
# for example, I want to find the weight that 95% of golden retriever fall under, then we use the inverse CDF

y = norm.ppf(.95, loc=64.43, scale=2.99) 
# 69.3481123445849 this is the weight that wil comprehend 95% of the dogs

print(x, y)
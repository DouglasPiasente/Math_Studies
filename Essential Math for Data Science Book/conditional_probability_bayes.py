""" 
Conditional Probability and Bayes’ Theorem
A probability topic that easily confuses people is the concept of conditional probability, 
which is the probability of an event A occurring given event B has occurred. It is typically expressed as P(A GIVEN B) or P(A|B).

Let’s say a study makes a claim that 85% of cancer patients drank coffee. How do you react to this claim? 
Does this alarm you and make you want to abandon your favorite morning drink? 
Let’s first define this as a conditional probability P(Coffee given Cancer) or P(Coffee|Cancer). 
This represents a probability of people who drink coffee given they have cancer.

Within the United States, let’s compare this to the percentage of people diagnosed with cancer (0.5% according to cancer.gov) 
and the percentage of people who drink coffee (65% according to statista.com):

Notice again that only 0.5% of the population has cancer at any given time. 
However 65% of the population drinks coffee regularly. 
If coffee contributes to cancer, should we not have much higher cancer numbers than 0.5%? Would it not be closer to 65%?

The reason people can be so easily confused by conditional probabilities is because the direction of the condition matters, 
and the two conditions are conflated as somehow being equal. The “probability of having cancer given you are a coffee drinker” 
is different from the “probability of being a coffee drinker given you have cancer.” To put it simply: few coffee drinkers have cancer, 
but many cancer patients drink coffee.

The formula to invert this is the Bayes' Theorem

P(A|B) = P(B|A) P(A) / P(B)
"""

p_coffee_drinker = .65
p_cancer = .005
p_coffee_drinker_given_cancer = .85

p_cancer_given_coffee_drinker = p_coffee_drinker_given_cancer * p_cancer / p_coffee_drinker


print(p_cancer_given_coffee_drinker)

# prints 0.006538461538461539
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# describe the decay as in
# https://www.sciencedirect.com/science/article/pii/S0013935120309890

T = 10  # temperature in degrees celcius
t = 1  # time in days


def get_ct_over_c0(T=T, t=t):

    # the rate of decay of sars-cov-2 in untreated wastewater for a temperature T (Table 5 in the paper linked above)
    k = 10 ** (0.016 * T - 1.16)

    # the proportion of the original concentration c0 remaining after time t
    ct_over_c0 = np.e ** (-k*t)

    return ct_over_c0


# check the function using values from the paper - to spot issues like wrong units
# for example from the figure, we see that ln(ct_over_c0) in untreated wastewater, at T=37, after t=18 days, is approx -5
#print(np.log(get_ct_over_c0(T=37, t=18)))
# while at 4 degrees its closer to -1.5
#print(np.log(get_ct_over_c0(T=4, t=18)))


# sample from a distribution of values for temperature T, time t
# could use the same approach to vary the parameters of the decay constant (0.016 and -1.16) to account for uncertainty
# a +- range on k is given in the paper
# could use this to determine an appropriate range

# I'm assuming a normal distribution here but might be better to use different distributions
# I don't have a copy of the draft paper with me, but there should hopefully be some details of the distributions I used in there?
T = st.norm(15, 5).rvs(100)
t = st.norm(10, 1).rvs(100) / 24  # time in days

# this is the fraction of the original concentration remaining after decay
print(get_ct_over_c0(T=T, t=t))

'''
Population variance is used when the data contains every value in the whole population. Because every value is known, the formula divides by n.

Sample variance is used when the data is only a sample taken from a larger population. A sample usually does not capture the full spread of the population perfectly. To correct this bias, sample variance divides by n - 1 instead of n. This correction is called Bessel's correction.

The same idea applies to standard deviation because standard deviation is the square root of variance.

So:
1. Population variance and population standard deviation divide by n.
2. Sample variance and sample standard deviation divide by n - 1.
3. Dividing by n - 1 usually gives a slightly larger value, which better estimates the variability of the full population from a sample.
'''

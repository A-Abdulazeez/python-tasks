def mystery(x):
    """Return the sum of the squares of all values in x."""
    y = 0
    for value in x:
        y += value ** 2
    return y


numbers = [1, 2, 3, 4, 5]
print(mystery(numbers))

'''
Output: 55
Meaning: 1**2 + 2**2 + 3**2 + 4**2 + 5**2 = 55
'''

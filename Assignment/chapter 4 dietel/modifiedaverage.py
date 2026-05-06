def average(first, *args):
    """Return the average of one or more numbers."""
    total = first + sum(args)
    count = 1 + len(args)
    return total / count


print(average(10))
print(average(10, 20, 30))
print(average(5, 10, 15, 20, 25))

# Calling average() with no argument will raise TypeError because first is required.

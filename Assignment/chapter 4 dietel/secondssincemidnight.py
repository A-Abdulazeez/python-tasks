def seconds_since_midnight(hour, minute, second):
    """Return the number of seconds since midnight."""
    hour_in_seconds = hour * 60 * 60
    minute_in_seconds = minute * 60
    return hour_in_seconds + minute_in_seconds + second


print(seconds_since_midnight(13, 30, 45))
print(seconds_since_midnight(0, 0, 0))
print(seconds_since_midnight(23, 59, 59))

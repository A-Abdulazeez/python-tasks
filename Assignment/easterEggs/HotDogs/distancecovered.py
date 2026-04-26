initial_velocity = float(input("Enter initial velocity: "))
acceleration = float(input("Enter acceleration: "))
time = float(input("Enter time: "))

distance = (initial_velocity * time) + (0.5 * acceleration * time * time)

print("The distance covered is", distance)

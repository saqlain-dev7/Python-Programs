# Determine quadrant for point (x, y)
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
if x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("On Y-axis")
elif y == 0:
    print("On X-axis")
elif x > 0 and y > 0:
    print("First quadrant")
elif x < 0 and y > 0:
    print("Second quadrant")
elif x < 0 and y < 0:
    print("Third quadrant")
else:
    print("Fourth quadrant")

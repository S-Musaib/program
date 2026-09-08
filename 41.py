hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))

hour = hour % 12

hour_angle = hour * 30 + minute * 0.5
minute_angle = minute * 6

angle = abs(hour_angle - minute_angle)

if angle > 180:
    angle = 360 - angle

print("Smaller angle:", angle)
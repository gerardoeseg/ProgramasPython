# Showing the uses of the while loop
# While controlled with an event
# Extracted from: https://goo.gl/WDVj9R

print "\nWhile controlled with an event"
print "==============================\n"

print "An example is calculating the average of degree\n"

average = 0.0
total = 0
count = 0

degree = int(raw_input(" Write a numeric value of a degree (-1 to exit): "))
while degree != -1:
    total = total + degree
    count = count + 1
    degree = int(raw_input(" Write a numeric value of a degree (-1 to exit): "))
average = total / count
print "Average of degree: " + str(average)

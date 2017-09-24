# Showing the uses of the while loop
# Complete example of a while loop
# Extracted from: https://goo.gl/WDVj9R


# With a counter----------------------------------------------------------------
print "\n\tWhile controlled with a counter"
print "\t===============================\n"

print "An example is a numeric addition until the value of counter is 10:\n"

addition = 0
number = 1
while number <= 10:
    addition = number + addition
    number = number + 1
print "The addition is: " + str(addition)

# With an event-----------------------------------------------------------------
print "\n\tWhile controlled with an event"
print "\t==============================\n"

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


# With a break sentence---------------------------------------------------------
print "\n\tWhile with a break sentence"
print "\t===========================\n"

variable = 10
while variable > 0:
    print 'Actual value of variable:', variable
    variable = variable -1
    if variable == 5:
        break

# With a continue sentence------------------------------------------------------
print "\n\tWhile with a continue sentence"
print "\t==============================\n"

variable = 10
while variable > 0:
   variable = variable -1
   if variable == 5:
      continue
   print 'Actual value of variable:', variable

# Showing the uses of the while loop
# While controlled with a counter
# Extracted from: https://goo.gl/WDVj9R

print "\nWhile controlled with a counter"
print "===============================\n"

print "An example is a numeric addition until the value of counter is 10:\n"

addition = 0
number = 1
while number <= 10:
    addition = number + addition
    number = number + 1
print "The addition is: " + str(addition)

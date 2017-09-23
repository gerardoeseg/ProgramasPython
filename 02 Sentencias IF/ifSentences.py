# Showing the uses of the if sentences
# Conditional if
# Extracted from: https://goo.gl/ZA4DRh

# Input of a number
number = int(raw_input("Write an integer, please: "))

if number < 0:
    number = 0
    print 'Negative number changed to zero'
elif number == 0:
    print 'Number is zero'
elif number == 1:
    print 'Single number'
else:
    print 'Greater than one'

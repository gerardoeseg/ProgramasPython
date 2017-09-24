# Showing the uses of the if sentences
# Logical operators
# Extracted from: https://goo.gl/ZA4DRh

a = 10
b = 20

print "\nThe value of 'a' is:", a
print "The value of 'b' is:", b

print "\n      Operator\t\tResult\n"
if ( a and b ):
   print "\tand \t'a' and 'b' are TRUE"
else:
   print "\tand \t'a' or 'b' is not TRUE"

if ( a or b ):
   print "\tor \t'a' or 'b' or both are TRUE"
else:
   print "\tor \t'a' and 'b' are not TRUE"

if not( a and b ):
   print "\tnot \t'a' and 'b' are FALSE"
else:
   print "\tnot \t'a' and 'b' are TRUE"

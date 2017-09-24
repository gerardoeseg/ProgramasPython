# Showing the uses of the if sentences
# Comparation operators
# Extracted from: https://goo.gl/ZA4DRh

a = 21
b = 10

print "\nThe value of 'a' is:", a
print "The value of 'b' is:", b

print "\n     Operator\t\tResult\n"
if ( a == b ):
   print "\t== \ta equals b"
else:
   print "\t== \ta not equals b"

if ( a != b ):
   print "\t!= \ta not equals b"
else:
   print "\t!= \ta equals b"

if ( a <> b ):
   print "\t<> \ta not equals b"
else:
   print "\t<> \ta equals b"

if ( a < b ):
   print "\t< \ta is less than b"
else:
   print "\t< \ta is not less than b"

if ( a > b ):
   print "\t> \ta is more than b"
else:
   print "\t> \ta is not more than b"

c = 5;
d = 20;

print "\nThe value of 'c' is:", c
print "The value of 'd' is:", d

print "\n     Operator\t\tResult\n"

if ( c <= d ):
   print "\t<= \t'c' is equals or less than 'd'"
else:
   print "\t<= \t'c' isn't equals or less than 'd'"

if ( d >= c ):
   print "\t>= \t'd' is equals or more than 'c'"
else:
   print "\t>= \t'd' isn't equals or more than 'c'"

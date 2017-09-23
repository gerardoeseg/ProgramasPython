# Showing de basic data types and variables on Python
# Extracted from: https://goo.gl/vnT6hp

# Integer types examples--------------------------------------------------------
# Examples
print '\nInteger data types'
print '==================\n'

# Integer / Long
a = 7
print a
print type (a)

a = 7L
print a
print type (a)

# Real number
real = 0.348
print real
print type (real)

# Real number
real = 0.56e-3
print real
print type (real)

# String types examples---------------------------------------------------------
# Examples
print '\nString data types'
print '=================\n'

# Single quotes
stringg = 'Text between single quotes'
print stringg
print type (stringg)

# Double quotes
stringd = "Text between double quotes"
print stringd
print type (stringd)

# String with scape
stringesc = 'Text between \n\t single quotes'
print stringesc
print type (stringesc)

# Multiline string
strmul = """Line 1 Text
line 2
line 3
line 4
.
.
.
.
.
line n
"""
print strmul
print type (strmul)

# Repeat string
strrep = "String" * 3
print strrep
print type (strrep)

# String concatenation
name = "Gerardo"
lastName = "Salinas"
complete_name = name + " " + lastName
print complete_name
print type (complete_name)

print "String size '", complete_name, "' is: '", len(complete_name)

# String range
print complete_name[3:13]

# Boolean types-----------------------------------------------------------------

# Examples
print '\nBoolean data types'
print '==================\n'

# Boolean data types
aT = True
print "The value is true: ", aT, ", which is a type", type(aT), "\n"

aF = False
print "The value is false: ", aF, ", which is a type", type (aF)

print '\nBoolean operators'
print '=================\n'

# Boolean operators
aAnd = True and False
print "If is true and false, then is: ", aAnd, ", type", type(aAnd)

aOr = True or False
print "If is true or false, then is:", aOr, ", type", type(aOr), "\n"

aNot = not True
print "If is not true , then is:", aNot, ", type", type(aNot), "\n"

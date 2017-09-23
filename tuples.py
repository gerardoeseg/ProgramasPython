# Showing de basic data types and variables on Python
# Tuples, is a list type that can't be modified once it was created
# Extracted from: https://goo.gl/vnT6hp

# Simple tuple example
stuple = 12345, 543221, 'hello!'

# Nested tuples example
other = stuple, (1, 2, 3, 4, 5)

# Value set on a tuple in variables
x, y, z = stuple

print "\nDefining conection to BD MySQL"
print "==============================\n"

connection_bd = "127.0.0.1", "root", "123456", "payroll",
print "Typical connection:", connection_bd
print type(connection_bd)
connection_complete = connection_bd, "3307", "10",
print "\nConnection with additional parameters: ", connection_complete
print type(connection_complete)

print "\n"

print "Accessing to the bd's IP:", connection_complete[0][0]
print "Accessing to the bd's user:", connection_complete[0][1]
print "Accessing to the bd's key:", connection_complete[0][2]
print "Accessing to the bd's name:", connection_complete[0][3]
print "Accessing to the port connection:", connection_complete[1]
print "Accessint to the wait time connection:", connection_complete[2]

print "\nMore information about MySQL and Python http://mysql-python.sourceforge.net/MySQLdb.html"

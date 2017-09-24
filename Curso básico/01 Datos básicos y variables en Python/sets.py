# Showing de basic data types and variables on Python
# Sets (conjuntos)
#    Un conjunto, es una coleccion no ordenada y sin elementos repetidos.
#    Los usos basicos de estos incluyen verificacion de pertenencia y
#    eliminacion de entradas duplicadas.
# Extracted from: https://goo.gl/vnT6hp

# Set without repeat
dish = ['cake', 'fries', 'cheese', 'biscuit']
print dish
print type(dish)
drink = ['soda', 'juice', 'coffee', 'milk']
print drink
print type(drink)

# Set in a variable
to_eat = set(dish)
print to_eat
print type(to_eat)

to_drink = set(drink)
print to_drink
print type(to_drink)

# Condicional practical example
theres_biscuit = 'biscuit' in to_eat
theres_soda = 'soda' in to_drink

print "\nToasts!"
print "======="

# Validates when an element is in the set
print "Is there biscuit?:", 'biscuit' in to_eat

if (theres_biscuit and theres_soda):
    print "Great breakfast!"
else:
    print "Light breakfast!"

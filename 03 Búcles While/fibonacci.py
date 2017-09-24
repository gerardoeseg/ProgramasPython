# Showing the uses of the while loop
# While in a Fibonacci series
# Extracted from: https://goo.gl/WDVj9R
# info: http://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci

a, b = 0, 1
while b < 100:
    print b,
    a, b = b, a + b

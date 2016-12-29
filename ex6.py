# name x with strings, insert format character
x = "There are %d types of people." % 10
# name binary with strings
binary = "binary"
# name variable with strings
do_not = "don't"
# name variable with strings
y = "Those who know %s and those who %s." % (binary,do_not)

# print variable x
print x
# print variable y
print y

# print strings,insert format character
print "I said: %r." % x
# print strings,insert format character
print "I also said: '%s'." % y

# name hilarious with False
hilarious = False
# name variable with strings
joke_evaluation = "Isn't that joke so funny?! %r"

# print variables
print joke_evaluation % hilarious

# name variable with string
w = "This is the left side of..."
# name variable with string
e = "a string with a right side."

# print variable
print w + e

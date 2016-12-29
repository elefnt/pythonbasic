# named 100 for "cars"
cars = 100
# named 4.0 for "space_in_a_car"
space_in_a_car = 4.0
# named 30 for drivers
drivers = 30
#named 90 for "passengers"
passengers = 90
# named cars_not_driven
cars_not_driven = cars - drivers
# name "cars_driven" for drivers
cars_driven = drivers
# named carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# named average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


# output the text
print "There are", cars, "cars available."
# output the text
print "There are only", drivers, "divers available."
# output the text
print "There will be", cars_not_driven, "empty cars today."
# output the text
print "We can transport", carpool_capacity, "people today."
# output the text
print "We have", passengers, "to carpool today."
# output the text
print "We need to put about", average_passengers_per_car, "in each car."

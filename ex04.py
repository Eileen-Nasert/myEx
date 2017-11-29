print "ex04"
print "Variables and Names\n"

# single-equal assings value on to the variable on the left"
# double-equal tests if two things have the same value"

cars = 100 # assigs value 100 to cars
space_in_car = 4.0 # QUESTION: why float point?
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "passengers to carpool today."
print "We need to put about", average_passengers_per_car, " passgengers in each car."

# popular names for variables are i, x, j
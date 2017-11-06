cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print( "There are", cars, "cars available." )
print( "There are only", drivers, "drivers available." )
print( "There will be", cars_not_driven, "empty cars today." )
print( "We can transport", carpool_capacity, "people today." )
print( "We have", passengers, "passengers to carpool today" )
print("We need to put about", average_passengers_per_car, "in each car." )


# Study Drills

# 0. 
#   The variable is undefined and the program can't find it. There should not be an underscore between car and pool.

# 1.
#   Not necessary, however, it only prints out intgers. Thankfully, that's all we are working with and the division yielded an integer.
# 6.
#  adam@Ubuntu-VM:~/Documents/LPTHW/Exercises/4$ python
# Python 2.7.12+ (default, Sep 17 2016, 12:08:02)
# [GCC 6.2.0 20160914] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> i = 2
# >>> j = 3
# >>> k = i*j
# >>> print(k)
# 6

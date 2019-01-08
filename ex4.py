cars = 100
sapce_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpoll_capacity = cars_driven * sapce_in_a_car
average_passeage_per_car = passengers / cars_driven

print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_driven,"emptly cars todya.")
print("We can transport",carpoll_capacity,"people today")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passeage_per_car,"in each car.")


def hotel_cost(night):
    return 140 * night


def plane_ride_Cost (city):
    if "Charlotte" == city:
        return 183
    elif "Tempa" == city:
        return 220
    elif "pittburgh" == city:
        return 222
    elif "los angeles" == city:
        return 475
    

def rental_car_cost (days):
    if days>7:
        return 40*days - 50
    elif days>3 :
        return 40*days - 20
    else:
        return 40* days
    

def trip_Cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_Cost(city) + spending_money

print ("cost of car rental: ", rental_car_cost(6))
print ("cost of plant ride: ", plane_ride_Cost("los angeles"))
print ("cost of hotel room: ", hotel_cost(7))
print ("total cost of trip: ",trip_Cost("los angeles",7,500))
print(trip_Cost("Tempa",6,500))

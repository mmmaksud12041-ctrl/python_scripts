#decalaring variables
distance_mi = 6
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = True

#Falsy Value
if  distance_mi == 0:
    print('False')

#When distance less than or equal to 1 mile
elif distance_mi <= 1:
    if is_raining == False:
        print('True')
    else:
        print('False')

#When distance is greater than 1 mile and lower than or equal to 6 miles 
elif distance_mi > 1 and distance_mi <= 6:
    if is_raining == True and has_bike == False:
        print('False')
    elif is_raining == False and has_bike == False:
        print('False')
    elif has_bike == True and is_raining == False:
        print('True')
    else:
        print('True')

#When distance is greater than 6 miles
elif distance_mi > 6:
    if has_ride_share_app == True:
        print('True')
    if has_car == True:
        print('True')
    if has_ride_share_app == False and has_car == False:
        print('False')

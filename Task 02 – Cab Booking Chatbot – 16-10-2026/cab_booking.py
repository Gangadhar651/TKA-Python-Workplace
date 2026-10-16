import random 

def select_cab():
    print("\n1. Auto - Rs.12/km")
    print("2. Sedan - Rs.18/km")
    print("3. SUV - Rs.25/km")

    choice = input("Select the cab :")

    match choice:
        case "1":
            return "Auto", 12
        case "2":
            return "Sedan", 18
        case "3":
            return "SUV", 25
        case _:
            print("Invalid cab choice!")
            return None, 0

def select_route():
    print("\n1. Pune Station to Shivajinagar - 5 km")
    print("2. Swargate to Kothrud - 8 km")
    print("3. Hinjawadi to Wakad - 10 km")

    choice = input("Select the route :")

    match choice:
        case "1":
            return "Pune Station", "Shivajinagar", 5
        case "2":
            return "Swargate", "Kothrud", 8
        case "3":
            return "Hinjawadi", "Wakad", 10
        case _:
            print("Invalid route choice!")
            return None, None, 0

def book_ride():
    cab, rate = select_cab()

    if cab is None:
        return
    
    source, destination, distance = select_route()
    if source is None:
        return
    fare = rate * distance
    print("Cab:", cab)
    print("Source:", source)
    print("Destination:", destination)
    print("Distance:", distance, "km")
    print("Rate: Rs.", rate, "/km")
    print("Total Fare: Rs.", fare)

    print("\n1. Confirm & Share OTP")
    print("2. Cancel Ride")

    hoice = input("Enter choice: ")

    match choice:
        case "1":
            otp = random.randint(1000, 9999)
            print("Your OTP is:", otp)
            print("Booking confirmed!")
            print("Cancellation is not allowed after OTP sharing.")

        case "2":
            print("Ride cancelled successfully.")
            print("No OTP shared.")

        case _:
            print("Invalid choice! Booking not confirmed.")
while(True):
    print("Book your cab....")
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter your choice :")
    match choice:
            case "1":
                book_ride()

            case "2":
                print("Thank you! Goodbye.")
                break

            case _:
                print("Invalid choice! Please try again.")


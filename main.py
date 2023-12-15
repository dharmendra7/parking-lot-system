from parking_lot import ParkingLot

def main():
    parking_lot = ParkingLot()

    while True:
        print("\n1. Assign Parking Spot")
        print("2. Retrieve Parking Spot")
        print("3. Unpark Vehicle")
        print("4. Retrieve Nearest Parking Location")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            vehicle_number = input("Enter vehicle number: ")
            result = parking_lot.assign_parking_spot(vehicle_number)
            print(f"Assigned spot: {result}")

        elif choice == '2':
            vehicle_number = input("Enter vehicle number: ")
            result = parking_lot.retrieve_parking_spot(vehicle_number)
            print(f"Parking spot: {result}")

        elif choice == '3':
            vehicle_number = input("Enter vehicle number: ")
            result = parking_lot.unpark_vehicle(vehicle_number)
            print(f"Unparked spot: {result}")

        elif choice == '4':
            level = input("Enter level (A/B): ")
            result = parking_lot.retrieve_nearest_parking_location(level)
            print(f"Nearest parking spot: {result}")

        elif choice == '5':
            break

if __name__ == "__main__":
    main()

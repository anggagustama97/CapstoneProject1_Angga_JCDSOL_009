# Sample car rental data
car_rental_data = [
    {"ID": "A1", "Brand": "Nissan", "Model": "Skyline", "Price": "100.0", "Status": "Available"},
    {"ID": "B2", "Brand": "Mitsubishi", "Model": "Evo", "Price": "120.0", "Status": "Rented"}
]

# Start Menu 1_________________________________________________________________________________________
# Function to display all car rental records
def display_all_records():
    if len(car_rental_data) == 0:     # if no data
        print("\nNo car rental records available.")
    else:
        print("\nCAR RENTAL DATA\n")
        for index, car_rental_record in enumerate(car_rental_data, start=1):
            print("{}. ID: {}, Brand: {}, Model: {}, Price: ${}, Status: {}".format(
                index,
                car_rental_record["ID"],
                car_rental_record["Brand"],
                car_rental_record["Model"],
                car_rental_record["Price"],
                car_rental_record["Status"]
            ))

# Function to display certain car rental record(s) based on ID
def display_certain_record():
    if len(car_rental_data) == 0:     #if no data
        print("\nNo car rental records available.")
    else:
        id = input("\nEnter ID of the car rental record: ").upper()
        print(f"\nCar rental record with ID: {id}")
        for car_rental_record in car_rental_data:
            if car_rental_record["ID"] == id:
                print("ID: {}, Brand: {}, Model: {}, Price: ${}, Status: {}".format(
                    car_rental_record["ID"],
                    car_rental_record["Brand"],
                    car_rental_record["Model"],
                    car_rental_record["Price"],
                    car_rental_record["Status"]
                ))
                break
        else:
            print("No car rental record found with the specified ID.") #If the for loop completes without finding a matching record

# Start Menu 2_________________________________________________________________________________________
# Function to add car rental data
def add_rental_data():
    while True:
        id = input("\nEnter the Car Rental ID: ").upper()
        if any(d["ID"].upper() == id for d in car_rental_data): # check if there is any id in data car_rental_data
            print("ID already exists.")
            return
        else:
            brand = input("Enter the Car Brand: ").capitalize()
            model = input("Enter the Car Model: ").capitalize()
            price = input("Enter the Rental Price: ")
            status = input("Enter the Rental Status: ").capitalize()
            while True:
                confirm = input("Confirm addition of new rental record? [Y/N]: ").upper()
                if confirm == 'Y':
                    new_record = {"ID": id, "Brand": brand, "Model": model, "Price": price, "Status": status}
                    car_rental_data.append(new_record)
                    print("\nNew rental record added successfully!")
                    return
                elif confirm == 'N':
                    print("\nRental record addition cancelled.")
                    return
                else:
                    print("Invalid input! Please enter [input Y/N]")

# Start Menu 3_________________________________________________________________________________________
def update_rental_data():
    while True:
        id = input("\nEnter the ID of the rental record you want to update: ").upper()
        for record in car_rental_data:
            if record["ID"].upper() == id:
                # Display data based on id
                print("\nCurrent rental record:")
                print("ID: {}, Brand: {}, Model: {}, Price: ${}, Status: {}".format(
                    record["ID"],
                    record["Brand"],
                    record["Model"],
                    record["Price"],
                    record["Status"]
                ))
                # Ask if we want to continue updating
                while True:
                    update = input("\nDo you want to update this rental record? (Y/N): ").upper()
                    if update == "N":
                        print("\nRental record update cancelled.")
                        return
                    elif update == "Y":
                        # Ask for what key/column and to update
                        key = input("\nEnter the key/column you want to update: ").capitalize()
                        value = input(f"Enter the new value for {key}: ").capitalize()
                        # Ask for confirmation to update
                        while True:
                            confirm_update = input(f"\nAre you sure you want to update {key} with {value}? [Y/N]: ").upper()
                            if confirm_update == "Y":
                                record[key] = value
                                print("\nRental record updated successfully.")
                                return
                            elif confirm_update == "N":
                                print("\nRental record update cancelled.")
                                return
                            else:
                                print("Invalid input! Please enter [input Y/N]")
                    else:
                        print("Invalid input! Please enter [input Y/N]")
        else:
            print("No car rental record found with the specified ID.") #If the for loop completes without finding a matching record
            return

# Start Menu 4_________________________________________________________________________________________
def delete_rental_data():
    while True:
        id = input("\nEnter the ID of the rental record you want to delete: ").upper()
        for i in range(len(car_rental_data)):
            if car_rental_data[i]["ID"].upper() == id:
                while True:
                    confirm_delete = input(f"\nAre you sure you want to delete data ID: {id}? [Y/N]: ").upper()
                    if confirm_delete == "Y":
                        car_rental_data.pop(i)
                        print("\nRental record deleted successfully.")
                        return
                    elif confirm_delete == "N":
                        print("\nRental record delete cancelled.")
                        return
                    else:
                        print("Invalid input! Please enter [Y/N]")
                
        else:
            print("No car rental record found with the specified ID.") #If the for loop completes without finding a matching record
            return

# Main program loop__________________________________________________________________________________
while True:
    print("\n=====CAR RENTAL DATA=====")
    print("\n1. Display Rental Records")
    print("2. Add New Car Rental Record")
    print("3. Update Car Rental Record")
    print("4. Delete Car Rental Record")
    print("5. Exit")

    choice = input("Enter your choice [1-5]: ")

    if choice == '1':
        while True:
            print("\n_______Read Rental Record_______")
            print("\n1. Display All Rental Records")
            print("2. Display Certain Data")
            print("3. Back to Main Menu")

            add_choice = input("Enter your choice [1-3]: ")

            if add_choice == '1':
                display_all_records()
            elif add_choice == '2':
                display_certain_record()
            elif add_choice == '3':
                break
            else:
                print("Invalid choice. Please try again [input 1-3].")
    elif choice == '2':
        while True:
            print("\n_______Add Record_______")
            print("\n1. Add New Car Rental Data")
            print("2. Back to Main Menu")

            add_choice = input("Enter your choice [1-2]: ")
            if add_choice == '1':
                add_rental_data()
            elif add_choice == '2':
                break
            else:
                print("Invalid choice. Please try again [input 1-2].")
    elif choice == '3':
        while True:
            print("\n_______Update Record_______")
            print("\n1. Update Car Rental Data")
            print("2. Back to Main Menu")

            add_choice = input("Enter your choice [1-2]: ")
            if add_choice == '1':
                update_rental_data()
            elif add_choice == '2':
                break
            else:
                print("Invalid choice. Please try again [input 1-2].")
    elif choice == '4':
        while True:
            print("\n_______Delete Record_______")
            print("\n1. Delete Car Rental Data")
            print("2. Back to Main Menu")

            add_choice = input("Enter your choice [1-2]: ")
            if add_choice == '1':
                delete_rental_data()
            elif add_choice == '2':
                break
            else:
                print("Invalid choice. Please try again [input 1-2].")
    elif choice == '5':
        print("\nThank You and Good Bye")
        break
    else:
        print("\nInvalid choice. Please try again [input 1-5].")
import random
import string

class Burak757:
    def __init__(self):
        # Initialize the seat map and booking databases
        self.seat_map = self.initialize_seat_map()
        self.booking_refs = {}  # Mapping from (row, col) to booking reference
        self.customer_data = {}  # Mapping from booking reference to customer data

    def initialize_seat_map(self):
        # Create a seat map where 'F' indicates free, 'X' indicates aisles, 'S' indicates storage areas
        seat_map = [['F' for _ in range(80)] for _ in range(6)]
        # Set aisles (X) and storage areas (S)
        for row in range(3, 6):
            for col in range(76, 78):
                seat_map[row][col] = 'S'
        for row in range(4):
            for col in range(3, 80, 4):
                seat_map[row].insert(col, 'X')
        return seat_map

    def display_seat_map(self):
        # Display the current seat map
        for row in range(6):
            for col in range(80 + (4 if row < 4 else 2)):
                print(self.seat_map[row][col], end=' ')
            print()

    def check_availability(self, row, col):
        # Check if a seat is available
        if self.seat_map[row][col] == 'F':
            return True
        return False

    def generate_booking_reference(self):
        # Generate a unique booking reference with 8 alphanumeric characters
        while True:
            booking_ref = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if booking_ref not in self.customer_data:
                return booking_ref

    def book_seat(self, row, col, passport_number, first_name, last_name):
        # Book a seat if it is available and save passenger information
        if self.check_availability(row, col):
            booking_ref = self.generate_booking_reference()
            self.seat_map[row][col] = booking_ref
            self.booking_refs[(row, col)] = booking_ref
            self.customer_data[booking_ref] = {
                'passport_number': passport_number,
                'first_name': first_name,
                'last_name': last_name,
                'seat_row': row + 1,
                'seat_col': col + 1
            }
            return booking_ref
        return None

    def free_seat(self, row, col):
        # Free a booked seat and remove passenger information
        if (row, col) in self.booking_refs:
            booking_ref = self.booking_refs.pop((row, col))
            if booking_ref in self.customer_data:
                del self.customer_data[booking_ref]
            self.seat_map[row][col] = 'F'
            return True
        return False

    def run(self):
        # Main menu loop
        while True:
            print("\nMenu:")
            print("1. Check seat availability")
            print("2. Book a seat")
            print("3. Free a seat")
            print("4. Show booking state")
            print("5. Exit program")

            choice = input("Enter your choice: ")

            if choice == '1':
                row = int(input("Enter row number (1-6): ")) - 1
                col = int(input("Enter column number (1-80): ")) - 1
                if self.check_availability(row, col):
                    print("Seat is available.")
                else:
                    print("Seat is not available.")
            elif choice == '2':
                row = int(input("Enter row number (1-6): ")) - 1
                col = int(input("Enter column number (1-80): ")) - 1
                if self.check_availability(row, col):
                    passport_number = input("Enter passport number: ")
                    first_name = input("Enter first name: ")
                    last_name = input("Enter last name: ")
                    booking_ref = self.book_seat(row, col, passport_number, first_name, last_name)
                    if booking_ref:
                        print(f"Seat booked successfully. Your booking reference is: {booking_ref}")
                    else:
                        print("Seat could not be booked.")
                else:
                    print("Seat is not available.")
            elif choice == '3':
                row = int(input("Enter row number (1-6): ")) - 1
                col = int(input("Enter column number (1-80): ")) - 1
                if self.free_seat(row, col):
                    print("Seat freed successfully.")
                else:
                    print("Seat could not be freed.")
            elif choice == '4':
                self.display_seat_map()
                print("\nCurrent booking database:")
                for ref, details in self.customer_data.items():
                    print(f"{ref}: {details}")
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    Burak757().run()

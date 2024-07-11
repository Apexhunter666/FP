class Burak757:
    def __init__(self):
        # Initialize the seat map
        self.seat_map = self.initialize_seat_map()

    def initialize_seat_map(self):
        # Create a seat map with 'F' for free, 'R' for reserved, 'X' for aisles, and 'S' for storage areas
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

    def book_seat(self, row, col):
        # Book a seat if available
        if self.check_availability(row, col):
            self.seat_map[row][col] = 'R'
            return True
        return False

    def free_seat(self, row, col):
        # Free a seat if reserved
        if self.seat_map[row][col] == 'R':
            self.seat_map[row][col] = 'F'
            return True
        return False

    def run(self):
        # Main loop for the menu
        while True:
            print("\nMenu:")
            print("1. Check availability of seat")
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
                if self.book_seat(row, col):
                    print("Seat booked successfully.")
                else:
                    print("Seat could not be booked.")
            elif choice == '3':
                row = int(input("Enter row number (1-6): ")) - 1
                col = int(input("Enter column number (1-80): ")) - 1
                if self.free_seat(row, col):
                    print("Seat freed successfully.")
                else:
                    print("Seat could not be freed.")
            elif choice == '4':
                self.display_seat_map()
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    Burak757().run()

class Star_Cinema:
    hall_list = []

    def entry_hall(self, obj):
        self.hall_list.append(obj)


class Hall:
    def __init__(self):
        self.show_list = []
        self.seat_map = {}

    def entry_show(self, movie_name, id, time):
        show_info = (id, movie_name, time)

        self.show_list.append(show_info)

        rows = 10
        cols = 10
        seat_map = [[False for _ in range(cols)] for _ in range(rows)]

        self.seat_map[id] = seat_map

    def book_seats(self, customer_name, phone_number, id, seats):
        show = None
        for s in self.show_list:
            if s[1] == id:
                show = s
            break

        if not show:
            print(f"Show with ID {id} not found")
            return False

        seat_map = self.seat_map.get(id)

        for seat in seats:
            row, col = seat
            if row < 0 or row >= len(seat_map) or col < 0 or col >= len(seat_map[0]):
                print(f"Invalid seat coordinates: ({row}, {col})")
                return False
            if seat_map[row][col]:
                print(f"Seat ({row}, {col}) is already booked")
                return False

        for seat in seats:
            row, col = seat
            seat_map[row][col] = True

        print(
            f"Seats {seats} booked for {customer_name} ({phone_number}) for show {id} ({show[1]} at {show[2]})")
        return True

    def view_show_list(self):
        print("___________________________________________________________________________________")
        for show in self.show_list:
            print(f"{show[1]}\t\t{show[0]}\t\t{show[2]}")
        print("___________________________________________________________________________________")

    def view_available_seats(self, show_id):
        seat_map = self.seat_map.get(show_id)

        if not seat_map:
            print(f"SHOW WITH ID {show_id} IS NOT FOUND")
        return False

        rows = len(seat_map)
        cols = len(seat_map[0])
        print(f"Available seats for show {show_id}:")
        for i in range(rows):
            for j in range(cols):
                if not seat_map[i][j]:
                    print(f"({i}, {j})")

    def start_system(self):
        while True:
            print("1. VIEW ALL SHOWS TODAY")
            print("2. VIEW AVAILABLE SEATS")
            print("3. BOOK SEAT")
            print("4. EXIT")

            choice = input("ENTER YOUR CHOICE: ")

            if choice == "1":
                self.view_show_list()

            elif choice == "2":
                id = input("ENTER THE SHOW ID: ")
                self.view_available_seats(id)

            elif choice == "3":
                show_id = input("ENTER SHOW ID: ")
                customer_name = input("Enter your name: ")
                phone_number = input("Enter your phone number: ")
                seat_list_str = input(
                    "Enter the seat coordinates (e.g. '0,0 0,1 0,2'): ")
                seat_list = [tuple(map(int, seat.split(",")))
                             for seat in seat_list_str.split()]
                self.book_seats(customer_name, phone_number,
                                show_id, seat_list)

            elif choice == "4":
                break
            else:
                print("Invalid choice, please try again")


hall = Hall()

hall.entry_show("Black Panther", "eb123", "7:00 PM")
hall.entry_show("Wonder Woman", "be234", "8:00 PM")

hall.start_system()

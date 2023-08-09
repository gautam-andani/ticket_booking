class Reserve:
    def __init__(self,train,seats=10):
        """Takes train object and number of reservable seats in that train(default=10)"""
        self.train = train
        self.seats = seats
        self.booked_seats = 0
    def book_seat(self,required_seat=2):
        """Takes required number of seats as an argument and if the seats are available mark them as book(default=2)"""
        self.required_seat = required_seat
        if self.is_available(self.required_seat):
            self.booked_seats+=required_seat
            print("Your seat has been Booked Successfully")
        else: print("Seats out of availability")
    def current_seat(self): #returns currently available seats
        return self.seats-self.booked_seats
    def is_available(self, required_seat):  #checks if the seats can be booked
            return required_seat <= self.current_seat()
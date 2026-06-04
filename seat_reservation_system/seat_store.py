class SeatStore:
    def __init__(self, seat_ids,seat_prices, seat_ranks):
        self._seats = {seat_id: None for seat_id in seat_ids}
        self._prices = seat_prices
        self._ranks = seat_ranks

    def list_seats(self):
        return self._seats.items()

    def reserve(self, seat_id, name):
        current = self._get(seat_id)
        if current is not None:
            raise ValueError("Seat is already reserved.")
        
        print(f"The seat is {self._ranks[seat_id-1]} class and costs {self._prices[seat_id-1]:,} won. Would you like to purchase this seat?")
        if input("Enter 'yes' to confirm: ").lower() != "yes":
            raise ValueError("Reservation cancelled by user.")
        self._seats[seat_id] = name
        return seat_id, name

    def cancel(self, seat_id, name=None):
        current = self._get(seat_id)
        if current is None:
            raise ValueError("Seat is not reserved.")
        if name and current != name:
            raise ValueError("Name does not match the reservation.")
        self._seats[seat_id] = None
        return seat_id, None

    def status(self, seat_id):
        return seat_id, self._get(seat_id)

    def stats(self):
        reserved = sum(1 for name in self._seats.values() if name)
        total = len(self._seats)
        return {"total": total, "reserved": reserved, "available": total - reserved}

    def _get(self, seat_id):
        if seat_id not in self._seats:
            raise ValueError("Seat does not exist.")
        return self._seats[seat_id]

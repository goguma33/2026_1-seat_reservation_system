class SeatStore:
    def __init__(self, seat_ids):
        self._seats = {seat_id: None for seat_id in seat_ids}

    def list_seats(self):
        return self._seats.items()

    def reserve(self, seat_id, name):
        current = self._get(seat_id)
        if current is not None:
            raise ValueError("Seat is already reserved.")
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

    def search(self, name): #검색 기능 추가
        results = []
        for seat_id, reserver_name in self._seats.items(): # 모든 좌석을 하나씩 확인하면서 예약자 이름을 검사
            if reserver_name == name: # 일치하면 결과 리스트에 (좌석번호, 이름) 형태로 추가
                results.append((seat_id, reserver_name))
        return results
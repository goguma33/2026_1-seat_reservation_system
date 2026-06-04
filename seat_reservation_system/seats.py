SEAT_IDS = list(range(1, 21))
SEAT_PRICES = list(int(0) for _ in range(20)) # 가격 정보 정의
SEAT_RANKS = list(str(0) for _ in range(20)) # 등급 정보 정의

for i in range(0, 5):
    SEAT_PRICES[i] = 50000
    SEAT_RANKS[i] = "Premium"


for i in range(5, 10):
    SEAT_PRICES[i] = 30000
    SEAT_RANKS[i] = "Standard"

for i in range(10, 20):
    SEAT_PRICES[i] = 15000
    SEAT_RANKS[i] = "Economy"
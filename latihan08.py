class Mobil(object):

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

carX = Mobil(240, 18)
print(f"Kecepatan : {carX.max_speed}, mileage : {carX.mileage}")





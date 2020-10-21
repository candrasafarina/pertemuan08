'''class Mobil(object):

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

carX = Mobil(240, 18)
print(f"Kecepatan : {carX.max_speed}, mileage : {carX.mileage}")'''


class Mobil:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def tampilkan_mobil(self):
        print('Kecepatan :',self.max_speed)
        print('mileage :',self.mileage)

carX = Mobil(240, 18)
carX.tampilkan_mobil()
print(f"Kecepatan : {carX.max_speed}, mileage : {carX.mileage}")

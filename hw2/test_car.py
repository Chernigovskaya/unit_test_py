from unittest import TestCase
import unittest

from hw2.car import Car
from hw2.vehicle import Vehicle


class TestCar(TestCase):
    def setUp(self):
        self.car = Car('mazda', 'm1', 2020)

    # проверка того, что экземпляр объекта Car также является экземпляром транспортного средства; (instanceof)
    def test_car_instanceof_vehicle(self):
        self.assertEqual(isinstance(self.car, Vehicle), True)

#     проверка того, объект Car создается с 4-мя колесами
    def test_car_four_wheels(self):
        self.assertEqual(self.car.num_wheels, 4)

#     проверка того, объект Car развивает скорость 60 в режиме тестового вождения (testDrive())
    def test_car_speed_test_drive(self):
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60)

# - проверить, что в режиме парковки (сначала testDrive, потом park, т.е эмуляция движения транспорта) машина останавливается (speed = 0)
    def test_park_speed(self):
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60)
        self.car.park()
        self.assertEqual(self.car.speed, 0)

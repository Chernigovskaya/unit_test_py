from unittest import TestCase

from hw2.motorcycle import Motorcycle


class TestMotorcycle(TestCase):
    def setUp(self):
        self.motorcycle = Motorcycle('yamaha', 'y1', 2020)

    # проверка того, объект Motorcycle создается с 2-мя колесами
    def test_motorcycle_two_wheels(self):
        self.assertEqual(self.motorcycle.num_wheels, 2)

    #     проверка того, объект Motorcycle развивает скорость 75 в режиме тестового вождения (testDrive())
    def test_motorcycle_speed_test_drive(self):
        self.motorcycle.test_drive()
        self.assertEqual(self.motorcycle.speed, 75)

    # проверить, что в режиме парковки (сначала testDrive, потом park  т.е эмуляция движения транспорта) мотоцикл останавливается (speed = 0)
    def test_park_speed(self):
        self.motorcycle.test_drive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0)

from abc import ABC, abstractmethod


class Vehicle(ABC):
    company: str
    model: str
    year_release: int
    num_wheels: int
    speed: int

    @abstractmethod
    def test_drive(self):
        pass

    @abstractmethod
    def park(self):
        pass
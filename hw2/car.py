from hw2.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, company, model, year_release):
        self.company = company
        self.model = model
        self.year_release = year_release
        self.num_wheels = 4
        self.speed = 0

    def test_drive(self):
        self.speed = 60

    def park(self):
        self.speed = 0


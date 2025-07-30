class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class BusChild(Vehicle):
    def fare(self):
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.10
        return base_fare + maintenance_charge


capacity = int(input("Enter the number of seats in the bus: "))
bus = BusChild(capacity)
print("Total Fare:", bus.fare())

class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = year

    def __eq__(self, other):
        return self.vid == other.vid

    def is_new(self, n):
        return (2026 - self.year) <= n

    def __str__(self):
        return f"VID: {self.vid} | {self.model} ({self.year})"

class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)
        self.fuel_type = fuel_type
        self.doors = doors

    def __str__(self):
        return f"[Car] {super().__str__()} | Fuel: {self.fuel_type} | {self.doors} Doors"

class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = max_load
        self.axles = axles

    def __str__(self):
        return f"[Truck] {super().__str__()} | Load: {self.max_load}kg | {self.axles} Axles"

class Motorcycle(Vehicle):
        def __init__(self, vid, model, year, engine_cc, m_type):
            super().__init__(vid, model, year)
            self.engine_cc = engine_cc
            self.m_type = m_type

        def __str__(self):
            return f"[Motorcycle] {super().__str__()} | Eng: {self.engine_cc}cc | Type: {self.m_type}"
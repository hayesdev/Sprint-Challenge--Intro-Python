# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
# Vehicle is the base class
class Vehicle:
    def __init__(self, name, types):
        self.name = name
        self.types = types

    def __str__(self):
        return f"Welcome to the {self.name} garage: Here are your vehicles: {self.types}"


class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__(name, types)

    def __str__(self):
        return f"Welcome to the {self.name} garage: Here are your vehicles: {self.types}"


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass


class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__(name, types)

    def __str__(self):
        return f"Welcome to the {self.name} garage: Here are your vehicles: {self.types}"


class Starship(FlightVehicle):
    def __init__(self):
        super().__init__(name, types)

    def __str__(self):
        return f"Welcome to the {self.name} garage: Here are your vehicles: {self.types}"

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
class Hangar:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        return f"Welcome to the {self.name}: Here are your vehicles: {self.categories}"


ground_vehicles = Hangar(
    'Garage', ['Car', 'Motorcycle'])

flight_vehicles = Hangar('Hangar', ['Airplane', 'Starship'])

print(ground_vehicles)
print(flight_vehicles)

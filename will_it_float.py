import customtkinter as ctk

# Create window
window = ctk.CTk()
window.geometry("400x400")
window.title("Will it float?")

# Create labels
body_label = ctk.CTkLabel(window, text="Select Body", font=("Calibri", 24))

class Body:
    def __init__(self, name, type, mass, xDimension, yDimension, zDimension):
        self.name = name
        self.type = type
        self.mass = mass
        self.xDimension = xDimension
        self.yDimension = yDimension
        self.zDimension = zDimension

    def check_type(self):
        if self.type == "Sphere":
            self.yDimension = self.xDimension
            self.zDimension = self.xDimension

    def calculate_volume(self):
        volume = self.xDimension * self.yDimension * self.zDimension
        return volume

class Fluid:
    def __init__(self, name, density):
        self.name = name
        self.density = density

# Preset instances for fluids
air = Fluid("Air", 1.293)
water = Fluid("Water", 998)
mercury = Fluid("Mercury", 13546)
vege_oil = Fluid("Vegetable Oil", 700)

box = Body("Box", "Prism", 10, 2, 5, 3)
print(box.calculate_volume())

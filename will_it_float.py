# Import Customtkinter for GUI and Math for calculations
import customtkinter as ctk
import math

# Set colour and theme of app
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Create window for app
display_window = ctk.CTk()
display_window.geometry("600x500")
display_window.title("Will it float?")

# Global variable used in methods
gravity = 9.81

# Class for object being placed within fluid
class Body:
    def __init__(self, name, type, mass, xDimension, yDimension, zDimension):
        self.name = name
        self.type = type
        self.mass = mass
        self.xDimension = xDimension
        self.yDimension = yDimension
        self.zDimension = zDimension

    def calculate_volume(self):
        if self.type == "Sphere":
            volume = (4/3) * math.pi * math.pow(self.xDimension / 2, 3)
            return volume
        elif self.type == "Cylinder":
            volume = math.pi * math.pow(self.xDimension / 2, 2) * self.yDimension
        elif self.type == "Prism":
            volume = self.xDimension * self.yDimension * self.zDimension
            return volume
        elif self.type == "Pyramid":
            volume = self.xDimension * self.yDimension * self.zDimension / 3

# Class for fluid the object is placed in 
class Fluid:
    def __init__(self, type, density):
        self.type = type
        self.density = density

# Create dropdown boxes
bodies = ["Sphere", "Cylinder", "Prism", "Pyramid"]
body_type_select = ctk.CTkOptionMenu(display_window, values=bodies)
body_type_select.grid(row=1, column=2, padx=20, pady=20)

fluids = ["Air", "Water", "Mercury", "Vegetable Oil"]
fluid_type_select = ctk.CTkOptionMenu(display_window, values=fluids)
fluid_type_select.grid(row=1, column=3, padx=20, pady=20)

# Create widgets for user to enter data into
enter_nameOfBody = ctk.CTkEntry(display_window, placeholder_text="Enter name of object:", width=200)
enter_nameOfBody.grid(row=2, column=2, padx=20, pady=20)

enter_mass = ctk.CTkEntry(display_window, placeholder_text="Enter mass of body (kg):", width=200)
enter_mass.grid(row=3, column=2, padx=20, pady=20)

enter_xValue = ctk.CTkEntry(display_window, placeholder_text="Enter X dimension of body (m):", width=200)
enter_xValue.grid(row=4, column=2, padx=20, pady=20)

enter_yValue = ctk.CTkEntry(display_window, placeholder_text="Enter Y dimension of body (m):", width=200)
enter_yValue.grid(row=5, column=2, padx=20, pady=20)

enter_zValue = ctk.CTkEntry(display_window, placeholder_text="Enter Z dimension of body (m):", width=200)
enter_zValue.grid(row=6, column=2, padx=20, pady=20)

enter_density = ctk.CTkEntry(display_window, placeholder_text="Enter density of fluid (kg/m3):", width=200)
enter_density.grid(row=2, column=3, padx=20, pady=20)

# Method to determine if object floats or not
def check_if_float():
        # Create objects for body and fluid from user inputs
        created_object = Body(enter_nameOfBody.get(), body_type_select.get(), float(enter_mass.get()), float(enter_xValue.get()), float(enter_yValue.get()), float(enter_zValue.get()))
        created_fluid = Fluid(fluid_type_select.get(), float(enter_density.get()))
        # Determine buoyancy force
        buoyancy = created_fluid.density * created_object.calculate_volume() * gravity
        # Determine weight force
        weight = created_object.mass * gravity
        # Compare buoyancy force to weight force to determine the result
        if buoyancy >= weight:
             answer_label.configure(text=f"{enter_nameOfBody.get()} floats in {fluid_type_select.get()}!")
        else:
             answer_label.configure(text=f"{enter_nameOfBody.get()} sinks in {fluid_type_select.get()}!")

# Method to clear user inputs
def clear_inputs():
     enter_nameOfBody.delete(0, 100)
     enter_mass.delete(0, 100)
     enter_xValue.delete(0, 100)
     enter_yValue.delete(0, 100)
     enter_zValue.delete(0, 100)
     enter_density.delete(0, 100)
     answer_label.delete(0, 100)

# Submit button
finish_button = ctk.CTkButton(display_window, text="Submit", font=("Calibri", 36), command=check_if_float)
finish_button.grid(row=7, column=2, padx=20, pady=20)

# Reset button
reset_button = ctk.CTkButton(display_window, text="Clear", font=("Calibri", 36), command=clear_inputs)
reset_button.grid(row=7, column=3, padx=20, pady=20)

# Answer display
answer_label = ctk.CTkLabel(display_window, text="", font=("Calibri", 24))
answer_label.grid(row=5, column=3, padx=20, pady=20)

# Function to run app
display_window.mainloop()
import customtkinter as ctk
import math

# Set colour and theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Create window
display_window = ctk.CTk()
display_window.geometry("600x500")
display_window.title("Will it float?")

gravity = 9.81

class Body:
    def __init__(self, name, type, mass, xDimension, yDimension, zDimension):
        self.name = name
        self.type = type
        self.mass = mass
        self.xDimension = xDimension
        self.yDimension = yDimension
        self.zDimension = zDimension

    def calculate_volume(self):
            volume = (4/3) * math.pi * math.pow(self.xDimension, 3)
            return volume
   
class Fluid:
    def __init__(self, name, density):
        self.name = name
        self.density = density

# Create dropdown boxes
bodies = ["Sphere", "Cube", "Prism", "Pyramid"]
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

# Create body from values
created_object = Body(enter_nameOfBody.get(), body_type_select.get(), enter_mass.get(), enter_xValue.get(), enter_yValue.get(), enter_zValue.get())

# Checks if object floats or not
def check_if_float():
        answer_label.configure(text=f"The volume of the object is {str(created_object.calculate_volume())}")

# Submit button
finish_button = ctk.CTkButton(display_window, text="Submit", font=("Calibri", 36), command=check_if_float)
finish_button.grid(row=7, column=2, padx=20, pady=20)

# Answer display
answer_label = ctk.CTkLabel(display_window, text="", font=("Calibri", 24))
answer_label.grid(row=5, column=3, padx=20, pady=20)

display_window.mainloop()
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
        if self.type == "Sphere":
            volume = (4/3) * math.pi * (self.xDimension / 2) ** 3
            return volume
        elif self.type == "Prism":
            volume = self.xDimension * self.yDimension * self.zDimension
            return volume
        
class Fluid:
    def __init__(self, name, density):
        self.name = name
        self.density = density

# Create preset bodies
cardboard_box = Body("Cardboard Box", "Prism", 1, 0.295, 0.215, 0.525)
tennis_ball = Body("Tennis Ball", "Sphere", 0.057, 2, 5, 3)

# Create labels
body_label = ctk.CTkLabel(display_window, text="Select Body", font=("Calibri", 24))
fluid_label = ctk.CTkLabel(display_window, text="Select Fluid", font=("Calibri", 24))
answer_label = ctk.CTkLabel(display_window, text="", font=("Calibri", 24))

# Format labels
body_label.grid(row=1, column=1, padx=20, pady=20)
fluid_label.grid(row=2, column=1, padx=20 , pady=20)
answer_label.grid(row=3, column=1, padx=20, pady=20)


# Checks if object floats or not
def check_if_float():
        answer_label.configure(text=enter_mass.get())


# Create dropdown boxes
bodies = ["Sphere", "Cube", "Prism", "Pyramid"]
body_type_select = ctk.CTkOptionMenu(display_window, values=bodies)
body_type_select.grid(row=1, column=2, padx=20, pady=20)
selected_body = body_type_select.get()

# Create widgets for user to enter data into
enter_mass = ctk.CTkEntry(display_window, placeholder_text="Enter mass of body:", width=200)
enter_mass.grid(row=2, column=2, padx=20, pady=20)

enter_xValue = ctk.CTkEntry(display_window, placeholder_text="Enter X dimension of body", width=200)
enter_xValue.grid(row=3, column=2, padx=20, pady=20)

enter_yValue = ctk.CTkEntry(display_window, placeholder_text="Enter Y dimension of body", width=200)
enter_yValue.grid(row=4, column=2, padx=20, pady=20)

enter_zValue = ctk.CTkEntry(display_window, placeholder_text="Enter Z dimension of body", width=200)
enter_zValue.grid(row=5, column=2, padx=20, pady=20)

# Submit button
finish_button = ctk.CTkButton(display_window, text="Submit", font=("Calibri", 36), command=check_if_float())
finish_button.grid(row=6, column=2, padx=20, pady=20)

display_window.mainloop()
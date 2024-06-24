import customtkinter as ctk
import math

# Set colour and theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Create window
display_window = ctk.CTk()
display_window.geometry("400x400")
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
    if 1 > 0:
        answer_label.configure(text="The object floats!")
    else:
        answer_label.configure(text="The object sinks!")

# Create dropdown boxes
bodies = ["Sphere", "Cube", "Prism", "Pyramid"]
body_type_select = ctk.CTkComboBox(display_window, placeholder_text="Select Body", values=bodies)
selected_body = body_type_select.get()

# Create widgets for user to enter data into
enter_mass = ctk.Entry(display_window, placeholder_text="Enter mass of body:")
enter_xValue = ctk.Entry(display_window, placeholder_text="Enter X dimension of body", state=DISABLED)
enter_yValue = ctk.Entry(display_window, placeholder_text="Enter Y dimension of body", state=DISABLED)
enter_zValue = ctk.Entry(display_window, placeholder_text="Enter Z dimension of body", state=DISABLED)

finish_button = ctk.Button(display_window, text="Submit", command=check_if_float())

display_window.mainloop()
import tkinter as tk
import math

# *Functions
def ConvertWeightToKG(weight):
    return weight / 0.45359237

#?######################################### B737-100 ##################################
def flaps_thirty_B737_100(weight):
    InitRnyLenght = 4000
    InitAircraftWeight = 80000
    result = (weight * InitRnyLenght) / InitAircraftWeight
    result_label.config(text=f"Result: {int(result)}Ft")

def flaps_forty_B737_100(weight):
    InitRnyLenght = 4000
    InitAircraftWeight = 85000
    result = (weight * InitRnyLenght) / InitAircraftWeight
    result_label.config(text=f"Result: {int(result)}Ft")

def flaps_twentyfive_B737_100(weight):
    InitRnyLenght = 5000
    InitAircraftWeight = 92500
    result = (weight * InitRnyLenght) / InitAircraftWeight
    result_label.config(text=f"Result: {int(result)}Ft")

def calculate_result_B737_100():
    weight = ConvertWeightToKG(int(AircraftWeight.get()))
    flaps_configuration = selectedFlaps.get()

    if flaps_configuration == "Flaps 25":
        flaps_twentyfive_B737_100(weight)
    elif flaps_configuration == "Flaps 30":
        flaps_thirty_B737_100(weight)
    elif flaps_configuration == "Flaps 40":
        flaps_forty_B737_100(weight)
#?#########################################################################################################
#?------------------------------------------------------------------------------------------------------------------
#?######################################### B737-200 ######################################################
def flaps_thirty_B737_200(weight):
    InitRnyLenght = 4500
    InitAircraftWeight = 90000
    result = (weight * InitRnyLenght) / InitAircraftWeight
    result_label.config(text=f"Result: {int(result)}Ft")

def flaps_forty_B737_200(weight):
    InitRnyLenght = 4500
    InitAircraftWeight = 100000
    result = (weight * InitRnyLenght) / InitAircraftWeight
    result_label.config(text=f"Result: {int(result)}Ft")

def flaps_twentyfive_B737_200(weight):
    InitRnyLenght = 4450
    InitAircraftWeight = 80000
    result = (weight * InitRnyLenght) / InitAircraftWeight
    result_label.config(text=f"Result: {int(result)}Ft")

def calculate_result_B737_200():
    weight = ConvertWeightToKG(int(AircraftWeight.get()))
    flaps_configuration = selectedFlaps.get()

    if flaps_configuration == "Flaps 25":
        flaps_twentyfive_B737_200(weight)
    elif flaps_configuration == "Flaps 30":
        flaps_thirty_B737_200(weight)
    elif flaps_configuration == "Flaps 40":
        flaps_forty_B737_200(weight)



#?#########################################################################################################
#?------------------------------------------------------------------------------------------------------------------
#?################################################### Aircraft Selector #####################################3
def AircraftTypeSelector(*args):
    aircraft_type = selectedType.get()

    if aircraft_type == "B737-100":
        CalculateBTN.config(command=calculate_result_B737_100)
    elif aircraft_type == "B737-200, -200C":
        CalculateBTN.config(command=calculate_result_B737_200)  # Add the appropriate calculation function for this aircraft type

# Window
window = tk.Tk()

# Dropdown variable
selectedFlaps = tk.StringVar()
selectedType = tk.StringVar()

# Get aircraft weight
label = tk.Label(window, text="Weight : ")
label.pack()

AircraftWeight = tk.Entry(window)
AircraftWeight.pack()

# Flaps Configuration
FlapsConfigurationoptions = {"Flaps 25", "Flaps 30", "Flaps 40"}
FlapsConfiguration = tk.OptionMenu(window, selectedFlaps, *FlapsConfigurationoptions)
FlapsConfiguration.pack()

# Aircraft Type
AircraftTypeOption = {"B737-100", "B737-200, -200C"}
AircraftTypeDropdown = tk.OptionMenu(window, selectedType, *AircraftTypeOption, command=AircraftTypeSelector)
AircraftTypeDropdown.pack()

# Calculate Result
CalculateBTN = tk.Button(window, text="Calculate")
CalculateBTN.pack()

# Display Result
result_label = tk.Label(window, text="")
result_label.pack()

# Other widgets
window.mainloop()
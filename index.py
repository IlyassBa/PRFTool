import tkinter as tk
import math

# *Functions
#?###########################################################################################################
#?-----------------------------------------------------------------------------------------------------------
#?############################################ Weight Converter  #####################################
def ConvertWeightToKG(weight):
    return weight / 0.45359237

#?###########################################################################################################
#?-----------------------------------------------------------------------------------------------------------
#?############################################ Configuration Calculator #####################################
def Configuration(weight,InitRnyLenght,InitAircraftWeight):
    result = (weight * InitRnyLenght) / InitAircraftWeight
    result_label.config(text=f"Result: {int(result)}Ft")

#?###########################################################################################################
#?-----------------------------------------------------------------------------------------------------------
#?################################################### Aircraft Selector #####################################
def AircraftTypeSelector(flaps,type,rnycondition,elevation):
    print("Flaps: " + str(flaps) + " Type: " + type + " Rny: " + rnycondition + " Elevation: " + str(elevation) )

# ! Check the wet part and change values to real values form b737 POH
    if type == "B737-100":
        
        if rnycondition == "dry":
            if 0 < elevation < 4000 :
                if flaps == "Flaps 40" :
                    InitRnyLenght = 4000
                    InitAircraftWeight = 85000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 30":
                    InitRnyLenght = 4000
                    InitAircraftWeight = 80000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 25":
                    InitRnyLenght = 4100
                    InitAircraftWeight = 75000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
            
            
            elif 4000 < elevation < 8000 :
                if flaps == "Flaps 40" :
                    InitRnyLenght = 5000
                    InitAircraftWeight = 95000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 30":
                    InitRnyLenght = 5000
                    InitAircraftWeight = 90000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 25":
                    InitRnyLenght = 5000
                    InitAircraftWeight = 85000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
            
            elif 8000 < elevation :
                if flaps == "Flaps 40" :
                    InitRnyLenght = 4050
                    InitAircraftWeight = 80000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 30":
                    InitRnyLenght = 5500
                    InitAircraftWeight = 90000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 25":
                    InitRnyLenght = 5500
                    InitAircraftWeight = 85000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
            
        if rnycondition == "wet":

            if 0 < elevation < 4000 :
                if flaps == "Flaps 40" :
                    InitRnyLenght = 5000
                    InitAircraftWeight = 95000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 30":
                    InitRnyLenght = 4500
                    InitAircraftWeight = 75000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 25":
                    InitRnyLenght = 6000
                    InitAircraftWeight = 95000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
            
            
            if 4000 < elevation < 8000 :
                if flaps == "Flaps 40" :
                    InitRnyLenght = 5000
                    InitAircraftWeight = 85000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 30":
                    InitRnyLenght = 5400
                    InitAircraftWeight = 85000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 25":
                    InitRnyLenght = 5500
                    InitAircraftWeight = 85000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
            
            if 8000 < elevation :
                if flaps == "Flaps 40" :
                    InitRnyLenght = 5500
                    InitAircraftWeight = 85000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 30":
                    InitRnyLenght = 6500
                    InitAircraftWeight = 95000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 25":
                    InitRnyLenght = 5900
                    InitAircraftWeight = 55000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
          



    elif type == "B737-200, -200C":

        
        if rnycondition == "dry":
            if 0 < elevation < 4000 :
                if flaps == "Flaps 40" :
                    InitRnyLenght = 4500
                    InitAircraftWeight = 10000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 30":
                    InitRnyLenght = 4500
                    InitAircraftWeight = 90000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 25":
                    InitRnyLenght = 4500
                    InitAircraftWeight = 80000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
            
            
            if 4000 < elevation < 8000 :
                if flaps == "Flaps 40" :
                    InitRnyLenght = 5000
                    InitAircraftWeight = 100000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 30":
                    InitRnyLenght = 4500
                    InitAircraftWeight = 80000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 25":
                    InitRnyLenght = 4500
                    InitAircraftWeight = 80000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
            
            if 8000 < elevation :
                if flaps == "Flaps 40" :
                    InitRnyLenght = 5500
                    InitAircraftWeight = 100000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 30":
                    InitRnyLenght = 6900
                    InitAircraftWeight = 10000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 25":
                    InitRnyLenght = 6000
                    InitAircraftWeight = 90000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
            
        if rnycondition == "wet":
            if 0 < elevation < 4000 :
                if flaps == "Flaps 40" :
                    InitRnyLenght = 5000
                    InitAircraftWeight = 95000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 30":
                    InitRnyLenght = 4500
                    InitAircraftWeight = 75000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 25":
                    InitRnyLenght = 6000
                    InitAircraftWeight = 95000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
            
            
            if 4000 < elevation < 8000 :
                if flaps == "Flaps 40" :
                    InitRnyLenght = 5000
                    InitAircraftWeight = 85000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 30":
                    InitRnyLenght = 5400
                    InitAircraftWeight = 85000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 25":
                    InitRnyLenght = 5500
                    InitAircraftWeight = 85000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
            
            if 8000 < elevation :
                if flaps == "Flaps 40" :
                    InitRnyLenght = 5500
                    InitAircraftWeight = 85000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 30":
                    InitRnyLenght = 6500
                    InitAircraftWeight = 95000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
                elif flaps == "Flaps 25":
                    InitRnyLenght = 5900
                    InitAircraftWeight = 55000
                    CalculateBTN.config(command=Configuration( ConvertWeightToKG(int(AircraftWeight.get())) ,InitRnyLenght ,InitAircraftWeight ))#calculate_result_B737_100
          


        

#?###############################################################################################################
#?---------------------------------------------------------------------------------------------------------------
#?################################################### Tkinter Configuration #####################################
# Window
window = tk.Tk()

# Dropdown variable
selectedFlaps = tk.StringVar()
selectedType = tk.StringVar()
selectedrnycdt = tk.StringVar()

# Get aircraft weight
label = tk.Label(window, text="Weight : (KG)")
label.pack()

AircraftWeight = tk.Entry(window)
AircraftWeight.pack()

# Flaps Configuration
# Get aircraft weight
FlapsConfigurationoptions = {"Flaps 25", "Flaps 30", "Flaps 40"}
FlapsConfiguration = tk.OptionMenu(window, selectedFlaps, *FlapsConfigurationoptions)
FlapsConfiguration.pack()

# Aircraft Type
AircraftTypeOption = {"B737-100", "B737-200, -200C"}
AircraftTypeDropdown = tk.OptionMenu(window, selectedType, *AircraftTypeOption)
AircraftTypeDropdown.pack()

# Runway Condition
RunwayConditionOption = {"dry", "wet"}
RunwayConditionDropdown = tk.OptionMenu(window, selectedrnycdt, *RunwayConditionOption)
RunwayConditionDropdown.pack()

# Get rny elevation
rnyElevationLabel = tk.Label(window, text="Runway Elevation : (FT)")
rnyElevationLabel.pack()

rnyElevationEntry = tk.Entry(window)
rnyElevationEntry.pack()
# Calculate Result
CalculateBTN = tk.Button(window, text="Calculate", command=lambda:AircraftTypeSelector( selectedFlaps.get() , selectedType.get() , selectedrnycdt.get() , int(rnyElevationEntry.get())))
CalculateBTN.pack()

# Display Result
result_label = tk.Label(window, text="")
result_label.pack()

# Other widgets
window.mainloop()
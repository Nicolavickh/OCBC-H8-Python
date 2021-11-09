# A function to converto from Celcius to Kelvin or vice versa
def convertCelciusKelvin(tempterature, command):
    # If statement to see if the funcntion is called to convert Celcius to Kelvin or vice versa
    # Inputs: 
    # param 1 temperature: input for temperature | int or float 
    # param 2 command: input for temparature convert command (to Celcius or Kelvin) | string 
    if(command == "CK"):
        # Return the converted temperature | int or float
        return tempterature + 273.15
    elif(command == "KC"):
        # Return the converted temperature | int or float
        return tempterature - 273.15
    return ("Command unrecognized!")

# A function to conver to from Celcius or Kelvin to Fahrenheit
def convertToFahrenheit(temperature, unit):
    # If statement to see if the funcntion is called to convert to Celcius to Kelvin
    # Inputs: 
    # param 1 temperature: input for temperature | int or float 
    # param 2 unit: input for temparature convert from what unit (to Celcius or Kelvin) | string 
    if (unit == "K"):
        # Return the converted temperature | int or float
        return (temperature - 273.15) * 9 / 5 + 32
    elif (unit == "C"):
        # Return the converted temperature | int or float
        return temperature * 9 / 5 + 32
    return "Unit unrecognized!"

#A funtion to convert from Fahrenheit to Celcius and Kelvin
def convertFromFahrenheit(temperature):
    # Return the converted temperature as a dictionary with 'K' and 'C' key representing Kelvin adn Celcius
    # Inputs: 
    # param 1 temperature: input for temperature | int or float 
    # Return the converted temperature | int or float
    return {'K': (temperature - 32) * 5/9 + 273.15, 'C': (temperature-32) * 5/9}

# Main function to run the program 
def main():
    print("===== Simple temperature converter app =====")
    convertFrom = -1
    
    # While loop so that the user choose the correct menu 
    while(convertFrom < 1 or convertFrom > 3):
        print("Convert from: ")
        print("1. Celcius")
        print("2. Kelvin")
        print("3. Fahrenheit")
        convertFrom = int(input("Your choice: "))
        print("==============================")
    
    # While loop so that the user choose the correct menu 
    convertTo = 0
    while(convertTo < 1 or convertTo > 2):
        print("Convert to: ")
        if(convertFrom == 1):
            print("1. Kelvin")
            print("2. Fahrenheit")
        elif(convertFrom == 2):
            print("1. Celcius")
            print("2. Fahrenheit")
        elif(convertFrom == 3):
            print("1. Celcius")
            print("2. Kelvin")
        convertTo = int(input("Your choice: "))
        print("==============================")

    # Input the temperature 
    temperature = float(input("Temperature: "))
    
    # if statement to see which result should be given based on the choosen menu
    if(convertFrom == 1 and convertTo == 1):
        # Print out the converted temperature based on the desired output unit
        print("Converted from Celcius to Kelvin: ", convertCelciusKelvin(temperature, "CK"))
    elif(convertFrom == 1 and convertTo == 2):
        # Print out the converted temperature based on the desired output unit
        print("Converted from Celcius to Fahrenheit: ", convertToFahrenheit(temperature,"C"))
    elif(convertFrom == 2 and convertTo == 1):
        # Print out the converted temperature based on the desired output unit
        print("Converted from Kelvin to Celcius: ", convertCelciusKelvin(temperature,"KC"))
    elif(convertFrom == 2 and convertTo == 2):
        # Print out the converted temperature based on the desired output unit
        print("Converted from Kelvin to Fahrenheit: ", convertToFahrenheit(temperature,"K"))
    elif(convertFrom == 3 and convertTo == 1):
        # Print out the converted temperature based on the desired output unit
        print("Converted from Fahrenheit to Celcius: ", convertFromFahrenheit(temperature)['C'])
    elif(convertFrom == 3 and convertTo == 2):
        # Print out the converted temperature based on the desired output unit
        print("Converted from Fahrenheit to Kelvin: ", convertFromFahrenheit(temperature)['K'])

if __name__ == "__main__":
    main()
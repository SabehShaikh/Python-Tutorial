# Program to convert Celsius to Fahrenheit

# formula > (C * 9/5) + 32

def celsius_to_fahrenheit(c):
    return round((c * 9/5) + 32, 2)  # Round to 2 decimal places

c = float(input("Enter temperature in Celsius: "))
print(f"The temperature in Fahrenheit is: {celsius_to_fahrenheit(c)}")


# Program to convert Fahrenheit to Celsius

# formula > 5 * (f-32) / 9
def fahrenheit_to_celsius(f):  
    return round(5 * (f - 32) / 9, 2)  # Round to 2 decimal places

f = float(input("Enter temperature in Fahrenheit: "))
print(f"The temperature in Celsius is: {fahrenheit_to_celsius(f)}")

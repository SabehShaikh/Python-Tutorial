# convert from inch to cm:

def inch_to_cm(inch):
    return inch * 2.54

inch = float(input("Enter length in inch: "))
print(f"The length in cm is: {inch_to_cm(inch)}")

# convert from cm to inch:

def cm_to_inch(cm):
    return cm / 2.54

cm = float(input("Enter length in cm: "))
print(f"The length in inch is: {cm_to_inch(cm)}")
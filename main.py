print("=== WELCOME TO VALUE CONVERTER APP ===\n")

while True:
    print("choose the type of conversion below")
    print("1. Celsius to Fahrenheit")
    print("2. Rupee to Pound")
    print("3. Centimeter to Foot")
    print("4. Exit")
    convert_format = int(input("Enter your choice: "))
    if convert_format == 1:
        convert_value = int(input("Enter the value you wish to convert: "))
        value = convert_value * 33.8
        print(f"answer is; {value}°F")
        break
    elif convert_format == 2:
        convert_value = int(input("Enter the value you wish to convert: "))
        value = convert_value * 0.011
        print(f"answer is; {value}pounds")
        break
    elif convert_format == 3:
        convert_value = int(input("Enter the value you wish to convert: "))
        value = convert_value * 0.033
        print(f"answer is; {value}FT")
        break
    elif convert_format == 4:
        print("Exiting...")
        break
    else:
        print("Invalid code")
        break















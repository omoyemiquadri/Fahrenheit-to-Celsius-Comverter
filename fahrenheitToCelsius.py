def converter(temp, type):
    if type=='F':
        celsius = 5/9 * (temp-32)
        return celsius
    elif type=='C':
        fahrenheit = temp * (9/5) + 32
        return fahrenheit
    else:
        print("Wrong input")


print("Enter the temperature")

temp = float(input("> "))
type = input(f"(F)ahrenheit or (C)celsius: ").upper()

result = converter(temp, type)
print(f"your temp is {result}°")

product_name = "Laptop"
price = 999.99
in_stock = True

print(f"Product: {product_name}, Price: ${price}, In Stock: {in_stock}")

first_name = "nabila"
last_name = "saeed"

full_name = first_name + " " + last_name

print("Full name:", full_name)

temperature = 25
is_raining = False

if temperature > 20 and not is_raining:
    print("It's a nice day to go outside.")

    age=18
    if age >=18:
        print(" You are adult.")

        temperature=10
        if temperature >=30:
            print("weather is hot today:")
        elif temperature >20:
            print("weather is pleasant today:")
        else:
            print("its a bit chilly,")

            temperature = 35
is_raining = False

if temperature > 20 and not is_raining:
    print("It's a nice day to go outside.")

    is_sunny = True
is_weekend = False

if is_sunny or is_weekend:
    print("You can go for a walk.")
else:
    print("Maybe stay indoors.")

day = "Monday"

match day:
    case "Monday":
        print("Start of the work week.")
    case "Friday":
        print("Almost the weekend!")
    case _:
        print("Have a nice day!")
number = 7

match number:
    case 1 | 2 | 3:
        print("Low number")
    case 4 | 5 | 6:
        print("Medium number")
    case _:
        print("High number")

        age = 25
has_id = True

if age >= 11:
    if has_id:
        print("You can enter the club.")
    else:
        print("ID required to enter.")
else:
    print("You are too young to enter.")

    temperature = 15
is_raining = True

if temperature > 20:
    if not is_raining:
        print("You can go for a walk.")
    else:
        print("It's raining, bring an umbrella.")
else:
    print("It's too cold for a walk.")

age = 18
message = "Adult" if age >= 18 else "Minor"
print(message)

score = 85
result = "Pass" if score >= 50 else "Fail"
print(result)
numbers = [1, 2, 3]

match numbers:
    case [1, 2, 3]:
        print("Matched the list [1, 2, 3]")
    case [x, y, z]:
        print(f"Matched a list with three elements: {x}, {y}, {z}")
    case _:
        print("No match")

        temperature = 68
is_raining = False
is_snowing = False

if (temperature > 20 and not is_raining) or is_snowing:
    print("Weather is suitable for outdoor activities.")
else:
    print("Weather conditions are not ideal.")

    is_weekend = False
is_holiday = True

if not is_weekend and is_holiday:
    print("Enjoy your day off!")
else:
    print("It's a regular workday.")


number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

    temperature = float(input("Enter the temperature in degrees Celsius: "))

if temperature <= 0:
    print("It's Freezing.")
elif 0 < temperature <= 10:
    print("It's Cold.")
elif 10 < temperature <= 25:
    print("It's Mild.")
else:
    print("It's Hot.")
    age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")


    count = 0

while count < 5:
    print(count)
    count += 1
    number = 10

while number > 0:
    print(number)
    number -= 1

    fruits=["apples","banana","cherry"]
    for fruit in fruits:
        print(fruit)



    












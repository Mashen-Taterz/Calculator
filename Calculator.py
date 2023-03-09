#basic calculator
first_number = input(float("First number is "))
second_number = input(float("Second number is "))
calculation_type = input("what would you like to do? (+,-,*,/) ")

add_numbers = (first_number) + (second_number)
subtract_numbers = (first_number) - (second_number)
multiply_numbers = (first_number) * (second_number)
divide_numbers = (first_number) / (second_number)

if calculation_type == "+":
  print(add_numbers)
elif calculation_type == "-":
  print(subtract_numbers)
elif calculation_type == "*":
  print(multiply_numbers)
elif calculation_type == "/":
  print(divide_numbers)
else:
  print("Try again!")
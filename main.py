
#basic calculator
first_number = input("First number is ")
second_number = input("Second number is ")
calculation_type = input("what would you like to do? (+,-,*,/) ")

add_numbers = float(first_number) + float(second_number)
subtract_numbers = float(first_number) - float(second_number)
multiply_numbers = float(first_number) * float(second_number)
divide_numbers = float(first_number) / float(second_number)

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





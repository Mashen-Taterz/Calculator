name = input("What is your name? ")
fav_color = input("What is your favorite color? ")

#print(name,"'s favorite color is ", fav_color) #bad design
print(f"{name}'s favorite color is {fav_color}.")

birth_year = int(input("What year were you born? "))
age = 2023 - birth_year
print(f"{name} will be {age} this year!")



my_list = [1,2,3,4,5]
print(my_list)

my_list.append(6)
print(my_list)

my_list.insert(0,0)
print(my_list)

print(len(my_list))

my_list.pop(6)
print(my_list)

my_list.reverse()
print(my_list)

example_number = 0
while example_number <= 3:
  print(example_number)
  example_number += 1

my_list = [1,2,3,4,5]
for number in my_list:
  print(number)


for number in my_list:
  print(number * 2)

print(3 in (my_list))

print(7 in (my_list))

numbers = range (5)
print(numbers)

new_numbers = range (5, 10)
for number in new_numbers:
  print(number)
  
for number in range(10):
  print(number)





# Continue statement
for i in range(10):
    if i == 5:
        continue
    print(i)

patient_name = input("What is your name? ")
patient_age = input("How old are you? ")
is_new_patient = input("Are you a new patient? (y/n) ")
if is_new_patient == "y":
  is_new_patient = True
else:
  is_new_patient = False

print("Hello " + patient_name)
print("You are " + patient_age + " years old.")
if is_new_patient == True:
  print("Welcome!")
else: 
  print("Welcome Back!")
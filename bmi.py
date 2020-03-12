# This file calculates a person's Body Mass Index

weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in centimetres: "))

# weight = 65
# height = 180

hm2 = ((height / 100) **2)

BMI = weight / hm2
BMI2 = (round (BMI,2))

print("Your Body Mass Index Score is", BMI2)

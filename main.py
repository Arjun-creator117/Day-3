#(average of both parents height, then add 2.5 inch if boy, subtract if girl)
print("let's calculate your height in the future!")
print("Enter the average of both your parents height rounded to the nearest foot")

height = float(input("\n\n\n \n\n\n\n")) * 12.0
print(type(height))
print('height in inches', height)

gender = input("Enter if you are a boy or girl: ")
print(type(gender))

if gender == "boy":
  boy = height + 2.5
  print("Your future height will be: ", boy)
else:
  girl = height - 2.5
  print("Your future height will be: ", girl)
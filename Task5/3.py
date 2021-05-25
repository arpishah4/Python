# Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits”


try:
  num = (input("Enter the 4 digit number: "))
  if len(num)<4 or len(num)>4:
      raise ValueError

except ValueError:
    print("the length is too short/long: ")

else:
    print("It is perfect:")




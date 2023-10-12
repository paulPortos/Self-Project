#Create a program that can take in input of the users name
#Save the name in a variable 
#Pass the variable through a function and print hello _____
#HANGMAN PROJECT 27/09/2023

usersName = input("What is your name? ")
def callOut(i):
  i = "Hello "
  i += usersName
  return i

i = callOut(usersName)
print(i)
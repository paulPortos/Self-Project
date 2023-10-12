#1) Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.

def number1():
  def computation(i):
    inputN = int(input("Enter Number: "))
    while inputN > 0 or inputN == 0:
      inputN = int(input("Enter Number: "))
      i += inputN
      if inputN < 0:
        return i
  computation(0)
  x = computation(0)
  print(x)
  

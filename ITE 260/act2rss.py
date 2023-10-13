inputNumber = int(input("Enter number: "))
total = 0
x = 1
print("Multiples of", inputNumber , ":", end=" ")
for i in range(0,10):
  total += inputNumber
  print(total, end="")
  if x <= 9:
    print("," , end="")
    x+=1
    
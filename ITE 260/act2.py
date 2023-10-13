#Name: Ahron Paul P. Villacote
#Section: BSIT1-01

#Write a program that will give for a list of ruits with designated price and it will ask you a fruit for a list that you want and it will add all of the fruits that you want and give the total price
fruits = ["Apple", "Orage", "Grapes", "Dalandan"]
fruitBought = []
totalPieces = []
prices = []
totalPriceBought = 0
print("Select your fruit: ")
print("Apple = 5$")
print("Orange = 4$")
print("Grapes = 20$")
print("Dalandan = 15$")
print("")
def interaction():
  global inputedFruit, pieces, askingForMore
  inputedFruit = input("Enter fruit that you want: ")
  pieces = int(input("How many pieces: "))
  askingForMore = input("Do you want more? [y/n]: ")
  if inputedFruit.lower() == "apple": 
    prices.append(5 * pieces)
  elif inputedFruit.lower() == "orange": 
    prices.append(4 * pieces)
  elif inputedFruit.lower() == "grapes": 
    prices.append(20 * pieces)
  elif inputedFruit.lower() == "dalandan":
    prices.append(15 * pieces)
  fruitBought.append(inputedFruit)
  totalPieces.append(pieces)
  
while True:
  interaction()
  if askingForMore.lower() == "y":
    continue
  elif askingForMore.lower() == "n":
    break

print("Orders: ")
run = 1
for i in fruitBought:
  index = run - 1
  print(i , ': ', end="")
  print(totalPieces[index], "pcs")
  run +=1

for total in prices:
  totalPriceBought += total
print ("Total: ", totalPriceBought)
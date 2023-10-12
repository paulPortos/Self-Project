import random

spaces = [1,2,3,4,5,6,7,8,9]
comp_choice = []
player_win = True

print("Welcome to tic tac toe!")

def main():
  print("")
  print(spaces[0], " ", spaces[1], " ",spaces[2])
  print(spaces[3], " ", spaces[4], " ",spaces[5])
  print(spaces[6], " ", spaces[7], " ",spaces[8])
  
def randomizer():
  global rnd_spaces
  while True:
    rnd_spaces = random.choice(spaces)
    print("Computer:",rnd_spaces)
    x,o='X','O'
    if rnd_spaces not in comp_choice and spaces != x and spaces != o:
      comp_choice.append(rnd_spaces)
      break
      
def loopings():
  global player
  while True:
    main()
    player = int(input("Enter number: "))
    if player not in comp_choice and player in spaces:
      playerChoiceIndication()
      randomizer()
      computerChoiceIndication()
#BUG
def playerChoiceIndication():

  if player in spaces:
    reSpace = player - 1
    while True:
        spaces[reSpace] = 'O'
        break
        
def computerChoiceIndication():
  
  if rnd_spaces in spaces:
    reSpace = rnd_spaces - 1
    print("line 50")
    if reSpace in spaces:
      spaces[reSpace] = 'X'
  
def run():
  loopings()

run()
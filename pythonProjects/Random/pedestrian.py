import time
#Still constructing
print("Pedestrian Countdown")

def countdown(t):
  runs = 1
  while t:
    mins, secs = divmod(t,60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1
  if runs == 1:
    runs = 2
    firstGoCommand()
  elif runs == 2:
    runs = 3
    secondGoCommand()
  else:
    stopCommand()


def choice():
  global run
  run = 1
  global side 
  side =  input("Enter side(right/left): ")
  if side == "Right" or side == "right":
    countdown(10)
  elif side == "Left" or side == "left":
    countdown(10)

def firstGoCommand():
  if side == "Right" or side == "right":
    print("Go left!")
    
    countdown(10)
  elif side == "Left" or side == "left":
    print("Go right!")
    
    countdown(10)
  
def secondGoCommand():
  if side == "Right" or side == "right":
    print("Go right!")
    countdown(10)
  elif side == "Left" or side == "left":
    print("Go left!")
    countdown(10)

def stopCommand():
  print("STOP!")

choice()
print(run)
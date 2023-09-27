def stringy(size):
  global i
  i = []
  while size > len(i): 
    
    if len(i) % 2: 
      i.append("0")
      
    else:
      i.append("1")
  display()
  
def display():
      seq = 0 
      while seq < len(i):
        print(i[seq], end="")
        seq+=1
        
stringy(10)
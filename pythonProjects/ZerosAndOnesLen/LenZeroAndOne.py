def stringy(name):
  term = 0 
  global output
  output = []
  while len(name) > term:
    term += 1
    if term % 2:
      output.append("1")

    else: 
      output.append("0")
  display()
  
def display():
  secondTerm = 0
  while len(output) > secondTerm:
    print(output[secondTerm] , end="")
    secondTerm+=1


stringy("Ahron")
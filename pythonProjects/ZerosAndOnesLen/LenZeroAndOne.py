import textwrap

def zerosAndOnes(name):
  term = 0 
  while len(name) > term:
    term += 1
    if term % 2:
      print("0")

    else: 
      print("1")


zerosAndOnes("Ahron")
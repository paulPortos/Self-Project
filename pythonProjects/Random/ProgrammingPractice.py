class ProgrammingPractice:
  def q4():
    age = int(input("Enter Age: "))
    votersId = input("Do you have a voters ID?(Yes/No): ")

    if age >= 18 and votersId == "Yes":
      print("You are eligible to vote")

    elif age >= 18 and votersId == "No":
      print("You are not eligible to vote")

    elif age < 18 and votersId == "Yes":
      print("Needs verification")

    else:
      print("You are not eligible to vote")

  def q6():
    number = int(input("Enter Age: "))

    if number % 7:
      print("The number " , number , "is not divisible by 7")
    
    else:
      print("The number " , number , "is divisible by 7")














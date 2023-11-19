print("Welcome to the tip calculator.")
bill=float(input("what is the total of the bill\n $"))
tip=int(input("what pecentage of tip would you like to give?\n10%,15%,20%\n"))
people=int(input("How many people to split the bill in between\n"))
total=round(((bill*tip)/100)/people,2)
print(f"Each person has to pay: ${total}")
      
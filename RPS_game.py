import random
print("welcome to the Rock Paper Scissor game")
print("to play rock enter '0' to play paper enter '1' to play scissor enter '2'")
ch=int(input());
print("your choice is:")
if ch == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

elif ch== 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

elif ch==2:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")        
else:
    print("your option is invalid")    
cch=random.randint(0,2)
print("The computer's choice is:")
if cch == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

elif cch== 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

elif cch==2:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("your option is invalid")            

if ch==cch:
    print("The game is a draw")
elif ch==0 and cch==2:
    print("you have won")
elif ch==0 and cch==1:
    print("you have lost")        
elif ch==1 and cch==0:
    print("you have won")
elif ch==1 and cch==2:
    print("you have lost")        
elif ch==2 and cch==0:
    print("you have won")
elif ch==2 and cch==1:
    print("you have lost")                
import random
numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,100]
VALUE=int(random.choice(numbers))

def working(no_of_lives):
    '''this calculates the no of lives to play and says when you have lost'''
    con=False
    print("Guess an number between 0 to 100:")
    print(f"You have {no_of_lives} chances.")
    while(con==False):
        vic=guessing(no_of_lives)
        if vic==False:
            no_of_lives-=1
        if no_of_lives<=0:
            print("You have lost.")
            exit()
        print(f"You have {no_of_lives} reaming chances.")

def guessing(no_of_lives):
    '''here the given input is compared with the number to be guessed'''
    choice=int(input("Enter your guess:\n"))
    global VALUE
    if(choice!=VALUE):
        diff=VALUE-choice
        if diff>0:
            print("The number you are searching for lies ahead.")
        elif diff<0:
            print("The number you are searching for lies behind.")
        win=False
        return win          
    else:
        print("The number you have been searching for has been found.")
        exit() 

def begining():
    '''this made to restart the program for a wrong input '''
    print("You are playing Guess the number.")
    cho=input("Do you want to play in easy mode or hard mode: ").lower()
    if cho=="hard mode":
        working(no_of_lives=5)
    elif cho=="easy mode":
        working(no_of_lives=10)
    else:
        begining()

begining()
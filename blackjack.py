import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user=[]
system=[] 
    
def part_1():
    i=0
    total=0
    while(i<2):
        user.append(random.choice(cards))    
        i+=1
    i=0
    while(i<2):    
        system.append(random.choice(cards))
        i+=1
    print(f"Your cards are {user}")
    print(f"the dealer's card is [{system[0]}] ")        
    part2()        

def part2():
    ch="y"
    total=0
    ch=input("do you want to draw another card 'y' or 'n' ")
    if ch=="y":
        while ch=="y":
            user.append(random.choice(cards))
            print(user)
            for i in user:
                total+=i
            print(total)
            if total>21:
                print("you loose")
                exit()
            elif total<21:
                a=len(user)
                print(a)   
                j=0
                while(j<a-2):
                    system.append(random.choice(cards))
                    print(system)
                    for i in system:
                        total+=i
                    if total>17:
                        j+=1
                    else:
                        part3()
            elif total==21:
                print("you win")
                exit()
        ch=input("do you want to draw another card 'y' or 'n' ")                        
    else:
            part3()


def part3():
    totalu=0
    totals=0
    for i in user:
        totalu+=i       
    for i in system:
        totals+=i
    if  totalu>totals:
        print("you win")
    elif totals>totalu:
        print("you loose")
    elif totalu==totals:
        print("it is a draw")

print('''                                                                                    
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                 
 ''')
part_1()
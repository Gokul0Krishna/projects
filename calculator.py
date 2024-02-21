
logo = """
             _____________________
            |  _________________  |
            | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
            | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
            |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
            | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
            | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
            | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
            | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
            | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
            | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
            | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
            | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
            |_____________________|
                                                                                                                        """

def addition(a,b):
    '''this function will add both the values'''
    return a+b

def subtraction(a,b):
    '''this function will subtract both the values'''
    return a- b

def multiplication(a,b):
    '''this function will multiply both the values'''
    return a*b

def division(a,b):
    '''this function will divide both the values'''
    return a/b


def calca():
        print(logo)
        a=float(input("enter the first no. : "))

        calc={}
        calc["+"]=addition
        calc["-"]=subtraction
        calc["*"]=multiplication
        calc["/"]=division

        for i in calc:
            print(i)
        ch="y"
        while ch=="y":
            op=input("what opperation do you want to perform:\n")
    
            b=float(input("enter the next no. : "))

            ans=calc.get(op)
            answ=ans(a,b)
            print(f"{a} {op} {b} = {answ}")
            a=round(answ,3)

            ch=input(f"Type 'y' to continue calculating with {answ}, or type n to exit:").lower()
            if ch=="n":
                return ch
            
            
cho=calca()
if cho=="n":
    res=input("to completely exit the program type 'y'else for a fresh start enter 'n'") 
    if res =="y":
        exit()
    if res=="n":    
        calca()
            

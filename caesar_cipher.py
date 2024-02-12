from pyfiglet import figlet_format
figlet_format("CAESER CIPHER", font = "standard" )

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#case=To store the input text in a list format.
#q=no. of letter is case
#w=variable to store the required elment from case
#change is used to store the position of the element of case in alphabet
#cript is the string to print at the end
def caesar(t,s,select):
    case=list(t)
    q=len(case)        
    for i in range(0,q):    
            w=case[i]
            for j in alphabet:    
                if(w==j):
                    og=alphabet.index(w)
                    change=og
                    if select=="1":
                        change+=s
                        if change>25:
                            change%=25
                            if change>=1:
                                og+=change
                    elif select=="2":
                        change-=s
                        if change<0:
                            change%=25
                            if change>=1:
                                og-=change
                    case[i]=alphabet[change]
                    cript="".join(case)
    print(cript)

print(figlet_format("CAESER CIPHER", font = "standard" ))
text = input("Type your message:\n").lower()
choice = input("Type '1' to encrypt, type '2' to decrypt:\n")
shift = int(input("Type the shift number:\n"))
caesar(t=text,s=shift,select=choice)
print("do you want to restart the cipher")
print("enter 'yes' to repeate and 'no' to exit")
g=input().lower()
while(g=="yes"):
    text = input("Type your message:\n").lower()
    choice = input("Type '1' to encrypt, type '2' to decrypt:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(t=text,s=shift,select=choice)
    print("do you want to restart the cipher")
    print("enter 'yes' to repeate and 'no' to exit")
    g=input().lower()
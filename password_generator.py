import random
print("this is a password generator");
print("how many letters would you like in your password ?");
l=int(input())
print("how many numbers would you like ?")
n=int(input())
print("how many symbols would you like ?");
s=int(input())

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

sin=[]
d=0
for i in range(l+1):
    d=(random.choice(letters))
    sin.append(d)

cos=[]
f=0
for i in range(n+1):
    f=(random.choice(numbers))
    cos.append(f)

tan=[]
g=0
for i in range(s+1):
    g=(random.choice(symbols))
    tan.append(g)

total=[]
total= sin+cos+tan
random.shuffle(total)
pasw="".join(total)
print(f"your password is:{pasw}")

number=int(input("enter your number:"))
factors=0
for i in range (1,number+1):
    if number%i==0:
        factors+=1
if factors==2:
    print("given number is a prime")
else:
    print("given number is not a prime")
n1 = int(input("Enter Number 1 : "))
n2 = int(input("Enter Number 2 : "))
n3 = int(input("Enter NUmber 3 : "))

if n1>n2 and n1>n3:
    print(f"Largest Number is : {n1}")
elif n2>n1 and n2>n3:
    print(f"Largest NUmber is : {n2}")
else :
    print(f"Largest Number is : {n3}")

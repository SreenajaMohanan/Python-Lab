a = int(input("Enter Starting Year : "))
b = int(input("Enter Ending Year : "))

if a > b:
    print("End year must be greater than or equal to start year")
else:
    print(f"Leap years from {a} to {b}")
    for year in range(a, b+1):
        if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(year)

number:int = int(input("Enter number: "))

if number % 2 == 0:
    print(f"Number is Even {number}")
    if number % 2 == 0 and number % 3 == 0:
        print(f"{number} is divisible by both 2 and 3")
    else:
        print(f"{number} is even but not divisible by both 2 and 3")    
else:
    print(f"Number is Odd {number}")    
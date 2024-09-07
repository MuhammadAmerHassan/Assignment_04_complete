age:int = int(input("Enter your age: "))
nationality:str = str.lower(input("Enter your nationality: "))
if age >= 18 and nationality == "pakistan":
    print("You are eligible to Vote        ")
else:
    print("""Sorry You are not eligible to vote
          To vote You have to meat folloeing both conditions
          1. 18 years old
          2. Nationality Pakistan""")
        
    

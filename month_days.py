month:int = int(input("Enter number of a month: "))

match month:
    case 1:
        print("january, 31 days")
    case 2:
        print("feb, 28 0r 29 days")
    case 3:
        print("March, 31 days") 
    case 4:
        print("April, 30 days") 
    case 5:
        print("May, 31 days") 
    case 6:
        print("June, 30 days")
    case 7:
        print("July, 31 days") 
    case 8:
        print("August, 31 days") 
    case 9:
        print("September, 30 days") 
    case 10:
        print("October, 31 days") 
    case 11:
        print("Novomber, 30 days")
    case 12:
        print("December, 31 days")  
    case _:
        print("Invalid Statement")           
def one():
    str1 = input("Enter a name: ")
    print("Hello ", str1)

def two():
    x =int( input("Enter a number : "))
    y = int(input("Enter a number :" ))
    print("Sum = ",x+y)

def three():
    C = eval(input("Enter a celsius temperature : "))
    print((9/5)*C + 32)

def four():
    principle = int(input("Enter the principle amount :"))
    rate = int(input("Enter the rate : "))
    time = int(input("Enter the time - \'years\'"))
    print("Simple Interest = ", (principle*rate*time)/100)
def five():
    seconds = int(input("Enter seconds : "))
    hours = seconds//3600
    seconds = seconds%3600
    minutes = seconds//60
    sec = seconds%60
    print("Hours: ",hours,"\nminutes: ",minutes,"\nseconds: ", sec)

def six():
    a = int(input("Enter a number :"))
    b = int(input("Enter a number: "))
    a,b = b,a
    print("a: ", a, "b: ", b)
    print("using extra var:")
    temp = a
    a = b
    b = temp
    print("we'll the input now! after re-swaping: \n a:", a," b: ", b)

if __name__ == '__main__':
    print("11-06-2024 - Python Training - Blue Yonder Assignment 2:")
    print("Assignments On Variable, Operator and Expression")
    print("\n1. A program that asks the user for his name and then welcomes him.")
    print("\n2. Prompts the user to enter two integers and display their sum on the screen")
    print("\n3. A program that prompts the user to input a Celsius temperature and outputs the equivalent temperature in Fahrenheit")
    print("\n4. Calculate simple interest ")
    print("\n5. Program should converts seconds in hours, minutes and seconds")
    print("\n6.  prompts the user to enter number in two variables and swap the contents of the variables")
    print("\n7. Exit")
    n = int(input("\n  Enter a choice: "))
    while n >= 7:
        if n == 1 : one()
        elif n==2 : two()
        elif n==3 : three()
        elif n==4 : four()
        elif n==5 : five()
        elif n==6 : six()
        n = int(input("\n  Enter a choice: "))

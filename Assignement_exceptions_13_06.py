def one():
    try:
        f = open('example.txt', 'r')
    except Exception as e:
        print("File doesnot Exists - ",e)
    else:
        print("file exists")

def two():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
    except Exception as e:
        print("Error occured- ", e)
    else:
        print(f"a= {a}, b={b}")
    finally:
        print("Yay! You made it!")

def three():
    try:
        val = [1,2,3,4]
        print(val[8])
    except Exception as e:
        print(e)

def four():
    try:
        val = [1,2,3]
        val.add(4)
    except Exception as e:
        print("error occured - ", e)

class FormulaError(Exception):
    def __init__(self, argv):
        self.argv =  argv

def five():
    exp = input("Enter an expression or enter \'quit\' to exit : ")
    while(exp != 'quit'):
        exp = exp.split()
        try:
            if len(exp)!=3 or (exp [1] not in [ '+', '-']):
                raise FormulaError("Expression given is wrong. Please try again!")
            exp[0] = float(exp[0])
            exp[2] = float(exp[2])
            if exp[1] == '+':
                print(exp[0] + exp[2])
            else:
                print(exp[0] - exp[2])

        except FormulaError as fe:
            print(fe)
        except ValueError as ve:
            print("Value Error: ", ve)
        exp = input("Enter an expression or enter \'quit\' to exit : ")
        
def six():
    try:
        values = [int(x) for x in input("Enter comma separated numbers: ").split(",")]
    except ValueError as ve:
        print(ve)
    else:
        print(values)

def seven():
    try:
        a = 1
        b = 2
        print(f"a = {a}, b= {b}")
        return f"result = {a+b}"
    except:
        print("Exception")
    finally:
        # return f"result = {a+b} from finally block"
        print(a+b)

def eight():
    f = open('story.txt', 'r')
    print(f" 1. the cursor is at - {f.tell()}")
    chars = f.read(12)
    print(f" 2. the cursor is at - {f.tell()}")
    f.seek(2)
    print(f" 3. the cursor is at - {f.tell()}")
    f.close()


if __name__ == '__main__':
    print("12-06-2024 - Python Training - Blue Yonder Assignment 2:")
    print("Assignments On Files")
    print("\n1. FileNotFoundException case")
    print("\n2. TypeError case ")
    print("\n3. IndexError case")
    print('\n4. AtrributeError case')
    print("\n5. Calculator - custom Exception")
    print("\n6. ValueError - list case")
    print("\n7. Investigate when there is return statement in both try and finally blocks")
    print("\n8. Investigate seek and tell functions ")
    print("\n9. Exit")
    n = int(input("\n  Enter a choice: "))
    while n != 9:
        if n == 1 : one()
        elif n==2 : two()
        elif n==3 : three()
        elif n==4 : four()
        elif n==5 : five()
        elif n==6 : six()
        elif n==7 : print(seven())
        elif n==8: eight()
        n = int(input("\n  Enter a choice: "))
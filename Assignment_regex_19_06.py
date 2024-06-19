import re
def one():
    mail_pattern = r"[a-zA-z0-9.]+\@[a-zA-Z]+.[a-z]+"
    email = input("Enter your email id: ")
    x = re.fullmatch(mail_pattern, email, re.IGNORECASE)
    if x!= None:
        print("Correct - ", x)
    else:
        print("Wrong email")

def two():
    password = '([a-z]+|[A-Z]+|[0-9]+)+'
    pas = input("enter password: ")
    t = re.match(password, pas)
    if t!= None:
        print(f"Correct- {pas}")
    else:
        print("Incorrect password")

def three():
    pattern = '^[a-zA-Z0-9]+'
    st = input("Enter a string: ")
    check = re.fullmatch(pattern, st)
    if check != None:
        print(f"Correct string - {st}")
    else:
        print("Wrong format")

def four():
    pattern = 'a(0|b*)'
    s = input("Enter a string : ")
    check = re.fullmatch(pattern, s)
    if check:
        print(f"correct - {check}")
    else:
        print("Wrong")

def five():
    pattern = '[a-z]+_'
    s = input("Enter a string : ")
    check = re.finditer(pattern, s)
    count = 0
    if check != None:
        for i in list(check):
            count += 1
            print(i)
    if count == 0:
        print("Wrong")

def six():
    pattern = '[A-Z][a-z]+'
    s = input("Enter a string : ")
    check = re.fullmatch(pattern, s)
    if check:
            print("correct -", check)
    else:
        print("wrong")

def seven():
    pattern = '^[a-zA-Z0-9_]+'
    st = input("Enter a string: ")
    check = re.fullmatch(pattern, st)
    if check != None:
        print(f"Correct string - {st}")
    else:
        print("Wrong format")
    
def eight():
    string =  input("Enter a string: ")
    string = re.split('\(.*\)', string)
    print("".join(string))

if __name__ == '__main__':
    print("19-06-2024 - Python Training - Blue Yonder Assignment :")
    print("Assignments On regex")
    print("\n1. Validate Email id")
    print("\n2. Validate password ")
    print("\n3. String has only alphanumeric chars")
    print('\n4. a followed by 0 or more b\'s')
    print("\n5. lowercase and underscore")
    print("\n6. 1 Uppercase followed by lowercase")
    print("\n7. Uppercase, lowercase, numbers and underscore")
    print("\n8. remove Parenthesis from a string")
    print("\n9. Exit")
    n = int(input("\n  Enter a choice: "))
    while n != 9:
        if n == 1 : one()
        elif n==2 : two()
        elif n==3 : three()
        elif n==4 : four()
        elif n==5 : five()
        elif n==6 : six()
        elif n==7 : seven()
        elif n==8: eight()
        n = int(input("\n  Enter a choice: "))
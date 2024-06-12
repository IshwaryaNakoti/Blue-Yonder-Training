def one():
    values  = [int(x) for x in input("Enter number - spcae separated: ").split()]
    print("Alternate elements are:\n")
    for i in range(0,len(values), 2):
        print(values[i])

def two():
    values = [x for x in input("Enter values: ").split()]
    print(values[::-1])

def three():
    values = [int(x) for x in input("Enter values: ").split()]
    max_num = 0
    for i in values:
        if i > max_num:
            max_num = i
    print(max_num)

def perform_rotation(values):
    new_list = values[len(values)-1: ] + values[0: len(values)-1]
    return new_list

def four():
    n = int(input("How many elements you want to enter? : "))
    values = []
    for i in range(n):
        values.append(input("Enter element: "))
    step = int(input("Enter the step (rotation step) : "))
    for i in range(step):
        after_rotation = perform_rotation(values)
        values = after_rotation
    print(after_rotation)

def five():
    str1 = input("Enter a string:")
    str2 = input("Enter a string: ")
    list_str1 = str1.split()
    for i in list_str1:
        if i ==str2:
            list_str1.remove(i)
    new_str = " ".join(list_str1)
    print(new_str)

def six():
    date = input("Enter date in mm/dd/yyyy format: ")
    date = [int(x) for x in date.split('/')]
    months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
    ]
    print(months[date[0]-1], date[1], ", ",date[2])

def seven():
    str1 = input("Enter a string: ")
    str1 = str1.split()
    str1_lenth = set([len(x) for x in str1])
    d = {}
    for i in str1_lenth:
        d[i] = 0
    for i in str1:
        d[len(i)] += 1
    print(d)

def eight():
    vals = [int(x) for x in input("Enter a digit: ").split()]
    d = {"EVEN" : [], "ODD": []}
    for i in vals:
        if i %2 ==0:
            d["EVEN"].append(i)
        else:
            d["ODD"].append(i)
    print(d)

if __name__ == '__main__':
    print("11-06-2024 - Python Training - Blue Yonder Assignment 2:")
    print("Assignments On Lists")
    print("\n1. A program that accepts a list from user and print the alternate element of list.")
    print("\n2. A program that accepts a list from user. Your program should reverse the content of list and display it. Do not use reverse() method.")
    print("\n3. Find and display the largest number of a list without using built-in function max()")
    print("\n4. Write a program that rotates the element of a list ")
    print("\n5. A program that input a string and ask user to delete a given word from a string")
    print("\n6. A program that reads a string from the user containing a date in the form mm/dd/yyyy")
    print("\n7. Write a program that reads string from user. Your program should create a dictionary having key as word length and value is count of words of that length.")
    print("\n8. Write a program to read 6 numbers and create a dictionary having keys EVEN and ODD")
    print("\n9. Exit")
    n = int(input("\n  Enter a choice: "))
    while n != 9:
        if n == 1 : one()
        elif n==2 : two()
        elif n==3 : three()
        elif n==4 : four()
        elif n==5 : five()
        elif n==6 : six()
        elif n==7: seven()
        elif n==8: eight()
        n = int(input("\n  Enter a choice: "))
def one():
    n = input("Enter a string: - 1st question: ")
    return (n[::-1])

def two():
    n = input("Enter a string: - 2nd question: ")
    even_pos = ""
    odd_pos = ""
    for i in range(len(n)):
        if i%2 == 0:
            even_pos += n[i]
        else:
            odd_pos += n[i]
    print("Even position : ",even_pos)
    print("Odd position: ", odd_pos)

def three():
    str1 = "ravi"
    str2 = "teja"
    new_str = ""
    if len(str1) > len(str2):
        for i in range(len(str2)):
            new_str += str1[i]
            new_str += str2[i]
        new_str += str1[len(str2):]
    else:
        for i in range(len(str1)):
            new_str += str1[i]
            new_str += str2[i]
        new_str += str2[len(str2):]
    print(new_str)

def four():
    str3 = input("Enter a string - 4th question:")
    new_str = ""
    num_str = ""
    for i in sorted(str3):
        if i.isdigit():
            num_str += i 
        else:
            new_str += i
    print(new_str+num_str)

def five():
    str5 = input("enter a string - 5th question")
    set_str = set(list(str5))
    newstrd= ""
    for i in sorted(list(set_str)):
        newstrd+= i
    print(newstrd)

def six():
    str6 = input("Enter a string - 6th question : ")
    all_chars = sorted(set((str6)))
    occurence ={}
    for i in all_chars:
        occurence[i] = 0
    for i in str6:
        occurence[i] +=1
    print(occurence)

def seven():
    str7 = input("Enter a string - 7th question: ")
    vowels_present = ""
    vowel_count = 0
    for i in str7:
        if i in ['a', 'e', 'i', 'o','u'] and i not in vowels_present:
            vowel_count +=1
            vowels_present += i +' '
        else:
            continue
    print(vowels_present, " => ", vowel_count )

if __name__ == '__main__':
    print("11-06-2024 - Python Training - Blue Yonder Assignment 1:")
    print("\n1. Reverse a string")
    print("\n2. Print even and odd position of a string")
    print("\n3. Print alternative chars of 2 strings")
    print("\n4. Sort the fchars and pritn first Alphabets later numeric chars")
    print("\n5. Remove duplicates from a string")
    print("\n6. Find the no. of occurence of each char in string")
    print("\n7. Display and count unique vowels present in the given word")
    print("\n8. Exit")
    n = int(input("\n  Enter a choice: "))
    while n != 8:
        if n == 1 : print(one())
        elif n==2 : two()
        elif n==3 : three()
        elif n==4 : four()
        elif n==5 : five()
        elif n==6 : six()
        elif n==7 : seven()
        n = int(input("\n  Enter a choice: "))

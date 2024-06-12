def one():
    f = open('poem.txt', 'r')
    for i in f.readlines():
        print(i)
    f.close()

def two():
    f = open('story.txt', 'w+')
    f.write('''A boy is playing there.
There is a playground.
An aeroplane is in the  sky.
The sky is blue
Aplhabets and number are allowed.''')
    f.seek(0)
    count=0
    contents = f.readlines()
    print(contents)
    for i in contents:
        if i[0] != 'T':
            count+=1
    print("Number of sentences starting without alphabet \'T\':",count)
    f.close()

def three():
    f = open("notes.txt", 'w+')
    f.write('''India is the fastest growing economy India is looking for more investments around the globe the whole world is looking at India as greatest market most of the Indians can for see the height that India is capable
            ''')
    f.seek(0)
    count =0
    for i in f.readlines():
        list = i.split()
        for j in list :
            if j == 'the':
                count=count+1
    f.close()
    print(count)

def four():
    f = open('story.txt', 'r')
    ans =[]
    f.seek(0)
    print(f.read())
    f.seek(0)
    for i in f.readlines():
        print(i)
        l = i.split()
        for j in l:
            print(j)
            if len(j) < 4:
                ans.append(j)
    print(ans)

def five():
    f = open('notes.txt', 'r')
    f.seek(0)
    count =0
    for i in f.readlines():
        for j in i.split():
            if j[len(j)-1].isdigit():
                count +=1
    print(count)

if __name__ == '__main__':
    print("12-06-2024 - Python Training - Blue Yonder Assignment 2:")
    print("Assignments On Files")
    print("\n1. Read file contenst line by line")
    print("\n2. Check how many lines start with\'T\' ")
    print("\n3. Count the occurence of a word")
    print('\n4. Print the words from the file where len(word)<4')
    print("\n5. Print the number of words ending with a digit in a file")
    print("\n6. Exit")
    n = int(input("\n  Enter a choice: "))
    while n != 6:
        if n == 1 : one()
        elif n==2 : two()
        elif n==3: three()
        elif n==4: four()
        elif n==5: five()
        n = int(input("\n  Enter a choice: "))
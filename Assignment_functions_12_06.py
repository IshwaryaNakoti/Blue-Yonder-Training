def one():
    str1 = input("Enter a word: ")
    vowels = 0
    consonents = 0
    for i in str1:
        if i in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
        else:
            consonents += 1
    print("Vowels = ", vowels, "\nConsonents = ", consonents)

def two():
    str1 = input("Enter a string: ")
    print(str1.upper())

def three():
    n = int(input("Enter a number: "))
    for i in range(1,11):
        print(n," * ", i, " = ", n*i)

def is_prime(n):
    for i in range(2,n):
        if n%i ==0:
            return False
    return True
def four():
    end = int(input("Enter a number :"))
    for i in range(2, end):
        j = i + 2
        if (is_prime(i) and is_prime(j)):
            print(f'({i}, {j} ) are twin primes')

def five():
    num = int(input("Enter a number: "))
    all_prime_factors = []
    for i in range(2, num):
        if num%i == 0 and is_prime(i):
            all_prime_factors.append(i)
    for i in all_prime_factors:
        print(i, end=" ")

def six():
    dec = int(input("Enter a decimal number: "))
    print(bin(dec))

if __name__ == '__main__':
    print("12-06-2024 - Python Training - Blue Yonder Assignment 2:")
    print("Assignments On functions")
    print("\n1. count vowels and consonents in a word")
    print("\n2. String lower to upper ")
    print("\n3. multiplication table of a number")
    print('\n4. print twin primes less than 1000')
    print("\n5. Print prime factors of a number")
    print("\n6. Decimal to binary")
    print("\n7. Exit")
    n = int(input("\n  Enter a choice: "))
    while n != 7:
        if n == 1 : one()
        elif n==2 : two()
        elif n==3: three()
        elif n==4: four()
        elif n==5: five()
        elif n==6: six()
        n = int(input("\n  Enter a choice: "))
# HELLO WORLD
print('Hello World')

print("\n")
#------------------------------------------------------------------
# ADDITION
x = 10
y = 20
z = x + y
print(z)

print("\n")
#-------------------------------------------------------------------
# GREATER THAN 2
if x>y:
    print(x, 'is greater.')
else:
    print(y, 'is greater.')

print("\n")
#--------------------------------------------------------------------
# AREA OF RECTANGLE
l = 5
b = 7
Area = l*b
print('Area of rectangle', Area)

print("\n")
#--------------------------------------------------------------------
# SQUARE OF A NUMBER
Num = 6
Square = Num*Num
S = Num**2
print('The square is', Square)
print('The square is', S)

print("\n")
#--------------------------------------------------------------------
# SIMPLE INTEREST
P = 10000
R = 15
T = 7
SI = (P*R*T)/100
print('The Simple Interest is: ', SI)

print("\n")
#-------------------------------------------------------------------
# TYPE OF VARIABLE
s = 3.14
print(type(P))
print(type(s))

print("\n")
#-------------------------------------------------------------------
# SWAP VARIABLES
a = 'Swap'
b = 'Variables'
c = a
a = b
b = c
print(a,b)

a,b = b,a
print(a,b)

print("\n")
#-------------------------------------------------------------------
# CELCIUS TO FARENHEIT
C = 19
F = C*(9/5) + 32
print(F)

print("\n")
#-------------------------------------------------------------------
# CONCATENATE STRING
j = 'Saachi '
k = 'Parmar'
l = (j + k)
print(l)

print("\n")
#-------------------------------------------------------------------
# SPLIT SENTENCE
f = 'I want to sleep'
words = f.split()
print(words)

print("\n")
#-------------------------------------------------------------------
# FIND PRIME NUMBERS IN A RANGE
# CODE 1
s_num = 1
l_num = 56
for num in range(s_num, l_num+1):
    if num > 1:
        for i in range(2,int (num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num , end=" ")

# CODE 2
s_num = 1
l_num = 19
primes = []
for num in range(s_num, l_num+1):
    if num > 1:  
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:  
            primes.append(num)

print("\nPrime numbers are: ", primes)

print("\n")
#--------------------------------------------------------------------
# PATTERN
g = '*'
for i in range(7):
    print(g*i)

h = 7
for i in range(h, 0, -1):
    print('*'*i)

print("\n")
#----------------------------------------------------------------------
# ARMSTRONG NUMBER - This is for 3 Digits
num = int(input('\nEnter a number: '))
sum = 0
temporary = num
while temporary > 0:
    digit = temporary % 10
    sum = sum+digit ** 3
    # sum += digit ** 3
    temporary //= 10
if num == sum:
    print(num, 'is Armstrong')
else:
    print(num, 'not Armstrong')
    
num = int(input('\nEnter a number: '))
sum = 0
temporary = num
while temporary > 0:
    digit = temporary % 10
    sum = sum+digit ** 3
    # sum += digit ** 3
    temporary //= 10
if num == sum:
    print(num, 'is Armstrong')
else:
    print(num, 'not Armstrong')
    
print("\n")

# For max 4 digits, maybe
x=input("\nEnter Number: ")
y=int(x)
l=len(x)
#a=int(x[2])+3
#print(a)
s=0
for i in range(l):
    a=int(x[i])
    s+=a**l

if s==y:
    print("Is Amstrong")

else:
    print("Not Amstrong")

print("\n")
#--------------------------------------------------------------------
# FACTORIAL
num = int(input("\nEnter the number: "))
fact = 1
for i in range(1, num+1):
    fact = fact*i
print("The factorial of", num, "is", fact)    

print("\n")
#---------------------------------------------------------------------
# FIBONACCI
n = 19
a,b = 0,1
print('\n', b, end=" ")                # end=" " is for horizontal display
for i in range(2,n):
    a, b = b, a+b
    print(b, end=" ",)

print("\n")
#---------------------------------------------------------------------
# PALINDROME
x = input('\n\nEnter the number: ')
if x==x[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

print("\n")
#----------------------------------------------------------------------
# REVERSE A NUMBER
x = int(input("\nEnter a number: "))
y = 0
while x>0:
    y = y * 10 + x % 10
    x //=10
print(y, end='  ')

print("\n")
# with space
x = int(input("\nEnter a number: "))
y = 0
while x>0:
    y = y * 10 + x % 10
    x //=10
print(" ".join(str(y)))

print("\n")
#-----------------------------------------------------------------------
# GCD - Greatest Common Divisor
a, b = 56, 98
while b:
    a,b = b, a%b
print("\nGCD is: ", a)

print("\n")
#-----------------------------------------------------------------------
# PASCAL TRIANGLE
# CODE 1
n = 7
for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end=' ')
    C = 1
    for j in range(1, i+1):
        print(' ', C, sep=' ', end=' ')

        C = C * (i - j) // j
    print()

print("\n")    
# CODE 2
n=5
for i in range(n):
    row = [1]
    if i>0:
        for j in range(1, i):
            row.append(prev[j - 1] + prev[j])
        row.append(1)
    print(row)
    prev = row
    
print("\n")
# CODE 3
n=5
for i in range(n):
    row = [1]
    if i>0:
        for j in range(1, i):
            row.append(prev[j -i -1] + prev[j])
        row.append(1)
    print(row)
    prev = row
    
print("\n")
#-----------------------------------------------------------------------
# DIAMOND
n = 8
for i in range(4,n):
    print(' '*(n-i-1)+ '*' *(2*i+1))
for i in range(n-2, -1, -1):
    print(' '*(n-i-1)+ '*' *(2*i+1))

print("\n")
#-----------------------------------------------------------------------
# EVEN ODD
num = int(input('\nEnter a number: '))
if num%2==0:
    print('It is even.\n')
else:
    print('It is odd.\n')

print("\n")
#-----------------------------------------------------------------------
# DISPLAY ALL SUBSETS IN A SET
# CODE 1
s1 = {'a','b','c','d','e'}
s2 = {'q','w','r','t','y'}
s3 = s1.union(s2)
print(s3)

print("\n")
# CODE 2
nums = [1,2,3]
subset = [[]]
for num in nums:
    subset += [curr +[num] for curr in subset]
print("Subsets: ", subset)
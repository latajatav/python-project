# Function definition is here
#def printinfo(arg):
#"This prints a passed info into this function"
   #print ("Name: ", name)
   #print ("Age ", age)
   #return;

# Now you can call printinfo function#printinfo( age=50, name="miki" )
#printinfo( name="lata" )
#Name = "lata"
#Class = "B.E"

#average function
#def findavg(first,second):
        #result = (first+second)/2
        #return result

#first = int(first)
#second = int(second)
#avg = findavg(first,second)
#print('The average of %d and %d is %.2f '%(first,second,avg))

#def greater(a,b):
#    if a>b:
#        return a
#    else:
#        return b

#a = input('Enter fisrt no.:' )
#b = input('Enter second no.:')
#a,b = int(a),int(b)
#great = greater(a,b)
#print("Greater no. is %d" %great)

#a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#for ele in a:
    #print(ele)

#for i in range(0,len(a)):
#    print(a[i])

#i = 100
#while i<201:
#    print(i)
#    i = i+10

#print("""1
#2
#3
#4
#5
#6""")

#i = 0
#    a[i] = a[i]
#    i = i+1
#    print(a[i])

#for i in range (1,101):
#    print(i)

#Counting lenght of digit in a number
#A = input("Enter a number")
#print(len(A))


#Write a program to find sum of all  numbers in the list

#total = 0
#a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#for i in range(0, len(a)):
#    total = total + a[i]
#    print(total)

#a = range(11)
# [0,1,2,3,4,5,6,7,8,9]
#b = sum(a)
#print(b)
# Prints 45



#write a program for calculating factorial of any number
#b = 1
#a = input("Enter a number")
#a = int(a)
#while(a>0):
#    b = b*(a-1)
#print(b)


#n=int(input("Enter number:"))
#fact=1
#while(n>0):
#    fact=fact*n
#    n=n-1
#print("Factorial of the number is: ")
#print(fact)


# Question number.1 program for adding element in list
#a = [1, 2, 3, 4, 5, 6]
#sum = 0
#for ele in a:
#    sum = sum + ele
#print(sum)


# Question number.2 program for Factorial
#a = input("Enter a number:")
#a = int(a)
#fact = 1
#for i in range(1,a+1):
#    fact = fact*i
#    i = i+1
#print(fact)

#   Question number.3 program for print even number in a list
#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#for i in range(0,len(a)):
#    if a[i]%2 == 0:
#        print(a[i])
#    else:
#        i = i+1

#   Question number.4 program for print all even numbers
#i = 0
#while(i<100):
#    i = i + 2
#    print(i)

#Write a program for print all even number between 1-100 using for loop:
#for i in range(1,100):
    #if
        #print(i)
    #else:
        #i = i+1

#lst=[]
#num=int(input('How many numbers: '))
#for n in range(num):
    #numbers=int(input('enter number '))
    #lst.append(numbers)
#print("sum of element in given list is :",sum(lst))


#num=input("enter a number to find is factorial ")
#num=int(num)
#fact=1
#for i in range(1,num+1):
    #fact=fact*i
    #i=i+1
#print(fact)


#a=[10,20,30,5,1,7]
#for i in range(0,len(a)):
    #if a[i]%2==0:
        #print(a[i])
    #else:
        #i=i+1


#for x in range(0,100):
    #if x%2==1:  #odd number
        #print(x)
    #x=x+1


#for x in range(0,100):
    #if x%2==0:  #even number
        #print(x)
    #x=x+1


#n=int(input("enter a number: "))
#sum1 = 0
#while(n > 0):
    #sum1=sum1+n
    #n=n-1
#print("the sum of first n natural numbers is",sum1)


#sum=0
#for ele in a:
    #sum = sum+ele


#a=[10,20,30]       #append method
#a.append(40)
#print(a)


#a=[10,20,30]
#a.insert(2,"india")
#print(a)


#b=[1,2,3,4]
#b.insert(0,8)
#print(b)


#def add(a,b):
        #return a+b
#x = input("Enter 1st number ")
#y = input("Enter 2nd number ")
#z = (add(int(x),int(y)))
#print("Add two number is " + str(z) )


#def sub(a,b):
        #return a-b
#x = input("Enter 1st number ")
#y = input("Enter 2nd number ")
#z = (sub(int(x),int(y)))
#print("sub two number is " + str(z) )


#def mul(a,b):
#        return a*b
#x = input("Enter 1st number ")
#y = input("Enter 2nd number ")
#z = (mul(int(x),int(y)))
#print("mul two number is " + str(z) )


#def square(a):
#        return a*a
#x = input("Enter a number ")
#y= (square(int(x)))
#print("square of number is " + str(y))


#def strings(a,b):
#        return a + b
#print(strings("lata ","jatav"))



#print("""1
#2
#3
#4
#5
#6""")


def fact(n):
    res = 1
    for i in range(1,n+1):
             res = res*i
    return res

n = int(input('enter a number to find in factorial:'))
r = fact(n)
print(r)

'''
import os
if (not os.path.exists("programming")):
 os.mkdir('programming')
 
for i in range(1,11):
   # os.mkdir(f"programming/day{i} ")
    os.rename(f"programming/day{i} " , f"programming/day-{i}")
'''
'''
with open('programming/plan.txt' ,'w') as f :
    f.write("rahul is very smart and hero")

with open('programming/plan.txt' , 'a') as f :
    f.write(" and he is future ai ml engineer ...")

with open('programming/plan.txt' , 'r') as f:
    f.seek(4)
    print(f.tell())
    print(f.read())

with open('programming/plan.txt' , 'w' ) as f:
    f.write("great hero \n best hero \nlovely man ")

# writeline() function
with open('programming/plan.txt' , 'w') as f:
    line =['rahul\n' ,'shivini\n' , 'ritika\n','anika\n']
    f.writelines(line)

#readline method
with open('programming/plan.txt','r') as f:
    while True:
     line = f.readline()
     if not line:
         break
     print(line)
'''
#factorial of number
'''
def fac(n):
 fact = 1
 for i in range(1,n+1):
    fact = fact * i
 print(fact)

n = int(input('enter a number : '))
fac(n)
'''
#fibonacci function 
#by loop 
'''
n=int(input('enter a number of term :'))
a,b= 0,1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c
'''
#by recursion 
'''
def fibo(n):
    if n <=1:
        return n
    else:
        return fibo(n-1) +fibo(n-2)

n=int(input('enter a number of term :'))
for i in range(n):
    print(fibo(i))'''

# binary search'''.................
'''

n=int(input('enter number of element in your list : '))
lst =[]
for i in range(1,n+1):
    val = int(input(f'enter {i} element of your array : '))
    lst.append(val)
lst = sorted(lst)
print(lst)
start =0
end =n-1
target = int(input('enter a element which you want to search in a list : '))

while start <=end:
    mid = (start+end)//2
    if lst[mid] == target:
        print(f'the target element is {target} in {mid} index')
        break
    elif lst[mid] <target:
        start =mid+1
    else:
        end= mid-1

'''

#error handling in python .....................................................
'''
def error(): 

    try :
      num = int(input('enter a number for table from 1 to 100 :'))
      if num <100 and num>=0:
        for i in range(1,11):
         print(f" {num} * {i} = {num*i}")
        return
      else:
         raise print(ValueError('number is not in a given range '))
         
       
    except Exception as e  :
        print('ERROR ->',e)
        return
#finally keyword is used to make a line always executable 
    finally:
     print('program executed sucessfully') 
error()

'''
#shorthand if else
'''
a= int(input('enter 1 number ')) 
b= int(input('enter 2 number ')) 
print(a,'is greater than ',b) if a>b else print(a ,"is equal to",b) if a==b else print(b,'is greater than ',a)'''

#for importing user define function from one file to another file 
#recape.py is a file in which a quicksort function is return and we use it from main.py file  
'''
from  recape import quick_sort as q
lst = [6,5,4,3,2,1]
print(q(lst))
'''
'''
import json 
with open('r.json','w') as f:
    sentence = 'hello rahul sir good morning'
    json.dump(sentence ,f)
    #s=json.load(f)
    #print(s)'''


#python completed sucessfully ............................................. |:-)|


#adiing some recursion stuff 
# inheritance in python single inheritance 
'''
class employee :
    def __init__(self,name,id):
        self.name =name
        self.id =id

    def info(self):
        print(f'employee name is {self.name} and its id is {self.id}')

#class programmer inherite class employee 

class programmer(employee):
    def pro(self,lan):
        self.lan = lan
        print(lan)
a=employee('rahul',1)
a.info()

b=employee('shiv',2)
b.info()

b=programmer('raaj',3)
b.pro('python')
b.info()
'''
# acces modifiers>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#public-> attribute name 
#private-> __attribute name 
#protected-> _atribute name 

'''
class emp:
    def __init__(self):
        self.name ='rahul'
        self._name ='raj'
        self.__name ='ritika'

class std(emp):
    None

a=emp()
print(a.name )
print(a._emp__name )
print(a._name )

b=std()
print(b.name)
print(b._emp__name )'''
'''
#4Write a recursive function to calculate the $N$-th Factorial of  number.
#imp................................................................................
def fact(n):
    if n <=1:
        return n
    else:
        return n* fact(n-1)
    
n =int(input('enter a number for factorial : '))
print(fact(n))

# recursive function for fibonacci series 

def fibo(num):
    if num<=1:
        return num
    else:
        return fibo(num-1) + fibo(num-2)
    
num =int(input('enter the number of terms : '))
for i in range(num):
 print(fibo(i))
'''
# stone paper sessior game ---------------------------------------------------------------------------------------'''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
logic understanding matrix using permutation and combination 
        comp
         st  pa  sc
me    st d   l   w
      pa w   d   l
      sc l   w  d

       ''' 
'''
import random
def chk(choice):
    if(compchoice ==2 and choice ==1):
        return -1
    elif(compchoice ==3 and choice ==2):
        return -1
    elif(compchoice ==1 and choice ==1):
        return -1
    elif(compchoice == choice):
        return 0
    elif choice >3 or choice==0:
       return 10
    else:
        return 1

    
choice=int(input('enter 1 for stone ,2 for papper ,3 for scessor :'))
compchoice = random.randint(1,3)
print(f'your choice : {choice}')
print("computer choice : ",compchoice)

if chk(choice) == 1 :
    print(f'you win your choice is {choice} and computer choice is {compchoice}')
elif chk(choice) == 0:
     print(f'match draw your choice is {choice} and computer choice is {compchoice}')
elif chk(choice) == -1:
     print(f'you lose your choice is {choice} and computer choice is {compchoice}')
elif chk(choice) == 10:
    print(f'your choice : {choice} is invalid !!!!!')

'''
# static method i..............................................in oops.
'''
class calculate:
    def __init__(self,n):
        self.name  =n


    def sum(self,a,b):
            return a+b
    @staticmethod
    def mul(a,b):
            return a*b
a=calculate('RAHUL')
print(a.name)
print(a.sum(1,8))
print(a.mul(9,9))
print(calculate.mul(8,2))'''

# instance variable and class variable ---------------------------------------------->>>>>>>>>>>>>>>>>>>>>
'''
class employee:
    bonus = 50000
    def __init__(self,name,salary,com):
        self.name = name
        self.salary = salary
        self.com = com
    def info(self):
            print(f'employee name is {self.name} with {self.salary} salary with creatited bonus is {self.bonus} in {self.com}')

e1=employee('Rahul',250000 ,'google')
e1.bonus = 100000
e1.info()
employee.bonus = 100

print(employee.bonus)
e2 =employee('ritika',50000,'tcs')
e2.bonus = 30000
e2.info()
'''
#2Find the sum of all elements in a list using recursion.
#3Reverse a string using recursion.
'''def revv(s):
    if len(s) == 0 or len(s) ==1:
        return s
    else:
        return s[-1] + revv(s[:-1])
s= input('enter a string :')
print(revv(s))

#recursive function for sum of n natural number 
def sumn(n):
    if n==0:
        return n
    else:
        return n +sumn(n-1)
n = int(input('enter a number :'))
print(sumn(n))
'''
#power using recursion 
'''
def poww(n,p):
    if p==1:
        return n
    else:
        return n *poww(n,p-1)
n=int(input('enter a number : '))
p=int(input('enter a power:'))
print(poww(n,p))
'''
#check pallindrome 
'''
def chkpallin(s):
    if len(s) ==1 or len(s)==0:
        print('pallindrome ')
        return 
    if s[0] != s[-1]:
        print('not pallindrome')
        return
    else:
        return chkpallin(s[1:-1]) 
s=input('enter a string :')
chkpallin(s)
'''
#GCD greatest comman divisor  bby recursive function eculid is algorithm logic (a,b=b,a%b return a when b=0)>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''

def gcd(a,b):
    if b==0:
        return a
    else :
        return gcd(b,a%b)
a=int(input('enter a :'))
b=int(input('enter b :'))
print(gcd(a,b))
'''
# Find the sum of all elements in a list using recursion.
#imp'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
def add(lst):
    if len(lst) ==0 :
        return 0
    return lst[0] + add(lst[1:])
lst= [1,2,3,4,5,6,7]
print(add(lst))

print(lst[1:-1])
print(lst[1:])
'''
#Implement linear search on a list using recursion.
'''
def linear(lst,target,index =0):
    if index == len(lst):
        return False
    if lst[index] == target:
        return True
    else:
        return linear(lst,target,index+1)
lst =[1,2,3,4,5,4,5,6,4,78,52,99]
target =88
index=0
print(linear(lst,target,index))
    
'''
# tower of hanio very important recursive problem ...............................................................................................
def toh(n,scr,helper,destination):
    if n==1:
        print(f'from {scr} to {destination}')
        return

    toh(n-1,scr,destination,helper)
    print(f'from  {scr} to {destination}')

    toh(n-1,helper,scr,destination)
toh(3,'source','helper','destination')

a=(1,2,3)
b=(1,2,3)
print(a==b)
print(a is b)
a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is b)
print(type(a))



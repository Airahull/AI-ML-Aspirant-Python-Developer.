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

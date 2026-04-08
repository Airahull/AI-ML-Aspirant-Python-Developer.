
#1 dir(),__dict__() , help()..................................................................>>>>>>>>>
#dir()
'''lst =[]
print(dir(str))

#__dict__ attribute
class emp:
    def __init__(self,name,id,salary):
        self.name =name
        self.id = id
        self.salary =salary

emp1 = emp('Rahul' , 23 , 250000)
print(emp1.name)
print(emp1.id)
print(emp1.salary)
print(emp1.__dict__)

#it return dictonary of class attributes 
#help() method 
print(help(list))'''

# super method in inheritance ''''''''''''''''''''''''''''''
'''
class parent:
    def prntmeth(self):
        print('parent method invoke from parent class ')
class child(parent):
    def prntmeth(self):
        print('parent method of child class ')
        super().prntmeth()
    def childmethod(self):
        print('child method from child class ')
chl = child()
pr =parent()
print(chl.childmethod())
print(pr.prntmeth())
print(chl.prntmeth())'''
#super() method acces same name meethods from parent and child class by instance of child class ...

#Given a string, count the frequency of each character and store it in a dictionary.
'''
from collections import Counter
dic ={}
text = 'python programming'
text2=text.replace(" ","").lower()
print(dict(Counter(text2)))
print(Counter(text))
print(type(text2))

#Given two lists, find all the common elements between them.
lst1=[1,2,34,4,5,6,7]
lst2=[2,4,5,0,9,8,34]
lst1=set(lst1)
lst2=set(lst2)
print(lst1)
print(lst2)
print(list(lst1.intersection(lst2)))
lst3=[ num for num in set(lst1)&set(lst2)]

#Iterate through a dictionary and print only the keys whose values are greater than $10$.
marks={'english' :87,'maths' : 99 , 'science' : 92,'gk':88,'sst' :90}
newmarks={ }
for subject,mark in marks.items():
    if mark >90:
        print(subject)'''

#Given a list with duplicates, return a new list containing only the unique elements in the order of their first appearance.
# by for loop by membership operator it takes alot of time 
'''
lst1=[1,4,2,3,2,21,3,4,4,2,4,42,1,10]
nl=[]
for num in lst1:
    if num not in nl:
        nl.append(num)
print(lst1)
print(nl)'''
#by set() constructor it gaves a ideal solution 
'''

lst=[1,4,2,3,2,21,3,4,4,2,4,42,1,10]
nl=set()
unique=[]
for num in lst:
    if num not in nl:
        nl.add(num)
        unique.append(num)
print(lst)
print(nl)
print(unique)
# by fromkeys() function best ways by dictonary inbuilltt functions
def dec(lst):
    return list(dict.fromkeys(lst))
print(dec(lst))
'''

#Given a list of numbers and a target sum $K$, find if any two numbers in the list add up to $K$.
# by brute force
'''
def trsum(lst,target):
    for i in range(len(lst)):
         for j in range(i+1,len(lst)):
             if lst[i] +lst[j] == target:
              print(f'target sum found {lst[i]} +{lst[j]} = {target}')
              return
    else:
            print(f'target not found')
            return False
lst=[1,2,3,4,5,4,3,2,9]
target = 18
trsum(lst,target)
'''
# two pointers ''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
def trsum(lst,k):
    sorted(lst)
    start = 0
    end = len(lst) -1
    while start <end:
        currentsum = lst[start] +lst[end]
        if currentsum == k:
            print(f'target sum found {lst[start] } + {lst[end]} = {k}')
            return
        elif currentsum < k:
            start +=1
        else:
            end -=1
    return False
lst=[1,2,3,4,5,4,3,2,9]
target = 12
trsum(lst,target)           

'''
#recomended and best method imp'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#using set
'''
def chksum(lst,target):
    element = set()
    for num in lst:
        val = target - num
        if val in element :
            print(f'target sum found {num} + {val} = {target}')
            return
        element.add(num)
lst=[1,2,3,4,5,4,3,2,9]
target = 12
chksum(lst,target)  
'''

#Merge two dictionaries into a single new dictionary. Handle the case where keys overlap.
#by import
'''
from collections import Counter
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 200, 'c': 300, 'd': 40}

merge =dict(Counter(dict1) + Counter(dict2))
print(dict1)
print(dict2)
print(merge)
'''
# by update method
'''
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 200, 'c': 300, 'd': 40}
merge2 = dict1.copy()
merge2.update(dict2)
print(merge2)
'''
#by dictonary unpack method (**dictname , **dict2name)
'''
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 200, 'c': 300, 'd': 40}
merge = {**dict1 , **dict2}
print(merge)

#by dictonary compherision 
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 200, 'c': 300, 'd': 40}
merge2={key: dict1.get(key,0) +dict2.get(key,0) for key in set(dict1) | set(dict2)}
print(merge2)'''

#Given a list of integers, find the number of distinct pairs $(a, b)$ such that $a+b = K$...........................................................
'''
def chkpair(lst,target):
   element = set()
   pairs =set()
   for num in lst:
      sum = target - num
      if sum in element:
         pairs.add(tuple((sum,num)))
      element.add(num)
   return pairs
lst = [1,2,3,2,4,5,6,7,8,9]
k=7
a=chkpair(lst,k)
print(a)
'''

#Write a program to convert a list of tuples (key, value) into a dictionary.
'''
lst = [(1,2),(6,4),(5,6),(7,8)]
nl =dict(lst)
print(type(nl))
print(nl)
print(nl.keys())
print(nl.values())
print(nl.items())

#by loop ''''''''''''''''''''''''''''''''
res={}
for key,value in lst:
    res[key]=value
print(res)
print(type(res))

#by list comphersion '''''''''''''''''''''''''''''''
ans = {key:value for key,value in lst}
print(ans)
'''
#Given a dictionary, invert the mapping (keys become values and values become keys). Assume all values are unique.
'''
dic = {'b': 200, 'c': 300, 'd': 40}
res ={}
for key,value in dic.items():
    res[value]=key
print(dic)
print(dic.keys())
print(dic.values())
print(res)
print(res.keys())
print(res.values())

#by list comphersion 
nd = { value:key for key ,value in dic.items()}
print(nd)
'''

#Implement Bubble Sort to sort a list of numbers.
'''
n=int(input('enter the no of element in your list :' ))
lst =[]
for i in range(n):
    val = int(input(f'enter {i} index element of your list: '))
    lst.append(val)
print(lst)
for i in range(n):
    for j in range(0,n-i-1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)'''

#Find the first occurrence of a target number in a sorted list that may contain duplicates using Binary Search.
#for first and last occurrence..........................................................................................................
'''
def firstoccr(lst,target):
    lst = sorted(lst)
    start = 0
    end = len(lst) -1
    result = -1
    while start <=end :
        mid = (start + end)//2
        if lst[mid] == target :
            result = mid
            end = mid-1
        elif lst[mid] > target:
            end = mid-1
        else:
            start = mid +1
    return result
def lstoccr(lst ,target):
    lst =sorted(lst)
    start =0
    end=len(lst)-1
    result=-1
    while start <=end:
        mid =(start +end)//2
        if lst[mid] == target:
            result =mid
            start =mid+1
        elif lst[mid] >target:
            end= mid-1
        else:
            start =mid+1
    return result

lst =[1,2,8,4,5,4,3,4,5,8,9]
print(sorted(lst))
k=4
a=firstoccr(lst,k)
b=lstoccr(lst,k)
print(a)
print(b)
'''
#Given a list of strings, sort them based on their length, from shortest to longest.
# bby sorted function
'''
lst = ['rahul' , 'ritika' ,'uday', 'ram','om']
nl =sorted(lst,key=len)
print(nl)
print(lst)
#by list.sort fun()
lst.sort(key=len)
print(lst)
#sort on basis last charracter
nll =sorted(lst,key = lambda x : x[-1])
print(nll)
'''
#square root by binary search because it fast 
'''
def sqrot(x):
    start = 0
    end= x//2
    res =1
    
    while start <=end:
        mid= (start+end)//2
        sq =mid**2
        if sq == x:
            return mid
        elif sq < x:
            res= mid
            start =mid+1
        else:
            end =mid-1
    return res
print(sqrot(8))
'''
#Find the $K$-th largest element in an unsorted list.	Sort the list and return the element at the correct index ($N-K$).
#sort lst in reverse order
'''
lst = [1,2,3,4,5,6,7,8]
k=3
nl =sorted(lst,reverse = True)
print(nl)
print(nl[k-1])
#without reverse pick element from end by (n-k)
lst.sort()
print(lst)
n=len(lst)
print(lst[n-k])
'''
#Sort a list of numbers based on their frequency (count of occurrences).................................
'''
from collections import Counter
lst=[1,2,3,4,5,6,5,4,5,6,5,4,34,3,2,223,4,5,43,4,5,5,654,3,6,6,7,89,8,76,6,688]
nll=sorted(lst)
print(nll)

nl=dict(Counter(lst))
print(nl)
print(type(nl))
'''


#Given a rotated sorted array, find a target element. (The hardest problem this week!).......................................
'''
def roatarry(arr , target):
    start =0
    end =len(arr) -1

    while start <=end:
        mid=(start +end)//2
        if arr[mid] == target:
            return mid
        # checking array is sorted froom first half
        if arr[start]  <=arr[mid]:
            if arr[start] <=target<arr[mid]:
                end = mid-1
            else:
                start = mid+1
        else:
            if arr[mid] < target <=arr[end]:
                start = mid+1
            else:
                end = mid-1
    return -1

arr = [4,5,6,7,0,1,2]
target = 0
a= roatarry(arr,target)
print(a)

'''
# binary search using recursion ............................
'''
def binaryrec(arr,target,start,end):
    mid =(start +end)//2
    if start >= end:
        return 
    if arr[mid] == target:
        return mid
    elif arr[mid]>target :
        return binaryrec(arr,target,start,mid-1)
    else:
        return binaryrec(arr,target,mid+1,end)
  
arr = [1,2,3,4,5,6,7,8,9]
a=binaryrec(arr,7,0,len(arr)-1)
print(a)
'''

# selection sort ........................................................................................................
'''
def selectionssort(arr):
    for i in range(len(arr)):
        minimumindex = i
        for j in range(i+1,len(arr)):
            if arr[minimumindex] > arr[j]:
             minimumindex = j
        arr[minimumindex],arr[i]= arr[i],arr[minimumindex]
    return arr
arr = [5,4,6,7,6,3,9,99]
print(selectionssort(arr))
'''
#insertion sort ................................................
'''
def insertion(array):
    for i in range(1,len(array)):
         key = array[i]
         j= i-1
         while j>=0 and array[j] > key:
              array[j+1]= array[j]
              j -=1
         array[j+1] = key
    return array

array = [4,5,6,3,2,1,99]
print(insertion(array))
        
'''

#quick sort algorithm...............................................................
'''
def quik(arr):
    if len(arr) <=1:
        return arr
    
    #mid element of array or a list

    pivot = arr[len(arr)//2]
    start = [num for num in arr if num<pivot]
    mid = [num for num in arr if num == pivot]
    end = [num for num in arr if num > pivot]
    return quik(start) +mid +quik(end)


arr= [7,6,5,4,3,2,1]
print(quik(arr))
'''

# merge sort ...........................................
'''
def brk(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2

    right = brk(arr[:mid])
    left = brk(arr[mid:])
    return mergsort(left,right)

def mergsort(left,right):
    result =[]
    i=j=0
    while i <len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    return result

arr =[5,4,3,2,1,6]
print(brk(arr))
'''
'''


def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2

    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left,right)
def merge(left,right):
    result =[]
    i=j=0

    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    return result

arr =[5,4,3,2,1,6]
print(mergesort(arr))
'''

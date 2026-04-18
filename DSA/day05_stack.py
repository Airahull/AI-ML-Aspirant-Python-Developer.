#stack using normal list in python 
stack=[]
stack.append(9)
stack.append(7)
stack.append(4)
stack.append(2)
#print(stack)
stack.pop()
#print(stack)

#stack using library 
from collections import deque

stack =deque()

stack.append(4)
stack.append(3)
stack.append(5)
stack.pop()
#print(stack)

#1️⃣ Reverse a String / Array
def rev(s):
  stack =deque()
  for ch in s:
    stack.append(ch)

  rev =''
  for ch in stack:
    rev =ch+rev

  return rev
s='rahul'
#print(rev(s))

#valid parenthesis........ very important .......................................................................
def validparenthises(s):
  stack =[]
  mapp = {")":"(","]":"[","}":"{"}
  for ch in s:
    if ch in mapp:
      if not stack or stack.pop() !=mapp[ch]:
        return False
    else:
      stack.append(ch)
  return  not stack
s='{{[(][])]}}'
#print(validparenthises(s))

nums =[1,2,3,4,5]
res = [-1]*len(nums)
#print(res)

#Next Greater Element...................................(monotonic increasing stack )
def nextgreater(arr):
  stack=[]
  res=[-1] * len(arr)
  for i in range(len(arr)):
    while stack and arr[i] > arr[stack[-1]]:#creating monotonic stack using some methods 
      indx=stack.pop()
      res[indx]=arr[i]

    stack.append(i)
  return res

nums = [2, 1, 2, 4, 3]
#print(nums)
#print(nextgreater(nums))

#next smaller .........................(monotonic decreasing stack )
def smaller(arr):
  res=[-1]*len(arr)
  stack=[]
  for i in range(len(arr)):
    while stack and arr[i]<arr[stack[-1]]:
      indx =stack.pop()
      res[indx]=arr[i]
    stack.append(i)
  return res
nums = [2, 1, 2, 4, 3]
#print(nums)
#print(smaller(nums))


#remove duplicate from arr
arr =[2,3,4,5,43,5,6,7,8,7,6,6,5,5667,87]

narr=["_"]*len(arr)
seen =set()
for index,num in enumerate(arr):
  if num not in seen:
    seen.add(num)
    narr[index]=num
print(narr)


#greater one 
def grett(arr):
  stack =[]
  res=[-1]*len(arr)
  print(len(res))
  for i in range(len(arr)):
    while stack and arr[i] > arr[stack[-1]]:
      index=stack.pop()
      res[index]=arr[i]
    stack.append(i)
  return res 
nums = [2, 1, 2, 4, 3]
print(grett(nums))


def window(arr,k):
  n=len(arr)
  if k>n:
    return []
  som =sum(arr[:k])
  res =[som]
  for i in range(k,n):
    som = som + arr[i] - arr[i-k]
    res.append(som)
  return res 
numss = [2, 1, 2, 4, 3]
print(window(numss,k:=3))


def vallid(s):
  stack =[]
  mapp = {")":"(","]":"[","}":"{"}
  for ch in s:
     if ch in mapp:
       if not stack or stack.pop() != mapp[ch]:
         return False
     else:
      stack.append(ch)
  return not stack

s='((({{[]}})))'
print(vallid(s))

Prices = [100, 80, 60, 70, 60, 75, 85,100, 80, 60, 70, 60, 75, 85]
span =[1, 1, 1, 2, 1, 4, 6, 8, 1, 1, 2, 1, 4, 6]
span =[1, 1, 1, 2, 1, 4, 6, 8, 1, 1, 2, 1, 4, 6]



print((-1//2))


#stock span problem ........................................................................................................


def stock(prices):
  n = len(prices)
  stack =[]
  span = [0]*n
  for i in range(n):
    while stack and prices[stack[-1]] <=prices[i]:
      stack.pop()
    if not stack:
      span[i] = i+1
    else:
      span[i] = i -stack[-1]
    stack.append(i)
  return span

prices =[10, 80, 60, 70, 60, 75, 85]
print("stocks prices = ",prices)
print("stock span = ",stock(prices))


def ng(arr):
  n=len(arr)
  res =[-1]*n
  stack=[]

  for i in range(n):
    while stack and arr[i] > arr[stack[-1]]:
      indx = stack.pop()
      res[indx] = arr[i]
    stack.append(i)
  return res

nums = [2, 1, 2, 4, 3]
print(ng(nums))




def vp(s1):
  stack =[]
  mapping = {"]":'[',"}":"{",")":"("}
  for ch in s1:
    if ch in mapping:
      if  not stack or stack.pop() != mapping[ch]:
        return False
    else:
      stack.append(ch)
  return not stack

#monotonic incresing very important stack
def nexgret(arr):
  stack =[]
  res=[-1]*len(arr)
  for i in range(len(arr)):
    while stack and arr[i]>arr[stack[-1]]:
      indx =stack.pop()
      res[indx] = arr[i]
    stack.append(i)
  return res
nums = [2, 1, 2, 4, 3]
print(nexgret(nums))
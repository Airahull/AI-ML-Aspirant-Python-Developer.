# Slinding window basics .....................................
#1.sum of all fixed size window element in a list or arr
#or sum all all subarrays of k fixed size in an array..................

def sum_of_subarray(arr,k):
    n=len(arr)
    if k>n:
        return[]
    #sum of first window 
    curentsum=sum(arr[:k])
    res=[curentsum]

    for i in range(k,n):
        curentsum = curentsum +arr[i] - arr[i-k]

        res.append(curentsum)
    return res

#arr = [2,3,5,1,6]
#k = 7
nums = [2, 1, 2, 4, 3]
print(sum_of_subarray(nums,k:=3))

#2.Maximum Sum Subarray of Size K...................
def maxsum(arr,k):
    n=len(arr)
    if k>n:
        return []
    #sum of first window in arr
    cur =sum(arr[:k])
    maxi =cur
    for i in range(k,n):
        cur =cur+ arr[i] -arr[i-k]
        maxi = max(cur,maxi)

    return maxi
arr = [2,3,5,1,6]
k = 3
#print(maxsum(arr,k))

#3.Find the Average of All Subarrays of Size K

def avrage(arr,k):
    n=len(arr)
    if k>n:
        return []
    suum = sum(arr[:k])
    res =[]
    res.append(suum/k)
    for i in range(k,n):
        suum = suum + arr[i] -arr[i-k]

        res.append(suum/k)
    return res
arr = [2,3,5,1,6]
k = 3
#print(avrage(arr,k))

#4.Sliding Window Maximum (Fixed Size)
#Task: For every window of size k, find the maximum element.
#brute force solution 

def maximum(arr,k):
    n=len(arr)
    if k>n:
        return []
    ele = arr[:k]
    res=[]
    res.append(max(ele))
    for i in range(k,n):
        ele = arr[(i-k)+1:i+1]

        res.append(max(ele))
    return res
arr=[1,3,-1,-3,5,3,6,7]
k = 3
#print(maximum(arr,k))
from collections import deque
def maxelement(arr,k):
  dq = deque()

  res =[]
# find maximum element for first window........
  for i in range(k):
      while dq and arr[dq[-1]] < arr[i]:
          dq.popleft()
      dq.append(i)
  res.append(arr[dq[0]])
# steps for finding maximum element for all left windows 
  for i in range(k,len(arr)):
      while dq and arr[dq[0]]<i-k:
          dq.pop()
      dq.append(i)
      # finding maximum in left windows 
      while dq and arr[dq[-1]] <=arr[i]:
          dq.pop()
      dq.append(i)
      res.append(arr[dq[0]])
  return res

arr=[1,2,3,4,5,6]
k=3
#print(maxelement(arr, k))
#brute force solution of it first negative number in a window 
def negative(arr,k):
    n=len(arr)
    res=[]
    if k>n:
        return []
    for i in range(k):
        if arr[i] <0:
            res.append(arr[i])
    for i in range(k,n):
        win = arr[(i-k) +1:i]
        if arr[i] < 0:
            res.append(arr[i])
    return res
arr=[-1,-2,3,4,-5,-1]
k=3
#print(negative(arr,k))
# and its optimal solution using deque 
from collections import deque 
def firstnegative(arr,k):
    q=deque()
    res =[]
    n =len(arr)
    if k>n:
        return []
    for i in range(k):
        if arr[i] < 0:
            q.append(i)
    if q:
        res.append(arr[q[0]])
    else:
        res.append(0)
    for i in range(k,n):
        while q and q[0] <= i-k:
            q.popleft()
            
        if arr[i] <0:
              q.append(i)

        if q:
         res.append(arr[q[0]])
        else:
         res.append(0)
    return res 
arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
#print(firstnegative(arr,k))

#disticnt pair in window 
arr=[1,2,3,4,5,3,4,599]
#print(" ".join(map(str,arr)))
#print(max(arr))

name ='rahul'
#print(name[0])
def isValid(s):
    stack = []
    mapping = {')':'(', ']':'[', '}':'{'}

    for ch in s:
        if ch in mapping:
            if not stack or stack.pop() != mapping[ch]:
                return False
        else:
            stack.append(ch)

    return not stack
print(isValid(s:='('))


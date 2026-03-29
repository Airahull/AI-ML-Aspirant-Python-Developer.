#array questions..........................-------------------------------------------
#1️⃣ Find the second largest element in an array-------------------------------------

arr =[2,3,4,5,43,5,6,7,8,7,6,6,5,5667,87]
k=2
nr=sorted(arr,reverse = True)
#print(nr[k-1])

#  or 
n=len(arr)
newarr=sorted(arr)
#print(newarr[n-k])

#best optimal way ........................-------------------------------------------
arr =[2,3,4,5,43,5,6,7,8,7,6,6,5,5667,87]
first=secound=float('-inf')

for num in arr:
    if num>first:
        secound =first
        first=num
    elif first>num>secound:
        secound=num
#print(secound)

#2️⃣ Remove duplicates from an array without using set()------------------------------
#brute force solutions 
arr =[2,3,4,5,43,5,6,7,8,7,6,6,5,5667,87]
res=[]
for num in arr:
    if num not in res:
        res.append(num)
#print(res)

#best optimal solution without using set using dictonary 
#imp................................................................................................
arr =[2,3,4,5,43,5,6,7,8,7,6,6,5,5667,87]
res=[]
element={}
for num in arr:
    if num not in element:
        element[num]= True
        res.append(num)
#print(res)

#5️⃣ Move all zeros to the end of array (in-place)-----------------------------------
arr=[0,1,0,3,12,24,0,3,4,23]
left=0
for right in range(len(arr)):
    if arr[right] !=0:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
#print(arr)

#6️⃣ Find all pairs of numbers whose sum equals a target (Two-sum)------------------
def targetsum(arr,k):
    #res=[]
    valu=set()
    for num in arr:
        dig = k-num
        if dig in valu:
            print('target sum found _->>',(num,dig))
            return
        valu.add(num)
        #res.append(num)
    return None
arr =[2,3,4,5,43,5,6,7,8,7,6,6,5,5667,87]
k=130
#targetsum(arr,k)
#target sum for returning indexes.....................................................
def targetsumindex(arr,k):
    dict={}
    for i,num in enumerate(arr):
        val = k-num
        if val in dict:
            print(f'target sum found in {dict[val]}index value + {i}index ')
            return
        dict[num] =i

arr =[2,3,4,5,43,5,6,7,8,7,6,6,5,5667,87]
k=130
#targetsumindex(arr,k)
#pratice--------------------------------------------------------------------------
def som(arr,k):
    res={}
    for index,num in enumerate(arr):
        digit = k-num
        if digit in res:
            print('target sum found in these indexes ',(res[digit],index))
            return
        res[num] = index
    return None
arr =[2,3,4,5,43,5,6,7,8,7,6,6,5,5667,87]
k=130
#som(arr,k)

#7️⃣ Find the majority element (appears more than n/2 times)--------------------------
#it a brute force for most frequent element or majority as well 
def majority(arr):
    res={}
    maxi=0
    for num in arr:
        res[num]=res.get(num,0) +1
    
        maxi =max(res.values())
    for key,value in res.items():
        if value == maxi:
            return key,value
    return maxi
arr =[2,3,4,5,43,5,6,7,8,7,6,6,5,5667,87]
print(majority(arr))

#best ideal solution bores voting algorithm ..impo......................................................................
def majorityy(arr):
    count=0
    candidate =None
    for num in arr:
        if count==0:
            candidate=num
            #count+=(1 if candidate==num else -1)
        if candidate==num:
          count+=1
        else:
            count-=1
    return candidate
arr =[2,3,4,2,3,2,3,2,4,22,4,4,2]
print(majorityy(arr))

#most frequent element in an array ------------------------------------------
#imp...........................................................................................................
def mstfreq(arr):
    freq={}
    maxfreq=0
    element =None
    for num in arr:
        freq[num]=freq.get(num,0)+1

        if freq[num] >maxfreq:
            maxfreq=freq[num]
            element=num
    return maxfreq,element
arr =[2,3,4,2,3,2,3,2,4,22,4,4,2]
print(mstfreq(arr))

#4️⃣ Find the missing number in an array of size n containing 1 to n+1------------
arr=[1,2,3,4,5,6,7,9]
n=len(arr)
totalsum = ((n+1)*(n+2))//2
arrsum = sum(arr)
missingnum=totalsum-arrsum
print("missing no in your array is :",missingnum)

#8️⃣ Find the maximum subarray sum (Kadane’s Algorithm) also meaning of question 
#✅ Kadane’s Algorithm Code (Python)
# this approach is also for finding the maximum sum of unfixed size window in sliding window ...............................................

def maxsumofsubarr(arr):
    maxsum=float('-inf')
    currsum=0
    for num in arr:
        currsum+=num
        if currsum>maxsum:
         maxsum =currsum
        if currsum <0:
         currsum=0
    return maxsum
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maxsumofsubarr(arr))


#3️⃣ Check if two arrays are rotations of each other--------------------------------
def rotated(A,B):
    if len(A)!=len(B):
        return False
    A = ' '.join(map(str,A))
    B = ' '.join(map(str,B))
    return B in (A + " " + A)
A = [1, 2, 22, 4, 5]
B = [3, 4, 5, 1, 2]
print(rotated(A , B))

#prefix sum of an array '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def prefix_sum(arr):
    n = len(arr)
    prefix = [0]*n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix

# Example array
arr = [1, 2, 3, 4, 5]

# Build prefix sum array
prefix = prefix_sum(arr)

# Function to answer range sum queries--------------------------------------------
def range_sum(prefix, L, R):
    if L == 0:
        return prefix[R]
    else:
        return prefix[R] - prefix[L-1]

L=0
R=3
print(f"Sum from index {L} to {R} = {range_sum(prefix, L, R)}")

arr = [1, 2, 3, 4, 5]
l=int(input('enter starting range :'))
r=int(input('enter ending range :'))
sum=0
for i in range(l,r+1):
     sum+=arr[i]
print(sum)



#function for prefix array .....................................................
def prefixsum(prefix,l,r):
     if l==0:
          return prefix[r]
     else:
          return prefix[r]-prefix[l-1]
     
#-----------------------------------------------------------------------------------


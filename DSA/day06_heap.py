#heap 
#1. min heap (by dafault )
import heapq
h=[]
heapq.heappush(h,20)
heapq.heappush(h,10)
heapq.heappush(h,25)
print(h)
print(heapq.heappop(h))


#2.max heap (trick)
h=[]
heapq.heappush(h,-20)
heapq.heappush(h,-10)
heapq.heappush(h,-25)
print(h)
print(-heapq.heappop(h))


import heapq

arr =[2,3,4,5,43,5,6,7,8,7,6,6,5,5667,87]

heap = [-x for x in arr]
heapq.heapify(heap)
print(-heapq.heappop(heap))


# find the kth largest elemenet in an array 
# by using min heap  very important-------------------------------------------------------------------------------------------------------------------
import heapq
def kthlarge(arr,k):
    heap =[]
    for num in arr:
        heapq.heappush(heap,num)

        if len(heap) > k:
          heapq.heappop(heap)
    print(heap[0])

n = int(input("enter a length of array : "))
arr=[]
for i in range(n):
    val = int(input(f"enter {i} index value : "))
    arr.append(val)
print(f"your array is :{arr}")
print(f"sorted array is : {sorted(arr)}") #1.this line is only for understanding purpose 
k = int(input("enter your kth position to find the element : "))
#kthlarge(arr,k)


#using maxheap------------------------------------------------------------------------------------------------------------------------------------- 
def klarge(arr,k):
    heap =[ -num for num in arr]
    heapq.heapify(heap) # for converting a python list into a binary heap structure which uses internally  

    for _ in range(k-1):
        heapq.heappop(heap)

    print(-heapq.heappop(heap))

arr=[2,3,4,5,4,5,6,76]
k=3
#klarge(arr,k)

# kth frequent element .........................................................
#heap and hash maps 
import heapq

def kthfreq(arr,k):
    freq ={}
    h=[]
    for num in arr:
        freq[num]=freq.get(num,0)+1
    for num,occurance in freq.items():
        heapq.heappush(h,(occurance,num))# in it we write occurance first because python campare thing in lexicographically means in dictonary order means left to right 

        if len(h) > k:
            heapq.heappop(h)
    return [num for occrance,num in h]    
nums = [1,1,1,2,2,3]
k = 2
print(kthfreq(nums,k))


    
    


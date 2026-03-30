
#linear search.................................................................. 

def linearsearch(lst,target):
    for index ,num in enumerate(lst,0):
        if num == target:
            print(f"target found in {index} index ")
            break
    else:
            print('target not found in your list ')


#binary search.................................................................
#it always apply on a sorted list
def binarysearch(arr,target):
     start = 0
     end = len(arr)-1
     while start <=end:
          mid = (start +end)//2
          if target == arr[mid]:
               print(f'your target {target} found in {mid} index ')
               return mid
          elif target >arr[mid]:
               start = mid+1
          else:
               end =mid-1
     else:
          print("target not found !!!")

# recursive binary search...................................................

def recursivebinarysearch(arr,target,start,end):
     mid = (start+end)//2
     if start > end:
          return arr
     if arr[mid] == target:
          print(f'number {target} found in {mid} index ')
          return mid
     if arr[mid] > target:
          return recursivebinarysearch(arr,target,start,mid-1)
     else:
          return recursivebinarysearch(arr,target,mid +1,end) 
     
#sorting algorithms ..............................................-----------------------------------------------------
#1. bubble sort ........................................................................................

def bubblesort(arr):
     for i in range(len(arr)):
          for j in range(len(arr)-i-1):
               if arr[j+1]<arr[j]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
     return arr 
    
#2.selection sort ......................................................................................

def selectionsort(arr):
     for i in range(len(arr)-1):
          minimumindex= i
          for j in range(i+1,len(arr)):
               if arr[minimumindex] > arr[j]:
                    minimumindex =j 
          arr[i],arr[minimumindex] = arr[minimumindex],arr[i]
     return arr 

#3 insertion sort>>......................................................................................

def insertionsort(arr):
     for i in range(1,len(arr)):
          key = arr[i]
          j=i-1
          while j>=0 and arr[j] >key:
               arr[j+1] =arr[j]
               j-=1
          arr[j+1] =key
     return arr               

# quicksort...............................................................................................

def quicksort(arr):
     if len(arr) <=1:
          return arr
     pivot = arr[len(arr)//2]
     left = [ x for x in arr if x<pivot]
     middle = [x for x in arr if x==pivot]
     right = [x for x in arr if x>pivot] 
     return quicksort(left) + middle +quicksort(right)

# mergesort...............................................................................................

def mergesort(arr):
     if len(arr) <=1:
          return arr
     mid =len(arr)//2
     left = mergesort(arr[:mid])
     right =mergesort(arr[mid:])

     return merge(left , right)

def merge(left,right):
     i=j=0
     res =[]
     while i < len(left) and j<len(right):
          if left[i] >right[j]:
               res.append(right[j])
               j+=1
          else:
               res.append(left[i])
               i+=1
     res += left[i:]
     res += right[j:]
     return res




lst = [1,7,1,4,0,90,7,5,6,7,88,54]
#linearsearch(lst,99)
#binarysearch(lst,100)
#recursivebinarysearch(lst,88,0,len(lst)-1)
#print(bubblesort(lst))
#print(selectionsort(lst))
#rint(insertionsort(lst))
#print(quicksort(lst))
#print(mergesort(lst))

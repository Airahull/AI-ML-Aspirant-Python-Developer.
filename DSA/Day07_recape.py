'''
✅ Top 10 Python Array (List) Questions
1️⃣ Find the second largest element in an array

Example: [12, 35, 1, 10, 34, 1] → 34

2️⃣ Remove duplicates from an array without using set()

Keep the order same.
Example:
[1,2,2,3,4,4] → [1,2,3,4]

3️⃣ Check if two arrays are rotations of each other

Example:
A = [1,2,3,4,5]
B = [3,4,5,1,2] → True

4️⃣ Find the missing number in an array of size n containing 1 to n+1

Example:
[1,2,4,5] → 3

5️⃣ Move all zeros to the end of array (in-place)

Example:
[0,1,0,3,12] → [1,3,12,0,0]

6️⃣ Find all pairs of numbers whose sum equals a target (Two-sum)

Example:
arr=[2,7,11,15], target=9 → (2,7)

7️⃣ Find the majority element (appears more than n/2 times)

Example:
[3,3,4,2,3,3,3] → 3

8️⃣ Find the maximum subarray sum (Kadane’s Algorithm)

Example:
[-2,1,-3,4,-1,2,1,-5,4] → 6

9️⃣ Check if an array is sorted and rotated

Example:
[3,4,5,1,2] → Yes

🔟 Find the first negative number in every window of size k

Sliding window problem.
Example:
arr=[12,-1,-7,8,-15,30,16,28], k=3
Output → [-1,-1,-7,-15,-15,30]
'''
#1. Find the second largest element in an array
def secounlarge(arr):
    firstlarge = float('-inf')
    secound =0
    for num in arr:
        if num >firstlarge:
            firstlarge=num
        if firstlarge>num>secound:
            secound=num
    return secound
arr =[12, 35, 1, 10, 34, 1] 
#print(secounlarge(arr))

#2.Remove duplicates from an array without using set()
def remove(arr):
    res={}
    ans =[]
    for num in arr:
        res[num]=res.get(num,0)+1
    for key,value in res.items():
       
       ans.append(key)
    return ans 
arr=[1,2,2,3,4,4]
#print(remove(arr))

#3.Check if two arrays are rotations of each other
def rotated(a,b):
    if len(a) !=len(b):
        return False
    str_a= ' '.join(map(str,a))
    str_b= " ".join(map(str,b))

    return str_b in (str_a + " " + str_b)

A = [1,2,3,4,5]
B = [3,4,5,1,2]
#print(rotated(A,B))

#4. Find the missing number in an array of size n containing 1 to n+1
def missing(arr):
    n=len(arr)
    #formula to finding total sum of arr from 1 to n
    totalsum = ((n+1)*(n+2))//2
    arrsum =sum(arr)

    missingnum =totalsum-arrsum
    return missingnum
arr=[1,2,4,5]
#print(missing(arr))

#5.Move all zeros to the end of array (in-place)
def movezero(arr):
    left =0
    n=len(arr)
    for right in range(n):
        if arr[right] !=0:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
    return arr
arr =[0,1,0,3,12]
#print(movezero(arr)) 

#6.Find all pairs of numbers whose sum equals a target (Two-sum) and return indexes
def pairsum(arr,target):
    res={}
    for index,num in enumerate(arr):
        val= target-num
        if val in res:
            return (res[val],index)
        res[num] =index  
    return None
arr=[2,7,11,15]
target =9
#print(pairsum(arr,target))

#7.Find the majority element (appears more than n/2 times)(bores voting algorithm )............................................................
def majority(arr):
    canditate =None
    count =0
    for num in arr:
        if count ==0:
            candidate =num
        if num == candidate:
             count+=1
        else:
             count-=1
    return candidate

arr=[3,3,4,2,3,3,3]
#print(majority(arr))

#8.Find the maximum subarray sum (Kadane’s Algorithm)..........................................................................................

def maxisum(arr):
    maxsum= float('-inf')
    currentsum =0
    for num in arr :
        currentsum = currentsum+num 
        if currentsum>maxsum:
            maxsum=currentsum
        if currentsum <0:
            currentsum=0
    return maxsum
arr=[-2,1,-3,4,-1,2,1,-5,4]
#print(maxisum(arr))

#9.Find the first negative number in every window of size k (sliding window )
from collections import deque

def negative(arr,k):
    dq =deque()
    n=len(arr)
    res=[]
    if k>n:
        return []
    for i in range(k):
        if arr[i]<0:
           dq.append(i)

    if dq:
        res.append(arr[dq[0]])
    else:
        res.append(0)
    for i in range(k,n):
        if dq and dq[0] <=i-k:
            
            dq.popleft()
        if arr[i]<0:
           dq.append(i)

        if dq:
            res.append(arr[dq[0]])
        else:
            res.append(0)

    return res


arr=[12,-1,-7,8,-15,30,16,28]
k=3
Output= [-1,-1,-7,-15,-15,30]  
#print(negative(arr,k)) 

#..........................................................strings..............................................................................
'''
1.Reverse String

2.Check palindrome

3.Count vowels

4.Remove duplicates

5.Longest substring without repeating characters

6.Check anagram

7.First non-repeating character

8.Compress string

9.Word frequency counter

10.Rotate string'''

#1.Reverse String
name ='rajat'
#print(name[::-1])

#3.Count vowels
name ='rajat'
vowels ='aeiou'
count =0
for ch in name:
    if ch in vowels :
        count+=1
#print(count)

#4.Remove duplicates
name ='arajiat'
seen =set()
res =""
for ch in name:
    if ch not in seen:
        seen.add(ch)
        res+=ch
#print(res)

#5.Longest substring without repeating characters,very imp logic................................................................

def lenoflonsub(s):
    res ={}
    left =0
    maxlen=0
    lonsub =""
    for right,ch in enumerate(s):
        if ch in res and res[ch] >= left:
            left = res[ch] +1
        res[ch]=right
        currentlen =right-left+1
        if currentlen > maxlen:
            maxlen =currentlen
            lonsub =s[left:right+1]
    return maxlen,lonsub
s='abbsadbss'
#print(lenoflonsub(s))

#6.Check anagram
def anagram(s1,s2):
    freq={}
    if len(s1) !=len(s2):
        return False
    for ch in s1:
        freq[ch] = freq.get(ch,0)+1
    for ch in s2:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] = freq[ch]-1
    return True


s1='debit card'
s2='bad credit'
#print(anagram(s1,s2))

#7.First non-repeating character
def firstnonrepch(s):
    freq ={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    for index,ch in enumerate(freq):
        if freq[ch] ==1:
            return ch,index

    return None

s='absgbaasx'
#print(firstnonrepch(s))

#8.mosst rep character.............. important logic.........................................................................................
def mstrep(s):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    mostrep =0
    char=''
    for ch,val in freq.items():
        if val> mostrep:
            mostrep=val
            char=ch
    return mostrep,char
s = "aabbbcddddde"
#print(mstrep(s))
#----------------------------------------------------------------------
#9.Compress string
def compress(s):
    res ={}
    cs=''
    for ch in s:
        res[ch]=res.get(ch,0)+1
    for key,value in res.items():
        cs+=key
        cs+=str(value)
    return  cs
s = "aabbbcddddde"
print(compress(s))

#most frequent number in array................................................
arr=[1,2,3,4,3,4,5,32,1,2,3,3,3,3]
res={}
maxfreq=0
number = 0
for num in arr:
    res[num]=res.get(num,0)+1
print(res)
for key,value in res.items():
    if value>maxfreq:
        maxfreq=value
        number=key
print(number,'occure', maxfreq,'times')

#more pythonic way but not optimal ................................................................
from collections import Counter
arr=[1,2,3,4,3,4,5,32,1,2,3,3,3,3]
k=int(input('how many elements freq you wants to check :'))
freq =Counter(arr)

occurance=freq.most_common(k)
print(f'frequency {occurance} occurance ')

# freq for kth elements ....................

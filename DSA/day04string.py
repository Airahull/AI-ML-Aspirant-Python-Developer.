#important questions on strings..........................................................
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

#1.Reverse String.......................................

s='rohan'
#print(s[::-1])

#2.Check palindrome..................................
s='nitin'
temps =s[::-1]
#print('pallindrome') if s==temps else print('not pallidrome')

#3.Count vowels...................................................
s='Non-Repeating Character'
vowels =set('aeiouAEIOU')
count=0
for ch in s:
  if ch in vowels:
      count+=1
#print('total vowels in string is :',count)

#4.Remove duplicates'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

s='Non Repeating Character'
new =set()
res=[]
for ch in s:
    if ch not in new:
        new.add(ch)
        res.append(ch)
result = "".join(res)
#print(result)

#6.Check anagram.........................................................
# and we can also done it with counter function
'''
s1 = 'a gentleman'
s2='agent leman'
s1 = s1.replace(" ",'').lower()
s2=s2.replace(" ","").lower()
if len(s1) !=len(s2):
    print('not anagram')

if sorted(s1) == sorted(s2):
    print('anagram ')
else:
    print('not anagram ')'''

#9.Word frequency counter.................................................
from collections import Counter
s='Non Repeating Character'
#print(Counter(s))
#and 
res={}
for ch in s:
    res[ch]=res.get(ch,0)+1
#print(res)

#10.rotate a string
'''
 1. Left rotate by 1                  ----->>     ✅
 2. Right rotate by 1                 ----->>     ✅
 3. Left rotate by k                  ----->>     ✅
 4. Right rotate by k                 ----->>     ✅
 5. Using slicing (best & easiest)    ----->>     ✅
 6. Using deque (fastest)             ----->>     ✅
 7. Check if two strings are rotation ----->>     ✅
 8. All possible rotations of string  ----->>     ✅
 9. Rotate until palindrome           ----->>     ✅
 
'''
def Leftrotate(s):
    return s[1:] +s[0]
print(Leftrotate("abcdef")) 

def rightrotate(s):
    return s[-1] + s[:-1]
print(rightrotate("abcdef")) 

def rotateleftbyk(s,k):
    return s[k:] + s[:k]
print(rotateleftbyk("abcdef",3)) 

def rotaterightbyk(s,k):
    return s[-k:] +s[:k]
print(rotaterightbyk("abcdef",3)) 

 

#7.First Non-Repeating Character in a String imp.......................................................................
def nonrepating(s):
    res={}
    for ch in s:
        res[ch]= res.get(ch,0)+1
    for index,ch in enumerate(s):
        if res[ch]==1:
            return (index,ch)
    else:
            return -1,None
s = "aabbcdde"
#print(nonrepating(s))  


def nonrep(s):
    freq={}
    for ch in s:
        freq[ch] = freq.get(ch,0)+1
    for index,ch in enumerate(s):
        if freq[ch] == 1:
            return (index,ch)
    else:
        return None
s = "aabbbcdde"
#print(nonrep(s))  

#2.Most repeating character.................................................
#brute force approach ''''''''''''''''''''''''''''''''''
def mostrep(s):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
        
    for key,value in freq.items():
        if value == max(freq.values()):
            return (key ,value)
     
s = "aabbbcddddde"
#print(mostrep(s))

# optimal solutiion ...................................................................................................
def mostrepp(s):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    maxvalue=0
    char =None
    for key,value in freq.items():
        if value > maxvalue:
            maxvalue =value
            char=key
    return (char,maxvalue)  
s = "aabbbcddddde"
#
# print(mostrepp(s))

#Check anagram......................................................... most ideal solution.imp.................................................. 
def anagram(s1,s2):
    freq={}
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    if len(s1) != len(s2):
        print('not anagram !!')
        return
    for ch in s1:
        freq[ch]=freq.get(ch,0)+1
    for ch in s2:
        if ch not in freq or freq[ch]==0:
            print('not anagram !')
            return
        freq[ch]=freq[ch] -1
    else:
        print('anagram ')
        return
   
s1='debit card'
s2='bad credit'
anagram(s1,s2)



#very imp question''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def lenoflongestsubstring(s):
    lastindex ={}
    left=0
    maxlen = 0
    maxsub=""
    for right,ch in enumerate(s):
        if ch in lastindex and lastindex[ch] >=left:
            left =lastindex[ch]+1
        lastindex[ch]=right
        currentlen = right-left+1
        if currentlen >maxlen:
            maxlen=currentlen
            maxsub=s[left:right+1]
    return  maxlen,maxsub
s='abbsadbss'
print(lenoflongestsubstring(s))




def lss(s):
    left=0
    res={}
    maxlen=0
    maxstring=''
    for right,ch in enumerate(s):
        if ch in res and res[ch] >=left:
            left=res[ch]+1
        res[ch] =right
        currentlength = right-left+1
        if currentlength>maxlen:
            maxlen=currentlength
            maxstring=s[left:right+1]
    return (maxlen,maxstring)
s='assdedsdfghj'
print(lss(s))
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def ana(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    if len(s1)!=len(s2):
        print('not anagram !')
        return 
    freq={}
    for ch in s1:
        freq[ch]=freq.get(ch,0)+1
    for ch in s2:
        if ch not in freq or freq[ch]==0:
            print('not anagram !!')
            return 
        freq[ch]= freq[ch] -1
    else:
        print('anagram ')
        return
s1='debit card'
s2='bad credit'
ana(s1,s2)



def lols(stri):
    left =0
    freq={}
    maxlenn=0
    maxstri= ""
    for right,ch in enumerate(stri):
        if ch in freq and freq[ch]>=left :
            left =freq[ch]+1
        freq[ch]=right
        currenlen =right-left+1
        if currenlen >maxlenn:
            maxlenn=currenlen
            maxstri = stri[left:right+1]
    return maxlenn,maxstri
s='abbsadbss'
print(lols(s))




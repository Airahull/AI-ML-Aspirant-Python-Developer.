# for displaying normal learning linkedlist
# Method 1: Creating a Linked List of 4 Values Manually (Best for Understanding)
'''

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = n1

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end= " -> ")
            temp =temp.next
        print(None)

n1=node(20)
n2=node(30)
n3=node(40)
n4=node(50)
n5=node(60)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
l = linkedlist()
l.display()
'''
# Method 2: Creating a Linked List Using a Class (INTERVIEW-STYLE)
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head =None
# for inserting elements in the end of linked list ----------------------------------------------------------------------------------------------
    def insert_end(self,data):
        newnode = node(data)

        if self.head is None:
            self.head=newnode
            return 
        temp =self.head 
        while temp.next is not None:
            temp = temp.next 

        temp.next= newnode
# for inserting elements in begain ------------------------------------------------------------------------------------------------------------
    def insert_begin(self,data):
        newnode = node(data)

        if self.head is None:
            self.head = newnode
            return
        newnode.next =self.head
        self.head = newnode 
# for display linkedlist-------------------------------------------------------------------------------------------------------------------------
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data ,end="->")
            temp =temp.next
        print(None)
# for deleting head and deleting any element by key/value------------------------------------------------------------------------------------------
    def deletee(self,key):
        def __init__(self):
            self.key =key
        #case 1 deleting head node
        temp =self.head
        if temp and temp.data == key:
            self.head =temp.next
            return 
        #case 2 deleting from middle and end 
        prev=None
        temp = self.head
        while temp and temp.data !=key:
           prev =temp 
           temp =temp.next

        if temp is None:
            return
        prev.next =temp.next
#for reversing a linked list---------------------------------------------------------------------------------------------------------------------
    def reverse(self):
        #with help of 3 pointers 
        prev =None
        curr = self.head
        while curr is not None:
            nextnode = curr.next #saving current  next element to nextnode
            curr.next=prev       #linking with previous element 
            prev=curr            #move previous pointer forword 
            curr =nextnode       #move curr pointer forword 
        self.head = prev # change head position 

# for finding middle node by using two pointer slow and fast pointer -----------------------------------------------------------------------
    def middle(self):
        fast = self.head
        slow =self.head

        while fast and fast.next :
            slow = slow.next      # it takes 1 step forword 
            fast = fast.next.next # it takes 2 step forword 
        return slow.data
    
#Floyd’s Cycle Detection Algorithm (Best ✅)-------------------------------------------------------------------------------------------------
    def cycle(self):
        slow = self.head
        fast =self.head

        while fast and fast.next:  #it means while fast is not none and fast.next is not none...
            slow = slow.next       # 1 steps
            fast = fast.next.next  # 2 steps

            if fast == slow:       #checking meeting points 
                return True        # cycle found 
        return False               #cycle not found 
    
# len of linkedlist -----------------------------------------------------------------------------------------------------------------------------
    def length(self):
        count =0
        temp = self.head

        while temp :
            count +=1
            temp = temp.next
        return count 
# detect first cycle ---------------------------------------------------------------------------------------------------------------------------
    def detectCycleStart(self):
        fast = self.head
        slow = self.head 

        while fast and fast.next:
            slow=slow.next
            fast =fast.next.next

            if fast == slow:
                break 
        if fast is None or fast.next is None:
            return None
        
        slow =self.head
        while slow !=fast:
            slow = slow.next
            fast = fast.next
        return slow 
# case 1. remove duplicate from a sorted linkedlist-----------------------------------------------------------------------------------------------------
    def remove_dup_sorted(self):
        curr = self.head
        while curr and curr.next:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr=curr.next
        return self.head
    
#remove duplicate from unsorted list --------------------------------------------------------------------------------------------------------------
    def remove_dup_unsorted(self):
        curr = self.head
        prev =None
        seen =set()
        while curr:
            if curr.data in seen:
                prev.next = curr.next
            else:
                seen.add(curr.data)
                prev = curr
            curr =curr.next
        return self.head

#---------------------------------------------------------------
ll = linkedlist()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_end(30)
ll.insert_begin(5)
ll.insert_begin(2)
ll.insert_begin(2)
print("full linkedlist is ")
ll.display()
print("-------------------------------------------")
ll.deletee(20)

print("after deleting 20 from linkedlist")
ll.display()
print("-------------------------------------------")
print("head of linkedlist is :",ll.head.data)
print("-------------------------------------------")
print('mid element of your linked list is',ll.middle())
print("-------------------------------------------")
ll.remove_dup_sorted()
print("after removing duplicate ")
ll.display()
print("-------------------------------------------")
ll.reverse()

print("after reverse a linkedlist ")
ll.display()
print("-------------------------------------------")
print("head of linkedlist is :",ll.head.data)
print("-------------------------------------------")
print('mid element of your linked list is',ll.middle())
print("-------------------------------------------")

print("length of linked list is ",ll.length())
print("-------------------------------------------")

l2 =linkedlist()
l2.insert_end(30)
l2.insert_end(2)
l2.insert_end(30)
l2.insert_end(5)
l2.insert_end(2)

l2.display()


l2.remove_dup_sorted() #  it not worked because of list is not sorted it only check adjusent element '''''''''
l2.display()
l2.remove_dup_unsorted()
l2.display()


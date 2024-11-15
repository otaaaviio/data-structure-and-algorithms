from linked_list import *

def find_middle(head):
    slow = head
    fast = head.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow    
    
def merge(l1, l2):
    dummy = Node()
    tail = dummy
    
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next

def merge_sort(head):
    if not head or not head.next:
        return head
    
    mid = find_middle(head)
    
    after_mid = mid.next
    mid.next = None
    
    left = merge_sort(head)
    rigth = merge_sort(after_mid)
    
    sorted_list = merge(left, rigth)
    
    return sorted_list


new_list = LinkedList()
new_list.insertAtBegin(1)
new_list.insertAtBegin(2)
new_list.insertAtBegin(3)
new_list.insertAtBegin(4)
new_list.insertAtBegin(5)
new_list.insertAtBegin(6)

sorted_list = merge_sort(new_list.head)
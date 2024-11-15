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
    right = merge_sort(after_mid)
    
    sorted_list = merge(left, right)
    
    return sorted_list


# tests

# new_list = LinkedList()
# new_list.insertAtBeginArray([1, 2, 3, 4, 5, 6])

# print(new_list) # before: 6 -> 5 -> 4 -> 3 -> 2 -> 1

# sorted_list = merge_sort(new_list.head)

# print(sorted_list) # after: 1 -> 2 -> 3 -> 4 -> 5 -> 6

# tests

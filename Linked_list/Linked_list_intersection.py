from Linked_list.Singly_linked_list_class import ListNode, printLinkedList, merge_intersecting_lists

# Given 2 singly linked lists, return the node at their intersection, if any
def find_intersection(headA: ListNode, headB: ListNode) -> ListNode:
    curA, curB = headA, headB

    # Let us consider both the linked lists seperate instead of merged
    # if we can make both the linked Lists of equal length such that we reach the intersecting node at the same time while traversing both then we can easily find it
    # we will achieve this by adding List B after List A and adding List A after List B
    #   A: 1, 3, 4, 8, 7, 2, 6, 4,| 8, 7, 2 |
    #   B: 6, 4, 8, 7, 2, 1, 3, 4,| 8, 7, 2 |

    while curA != curB:
        if curA == None:
            curA = headB

        if curB == None:
            curB = headA

        curA = curA.next
        curB = curB.next

    return curA.value


headA, headB = merge_intersecting_lists([1, 3, 4], [6, 4], [8, 7, 2])       # Creates 2 linked Lists with items [1, 3, 4, 8, 7, 2] and [6, 4, 8, 7, 2] where the linked list from 8 is merged
print("Linked List A: ",  end=" ")
printLinkedList(headA)
print("")
print("Linked List B: ",  end=" ")
printLinkedList(headB)
print("")
print(f"Intersecting node: {find_intersection(headA, headB)}")

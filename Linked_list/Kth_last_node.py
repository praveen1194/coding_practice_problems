from Linked_list_class import ListNode, createLinkedList, printLinkedList

# remove the Kth last node from the end of a singly linked list
def remove(head: ListNode, k: int) -> None:
    tempNode = ListNode(-1)                 # we start from a dummy node before the actual linked list, in case the head node itself needs to be removed
    tempNode.next = head

    leader_cur = trailer_cur = tempNode     # we start traversing from teh dummy node. 
    
    for _ in range(k):                      #Both the leader and trailer cursor will have a distance of K
        leader_cur = leader_cur.next

    while leader_cur.next:
        leader_cur = leader_cur.next
        trailer_cur = trailer_cur.next

    trailer_cur.next = trailer_cur.next.next

    return tempNode.next

head = createLinkedList(1, 2, 4, 7, 3)

print("Input: ",  end=" ")
printLinkedList(head)
print("")
print("Output: ",  end=" ")
printLinkedList(remove(head, 2))
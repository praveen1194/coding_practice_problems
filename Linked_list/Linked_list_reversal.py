from Linked_list_class import ListNode, createLinkedList, printLinkedList

# Reverse a singly linked list
def reverse(head: ListNode) -> ListNode:
    if not head:
        return None

    previous_node = None
    cur_node = head

    while(head is not None):
        cur_node = cur_node.next
        head.next = previous_node
        previous_node = head
        head = cur_node

    return previous_node

head = createLinkedList(1, 2, 4, 7, 3)

print("Input: ",  end=" ")
printLinkedList(head)
print("")
print("Output: ",  end=" ")
printLinkedList(reverse(head))


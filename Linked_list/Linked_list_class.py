from typing import List

class ListNode:

    def __init__(self, value):
        self._value = value
        self._next = None

    @property
    def value(self):
        return self._value
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, node):
        self._next = node

def printLinkedList(head: ListNode) -> None:
    cursor = head
    while(cursor is not None):
        print(cursor.value,  end=" ")
        cursor = cursor.next


def createLinkedList(*nums):
    if not nums:
        return None

    head = ListNode(nums[0])

    curNode = head
    for i in range(1, len(nums)):
        nextNode = ListNode(nums[i])
        curNode.next = nextNode
        curNode = nextNode

    return head


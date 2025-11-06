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

def merge_intersecting_lists(A: List, B: List, mergedSubList: List):

    headA = curA = ListNode(A[0])
    headB = curB = ListNode(B[0])

    for i in range(1, len(A)): 
        curA.next = ListNode(A[i])
        curA = curA.next

    for i in range(1, len(B)): 
        curB.next = ListNode(B[i])
        curB = curB.next

    curA.next = curB.next = ListNode(mergedSubList[0])
    curA = curA.next
    for i in range(1, len(mergedSubList)): 
        curA.next = ListNode(mergedSubList[i])
        curA = curA.next

    return headA, headB
    

def create_intersecting_lists(A: List, B: List):
    longer_list = shorter_list = None
    merged = False

    if len(A) >= len(B):
        longer_list = A
        shorter_list = B
    elif len(A) < len(B):
        longer_list = B
        shorter_list = A

    headA = curA = ListNode(shorter_list[0])
    
    if shorter_list[0] == longer_list[0]:
        headB = headA
        merged = True
    else:
        headB = curB = ListNode(longer_list[0])

    nodes = {shorter_list[0]: headA}

    for i in range(1, len(longer_list)):
        if i < len(shorter_list):
            curA.next = ListNode(shorter_list[i])
            curA = curA.next
            nodes[shorter_list[i]] = curA

        if not merged:
            if longer_list[i] in nodes:
                curB.next = nodes[longer_list[i]]
                merged = True
            else:
                curB.next = ListNode(longer_list[i])
                curB = curB.next

    return headA, headB
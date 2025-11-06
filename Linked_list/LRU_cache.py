from Doubly_linked_list_class import DoublyLinkedListNode

class LRUDoublyLinkedListNode(DoublyLinkedListNode):

    def __init__(self, key, value):
        self._key = key
        DoublyLinkedListNode.__init__(self, value)

    @property
    def key(self):
        return self._key

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._valueMap = {}
        self._head = LRUDoublyLinkedListNode(-1, -1)
        self._tail = LRUDoublyLinkedListNode(-1, -1)

    def get(self, key: int) -> int:
        if key not in self._valueMap:
            return -1
        
        self._valueMap[key].previous.next = self._valueMap[key].next
        self._valueMap[key].next.previous = self._valueMap[key].previous
        
        self._valueMap[key].next = self._head.next
        self._valueMap[key].previous = self._head
        self._head.next = self._valueMap[key]
        
        return self._valueMap[key].value


    def put(self, key: int, value: int) -> None:
        if key in self._valueMap:
            self._valueMap[key].previous.next = self._valueMap[key].next
            self._valueMap[key].next.previous = self._valueMap[key].previous
            del self._valueMap[key]

        if len(self._valueMap) == self._capacity:
            del self._valueMap[self._tail.previous.key]
            self._tail.previous = self._tail.previous.previous
            self._tail.previous.next = self._tail
        
        newNode = LRUDoublyLinkedListNode(key, value)

        if len(self._valueMap) == 0:
            self._tail.previous = newNode
            newNode.next = self._tail

            self._head.next = newNode
            newNode.previous = self._head

        else:
            self._head.next.previous = newNode
            newNode.next = self._head.next
            newNode.previous = self._head
            self._head.next = newNode

        

        self._valueMap[key] = newNode

cache = LRUCache(3)
cache.put(1, 100)
cache.put(2, 250)
print(cache.get(2))
cache.put(4, 300)
cache.put(3, 200)
print(cache.get(4))
print(cache.get(1))
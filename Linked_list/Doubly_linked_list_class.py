class DoublyLinkedListNode:

    def __init__(self, value):
        self._value = value
        self._next = None
        self._previous = None
    
    @property
    def value(self):
        return self._value
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, node):
        self._next = node 

    @property
    def previous(self):
        return self._previous
    
    @previous.setter
    def previous(self, node):
        self._previous = node 
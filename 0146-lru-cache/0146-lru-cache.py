
class ListNode:
    def __init__(self,key=None,val=None):
        self.key = key
        self.val = val 
        self.next = None
        self.prev = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail 
        self.tail.prev = self.head 
    def get(self, key: int) -> int:
        if key not in self.cache:return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add(self,node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node 

    def put(self, key: int, value: int) -> None:
            if key in self.cache:
                old = self.cache[key]
                self.remove(old)
            new = ListNode(key,value)
            self.cache[key] = new 
            self.add(new)

            if len(self.cache) > self.capacity:
                deleted_node = self.head.next
                self.remove(deleted_node)
                del self.cache[deleted_node.key]




            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
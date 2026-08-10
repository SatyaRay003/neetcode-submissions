class ListNode:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        # Empty
        if self.head is None:
            return -1

        counter = 0
        current_node = self.head
        while counter<index and current_node.next_node:
            current_node = current_node.next_node
            counter += 1

        # Index out of range
        if counter!=index:
            return -1

        return current_node.value


    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)

        new_node.next_node = self.head
        self.head = new_node

        if not self.tail:
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
           

    def remove(self, index: int) -> bool:
        # Empty
        if self.head is None:
            return False

        # Remove Head
        if index==0:
            self.head = self.head.next_node

            if self.head is None:
                self.tail = None

            return True

        # Find the node which is previous to removal node
        counter = 0
        current_node = self.head
        while current_node.next_node and counter<index-1:
            current_node = current_node.next_node
            counter += 1

        # Index doesn't exist
        if current_node.next_node is None:
            return False

        # Change the reference
        node_to_be_removed = current_node.next_node
        current_node.next_node = node_to_be_removed.next_node

        # If Tail removal
        if node_to_be_removed.next_node is None:
            self.tail = current_node

        return True

    def getValues(self) -> List[int]:
        current_node = self.head
        values = []
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next_node
            
        return values

        

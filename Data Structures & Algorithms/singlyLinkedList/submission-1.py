class LinkedList:
    
    def __init__(self):
        self.ll=[]
    
    def get(self, index: int) -> int:
        if index<len(self.ll):
            return self.ll[index]
        return -1

    def insertHead(self, val: int) -> None:
        self.ll.insert(0, val)
        

    def insertTail(self, val: int) -> None:
        self.ll.insert(len(self.ll), val)
        

    def remove(self, index: int) -> bool:
        if index<len(self.ll):
            self.ll.pop(index)
            return True
        return False
        

    def getValues(self) -> List[int]:
        return [i for i in self.ll]




        

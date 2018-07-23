class Element(Object):
    def __init__(self,value):
        self.value = value
        self.next = None    

class LinkedList(Object):
    def __init__(self,head = None):
        self.head = head

#If the LinkedList already has a head, iterate through the next reference in every Element until you reach the end of the list.
# Set next for the end of the list to be the new_element. Alternatively, if there is no head already, you should just assign new_element to it and do nothing else.
    def append(self,new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
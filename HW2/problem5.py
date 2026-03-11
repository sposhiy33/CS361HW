"""
CS361 - HW2
Problem 5 - Merge Two Sorted Linked Lists
Author @Shrey Poshiya
"""

# helper classes for the linked list 
class Node:
    def __init__(self, value): 
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def build_list(self, arr):
        for value in arr:
            self.insert(value)

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            # travese the linked list
            while current.next is not None:
                current = current.next

            # add new node
            current.next = new_node

    def printList(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

def mergeLists(list1, list2):
    
    # initialize a new linked list:
    merged_list = LinkedList()

    # traverse the two lists
    current1 = list1.head
    current2 = list2.head

    # similar logic to merge sort: compare the values and 
    # add smaller value to list
    # end traverasal when one of the lists is fully traversed
    while (current1 is not None) and (current2 is not None):
        if current1.value < current2.value:
            merged_list.insert(current1.value)
            print(f"inserting {current1.value} from list1")
            current1 = current1.next
        else:
            merged_list.insert(current2.value)
            print(f"inserting {current2.value} from list2")
            current2 = current2.next

    # if any elements missed, add them to final list 
    while (current1 is not None):
        merged_list.insert(current1.value)
        current1 = current1.next

    while (current2 is not None):
        merged_list.insert(current2.value)
        current2 = current2.next

    return merged_list

def main():

    list1 = [1,2,4]
    list2 = [1,3,4]

    list1_linked = LinkedList()
    list2_linked = LinkedList()

    list1_linked.build_list(list1)
    list2_linked.build_list(list2)

    merged_list = mergeLists(list1_linked, list2_linked)
    merged_list.printList()

if __name__ == "__main__":
    main()

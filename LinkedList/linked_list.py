from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value: Optional[Node]):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value: Optional) -> bool:
        """
        Append node to end of LL
        A -> B -> C -> None
        A -> B -> C -> D -> None

        Constant time O(1)
        No matter how large the linked list is, the number of operations taken to execute append remains constant
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
        self.length += 1
        return True

    def pop(self) -> Optional[Node]:
        """
        Pop node from end of LL
        A -> B -> C -> D -> None
        A -> B -> C -> None

        Linear time O(n)
        An algorithm with a single loop that iterates through all n items in the worst case has a time complexity of O(n)
        """
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value: Optional):
        """
        Prepend node to LL

        B -> C -> D -> None
        A -> B -> C -> D -> None

        Constant time O(1)
        ...
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first_node(self) -> Optional[Node]:
        """
        Remove first node

        A -> B -> C -> D -> None
        B -> C -> D -> None

        Constant time O(n)
        ...
        """
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get_by_index(self, index: int) -> Optional[Node]:
        """
        Return and node with index of n
        A -> B -> C -> D -> None
        1 -> 2 -> 3 -> 4 -> None

        Linear time O(n)
        """
        if 0 > index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index: int, value: Optional):
        temp = self.get_by_index(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index: int, value: Optional):
        if not (0 <= index <= self.length):
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get_by_index(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

        return True

    def remove(self, index) -> Optional[Node]:
        if not (0 <= index <= self.length):
            return None
        if index == 0:
            return self.pop_first_node()
        if index == self.length - 1:
            return self.pop()
        prev = self.get_by_index(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self, ):
        """
        A -> B -> C -> D -> None
        None <- D <- C <- B <- A

        O(n)

        """
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

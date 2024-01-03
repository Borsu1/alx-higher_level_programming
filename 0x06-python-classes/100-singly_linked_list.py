#!/usr/bin/python3
class Node:
    """
    This is a class for defining a node of a singly linked list.

    Attributes:
        __data (int): The data held by the node. It's a private attribute.
        __next_node (Node): The next node in the list. It's a private attribute.

    Methods:
        data: A property that gets or sets the data of the node.
        next_node: A property that gets or sets the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        The constructor for the Node class.

        Parameters:
            data (int): The data to be held by the node.
            next_node (Node, optional): The next node in the list. Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        The data property.

        Returns:
            int: The data held by the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        The data property setter.

        Parameters:
            value (int): The data to be held by the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        The next_node property.

        Returns:
            Node: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        The next_node property setter.

        Parameters:
            value (Node): The next node in the list.

        Raises:
            TypeError: If next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    This is a class for defining a singly linked list.

    Attributes:
        __head (Node): The first node in the list. It's a private attribute.

    Methods:
        sorted_insert(value): Inserts a new Node into the correct sorted position in the list.
    """

    def __init__(self):
        """
        The constructor for the SinglyLinkedList class.
        """
        self.__head = None

    def __str__(self):
        """
        The function to print the entire list.

        Returns:
            str: The entire list with one node number per line.
        """
        values = []
        node = self.__head
        while node is not None:
            values.append(str(node.data))
            node = node.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """
        The function to insert a new Node into the correct sorted position in the list.

        Parameters:
            value (int): The data to be held by the new node.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node

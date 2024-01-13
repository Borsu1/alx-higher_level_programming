#!/usr/bin/python3
"""This is a class for defining a node of a singly linked list."""


class Node:
    """
    This class represent a node class.
    Attributes:
        __data (int): The data held by the node. It's a private attribute.
        __next_node (Node): Next list node. It's a private attribute.

    Methods:
        data: A property that gets or sets the data of the node.
        next_node: A property that gets or sets the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Parameters:
            data (int): The data to be held by the node.
            next_node (Node, optional): Next list node. Defaults to None.

        Raises:
        TypeError: Ensure data is an integer and next_node is a Node instance.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Returns:
            int: The data held by the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
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
        Returns:
            Node: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
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
    Attributes:
        __head (Node): The first node in the list. It's a private attribute.

    Methods:
        sorted_insert(value): Inserts a new Node into the correct sorted list.
    """

    def __init__(self):
        """
        The constructor for the SinglyLinkedList class.
        """
        self.__head = None

    def __str__(self):
        """
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

#!/usr/bin/python3

"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Returns a list in sorted ascending order."""
        return sorted(self)


def test_my_list():
    my_list = MyList()

    # Test instantiation
    assert isinstance(my_list, MyList), "my_list is not an instance of MyList"

    # Test inherits from list
    assert isinstance(my_list, list), "my_list does not inherit from list"

    # Test __str__
    my_list.append(1)
    assert str(my_list) == '[1]', "__str__ does not return expected string"

    # Test append
    my_list.append(2)
    assert my_list == [1, 2], "append does not add element to list"

    # Test print_sorted
    my_list.append(3)
    print(my_list.print_sorted())  # Should print: [1, 2, 3]
    assert my_list.print_sorted() == [1, 2, 3], (
            "print_sorted does not return sorted list"
            )

    # Test print_sorted with negative number
    my_list.append(-1)
    print(my_list.print_sorted())  # Should print: [-1, 1, 2, 3]
    assert my_list.print_sorted() == [-1, 1, 2, 3], (
            "print_sorted does not return sorted list"
            )

    # Test print_sorted with empty list
    empty_list = MyList()
    print(empty_list.print_sorted())  # Should print: []
    assert empty_list.print_sorted() == [], (
            "print_sorted does not return empty list"
            )


test_my_list()

"""
Test file
"""


def ll_is_circular(head):
    """
    Is a Linked List circular
    """

    curr_node = head.next

    # Iterating through LL
    while (
        curr_node.next is not None and
        curr_node != head
    ):
        curr_node = curr_node.next

    return curr_node == head



class Node:
    """
    Linked List Class
    """

    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":

    # Created LL
    head_node = Node(0)
    curr_node = head_node
    for number in range(1, 10):
        next_node = Node(number)
        curr_node.next = next_node
        curr_node = next_node

    # Make LL circular
    curr_node.next = head_node

    print(
        "Linked is circular: "
        f"{ll_is_circular(head_node)}"
    )


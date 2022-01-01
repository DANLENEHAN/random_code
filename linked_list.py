"""
Test file
"""


def ll_is_circular(head):
    """
    Is a Linked List circular
    """

    nodes = set()
    curr_node = head

    # Iterating through LL
    while (
        curr_node is not None and
        curr_node not in nodes
    ):
        nodes.add(curr_node)
        curr_node = curr_node.next

    return curr_node in nodes


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
        if number %5 == 0:
            keep_node = curr_node
        curr_node = next_node

    # Make LL circular
    curr_node.next = keep_node

    print("Printing List:")
    node = head_node
    count = 1
    while (
        node.next and 
        count < 16
    ):
        print(f"curr node Data: {node.data}, ID: {id(node)}")
        node = node.next
        count += 1

    print(
        "Linked is circular: "
        f"{ll_is_circular(head_node)}"
    )


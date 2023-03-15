"""Merge a linked list into another linked list at alternate positions."""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_alternate(head1, head2):
    if not head1:
        return head2

    if not head2:
        return head1

    curr1 = head1
    curr2 = head2

    while curr1 and curr2:
        next_node1 = curr1.next
        next_node2 = curr2.next

        curr1.next = curr2
        curr2.next = next_node1

        curr1 = next_node1
        curr2 = next_node2

    return head1

# get user input to create the first linked list
arr1 = list(map(int, input("Enter the elements of the first linked list separated by spaces: ").split()))
head1 = Node(arr1[0])
curr = head1
for i in range(1, len(arr1)):
    curr.next = Node(arr1[i])
    curr = curr.next

# get user input to create the second linked list
arr2 = list(map(int, input("Enter the elements of the second linked list separated by spaces: ").split()))
head2 = Node(arr2[0])
curr = head2
for i in range(1, len(arr2)):
    curr.next = Node(arr2[i])
    curr = curr.next

# call the merge_alternate function on the linked lists
head1 = merge_alternate(head1, head2)

# print the resulting linked list
while head1:
    print(head1.data, end=" ")
    head1 = head1.next

"""Reverse a linked list in groups of given size"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_k(head, k):
    curr = head
    prev = None
    count = 0

    while curr and count < k:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        count += 1

    if next_node:
        head.next = reverse_k(next_node, k)

    return prev

# get user input to create the linked list
arr = list(map(int, input("Enter the elements of the linked list separated by spaces: ").split()))
k = int(input("Enter the size of the groups to reverse: "))
head = Node(arr[0])
curr = head
for i in range(1, len(arr)):
    curr.next = Node(arr[i])
    curr = curr.next

# call the reverse_k function on the linked list
head = reverse_k(head, k)

# print the resulting linked list
while head:
    print(head.data, end=" ")
    head = head.next

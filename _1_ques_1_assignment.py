"""Delete the elements in an linked list whose sum is equal to zero"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_zero_sum(head):
    if not head:
        return None

    dummy = Node(0)
    dummy.next = head
    prefix_sum = {0: dummy}

    curr = head
    sum_so_far = 0

    while curr:
        sum_so_far += curr.data

        if sum_so_far in prefix_sum:
            node_to_remove = prefix_sum[sum_so_far].next
            curr_sum = sum_so_far
            while node_to_remove != curr:
                curr_sum += node_to_remove.data
                del prefix_sum[curr_sum]
                node_to_remove = node_to_remove.next

            prefix_sum[sum_so_far].next = curr.next

        else:
            prefix_sum[sum_so_far] = curr

        curr = curr.next

    return dummy.next

# get user input to create the linked list
arr = list(map(int, input("Enter the elements of the linked list separated by spaces: ").split()))
head = Node(arr[0])
curr = head
for i in range(1, len(arr)):
    curr.next = Node(arr[i])
    curr = curr.next

# call the delete_zero_sum function on the linked list
head = delete_zero_sum(head)

# print the resulting linked list
while head:
    print(head.data, end=" ")
    head = head.next

"""Move all the negative elements to one side of the array"""

def move_negatives(arr):
    neg_idx = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i], arr[neg_idx] = arr[neg_idx], arr[i]
            neg_idx += 1
    return arr

# get user input to create the array
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

# call the move_negatives function on the array
new_arr = move_negatives(arr)

# print the new array with negatives on one side
print("The new array with all negative elements on one side is:", new_arr)

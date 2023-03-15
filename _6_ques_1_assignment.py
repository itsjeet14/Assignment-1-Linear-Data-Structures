"""Find the Kth largest and Kth smallest number in an array"""

def find_kth_largest_smallest(arr, k):
    arr.sort()
    kth_largest = arr[-k]
    kth_smallest = arr[k-1]

    return kth_largest, kth_smallest

# get user input to create the array and the value of k
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
k = int(input("Enter the value of k: "))

# call the find_kth_largest_smallest function on the array and k
kth_largest, kth_smallest = find_kth_largest_smallest(arr, k)

# print the kth largest and kth smallest numbers
print("The", k, "th largest number in the array is:", kth_largest)
print("The", k, "th smallest number in the array is:", kth_smallest)

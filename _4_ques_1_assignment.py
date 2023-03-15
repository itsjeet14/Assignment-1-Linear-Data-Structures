"""In an array, Count Pairs with given sum"""

def count_pairs(arr, sum):
    count = 0
    seen = set()

    for num in arr:
        target = sum - num
        if target in seen:
            count += 1
        seen.add(num)

    return count

# get user input to create the array and the target sum
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
target_sum = int(input("Enter the target sum: "))

# call the count_pairs function on the array and target sum
pairs_count = count_pairs(arr, target_sum)

# print the number of pairs with the given sum
print("The number of pairs with sum", target_sum, "in the array is", pairs_count)

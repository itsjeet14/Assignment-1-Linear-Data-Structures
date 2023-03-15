"""Find duplicates in an array"""

def find_duplicates(arr):
    duplicates = set()
    seen = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return duplicates

# get user input to create the array
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

# call the find_duplicates function on the array
duplicates = find_duplicates(arr)

# print the duplicates
if not duplicates:
    print("There are no duplicates in the array.")
else:
    print("The duplicates in the array are:", end=" ")
    for duplicate in duplicates:
        print(duplicate, end=" ")

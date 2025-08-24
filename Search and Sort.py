# Task 1

my_list = [34, 29, 17, 91, 35, 30, 21, 13, 63, 34, 60, 23, 63, 39, 75, 90, 86, 13, 
           98, 64, 94, 80, 69, 82, 14, 35, 22, 15, 63, 82, 16, 53, 78, 15, 39, 87, 
           78, 16, 64, 48, 81, 63, 10, 18, 4, 51, 51, 95, 80, 61, 95, 28, 95, 39, 
           76, 45, 49, 23, 16, 86, 19, 41, 46, 3, 21, 50, 68, 36, 17, 61, 18, 21, 
           32, 17, 27, 40, 84, 1, 78, 50, 28, 24, 89, 74, 67, 2, 43, 3, 73, 79, 95, 
           47, 90, 46, 61, 61, 6, 64, 53, 100]

def linear_search(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return i
    return -1

target = int(input("Enter the number you'd like to look for (linear search): "))
index = linear_search(my_list, target)

if index != -1:
    print(f"Number found at index: {index} (linear search)")
else:
    print("Number not found (linear search).")

newlist = sorted(my_list)  # Create a sorted copy of my_list

def binary_search(newlist, target):
    left, right = 0, len(newlist) - 1
    while left <= right:
        mid = (left + right) // 2
        if newlist[mid] == target:
            return mid
        elif newlist[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

target = int(input("Enter the number you'd like to look for (binary search): "))
index = binary_search(newlist, target)

if index != -1:
    print(f"Number found at index: {index} (binary search)")
else:
    print("Number not found (binary search).")

#Task 2

task_2_list = [77, 43, 54, 39, 26, 16, 7, 10, 27, 18, 35, 54, 66, 45, 43, 54, 54, 71, 9, 39, 7, 3, 16, 48, 7, 24, 
               6, 19, 17, 61, 85, 28, 54, 100, 80, 34, 2, 65, 19, 84, 27, 61, 40, 34, 52, 42, 50, 66, 4, 58, 59, 
               90, 25, 40, 63, 15, 99, 99, 90, 10, 67, 31, 31, 57, 82, 83, 59, 70, 90, 53, 69, 12, 54, 39, 76, 63, 
               26, 75, 47, 71, 80, 68, 61, 34, 10, 70, 8, 85, 43, 15, 17, 100, 72, 83, 59, 74, 26, 71, 98, 81]

def bubble_sort(task_2_list):

    for n in range(len(task_2_list) - 1, 0, -1):

        for i in range(n):
            if task_2_list[i] > task_2_list[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                task_2_list[i], task_2_list[i + 1] = task_2_list[i + 1], task_2_list[i]

print("Unsorted list is:")
print(task_2_list)

bubble_sort(task_2_list)

print("Sorted list is:")
print(task_2_list)


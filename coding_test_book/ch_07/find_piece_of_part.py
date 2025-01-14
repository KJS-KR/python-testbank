pieces = 5
idxes = [8, 3, 7, 9, 2]

req_pieces = 3
req_idxes = [5, 7, 9]


def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2

    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


for req in req_idxes:
    if binary_search(idxes, req, 0, len(idxes) - 1):
        print("yes", end=" ")
    else:
        print("no", end=" ")

print()

for req in req_idxes:
    if req in idxes:
        print("yes", end=" ")
    else:
        print("no", end=" ")

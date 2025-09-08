def merge_sort(arr):
    # Base case: if array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Split array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original:", arr)
print("Sorted:", merge_sort(arr))

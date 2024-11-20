def main():

    arr = get_arr()

    final_arr = next_arr(arr)

    print(final_arr)

    # if num == nnum:
    #     print("This number is already the smallest one")
    # else:
    #     print(nnum)

def swapinarr(arr ,a, b):
    t = arr[a]
    arr[a] = arr[b]
    arr[b] = t


def next_arr(arr):

    # If already in descending order, no bigger number possible

    arr_len = len(arr)
    pivot = 0
    
    # Find rightmost pair where left digit is smaller than right digit
    for i in range(arr_len - 1, 0, -1):
        if arr[i] > arr[i - 1]:
            pivot = i - 1
            break

    # Find smallest digit on right that's greater than pivot
    smallest_greater = max(arr)
    swap_idx = pivot
    for i in range(pivot + 1, arr_len):
        if arr[i] > arr[pivot] and arr[i] <= smallest_greater:
            smallest_greater = arr[i]
            swap_idx = i

    # Swap pivot with next bigger digit
    swapinarr(arr, pivot, swap_idx)

    # Sort remaining digits in ascending order
    sorted_part = arr[pivot + 1:]
    sorted_part.sort()

    new_arr = arr[:pivot + 1] + sorted_part

    return new_arr


def get_arr():
    return eval(input("Enter a number arr: "))



if __name__ == "__main__":
    main()


def main():

    num = 315
    num = get_int()

    nnum = next_int(num)

    if num == nnum:
        print("This number is already the smallest one")
    else:
        print(nnum)

def numtoarr(num:int):
    str_n = str(num)
    num_arr = []
    for i in str_n:
        num_arr.append(int(i))
    return num_arr

def swapinarr(arr ,a, b):
    t = arr[a]
    arr[a] = arr[b]
    arr[b] = t

def get_final_int(arr):
    arr = [str(i) for i in arr]
    return int("".join(arr))

def next_int(n):
    arr = numtoarr(n)

    if sorted(arr ,reverse=True):
        return get_final_int(arr)


    arr_len = len(arr)
    pivot = 0
    for i in range(arr_len):
        index = arr_len - i - 1
        if i < arr_len - 1 and arr[index] < arr[index - 1] and arr[pivot] < arr[index - 1]:
            pivot = index - 1
    
    swapinarr(arr, pivot, pivot + 1)
    
    sorted_part = arr[pivot + 1:]
    sorted_part.sort(reverse=True)

    new_arr = arr[:pivot + 1] + sorted_part

    return get_final_int(new_arr)


def get_int():
    return int(input("Enter a number: "))



if __name__ == "__main__":
    main()

import random
import threading
import time
start_time = time.time()


def selection_sort(arr):
    for i in range(len(arr)):
        number = -1
        ind = 0
        for j in range(i, len(arr)):
            if arr[j] > number:
                number = arr[j]
                ind = j
        arr[ind] = arr[i]
        arr[i] = number
    return arr


def sort_list(lst):
    selection_sort(lst)
    return lst


if __name__ == "__main__":
    num_threads = 2
    thread_lists = []

    data1 = [random.randint(1, 1000) for _ in range(10)]
    data2 = [random.randint(1, 1000) for _ in range(10)]

    for _ in range(num_threads):
        thread_lists.append([data1, data2])

    start = 0
    end = len(thread_lists) - 1

    while start <= end:
        th1 = threading.Thread(target=sort_list, args=(thread_lists[start][0],))
        th2 = threading.Thread(target=sort_list, args=(thread_lists[end][1],))

        th1.start()
        th2.start()

        start += 1
        end -= 1

    th1.join()
    th2.join()

    sorted_list1 = thread_lists[0][0]
    sorted_list2 = thread_lists[-1][1]

    print(sorted_list1)
    print(sorted_list2)

    end_time = time.time()
    print(end_time - start_time)

# Время выполнения задачи
# 0.0009968280792236328
# 0.001001119613647461
# 0.0009961128234863281
# 0.0010001659393310547
# 0.0010018348693847656

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

    data1 = [random.randint(1, 1000) for _ in range(10000)]
    data2 = [random.randint(1, 1000) for _ in range(10000)]

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
# 3.5059897899627686
# 3.545060396194458
# 3.5488545894622803
# 3.5041120052337646
# 3.550469398498535

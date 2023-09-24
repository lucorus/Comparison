import random
import time
start = time.time()


def sort_selection(arr):
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


data1 = [random.randint(1, 1000) for _ in range(10000)]
data2 = [random.randint(1, 1000) for _ in range(10000)]

print(sort_selection(data1))
print(sort_selection(data2))

end = time.time()
print(end - start)

# Время выполнения задачи
# 3.5775256156921387
# 3.6148946285247803
# 3.5332701206207275
# 3.540168046951294
# 3.557704448699951


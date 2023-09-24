import random
import timeit
start_time = timeit.default_timer()


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


if __name__ == "__main__":
    data1 = [random.randint(1, 1000) for _ in range(10)]
    data2 = [random.randint(1, 1000) for _ in range(10)]

    print(sort_selection(data1))
    print(sort_selection(data2))

    end_time = timeit.default_timer()
    print(end_time - start_time)

# Время выполнения задачи
# 0.00007374412241144111
# 0.00006479999865405262
# 0.00005784124352344342
# 0.00005460000829771161
# 0.00005799997597932815

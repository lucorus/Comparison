import multiprocessing
import time
import random
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


if __name__ == '__main__':
    # создаём набор процессов, кол-вом 2
    pool = multiprocessing.Pool(processes=2)

    datas = [[random.randint(1, 1000) for _ in range(10000)] for _ in range(2)]

    # запускаем функцию selection_sort для каждого элемента в списке
    results = pool.map(selection_sort, datas)

    print(*results, sep='\n')
    end_time = time.time()
    print(end_time - start_time)


# Время выполнения задачи
# 2.2604501247406006
# 2.2580723762512207
# 2.3873188495635986
# 2.3569254875183105
# 2.185117721557617

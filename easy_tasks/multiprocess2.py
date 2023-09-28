from multiprocessing import Pool
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
    pool = Pool(processes=2)

    datas = [[random.randint(1, 1000) for _ in range(10)] for _ in range(2)]

    # запускаем функцию selection_sort для каждого элемента в списке
    results = pool.map(selection_sort, datas)

    print(*results, sep='\n')
    end_time = time.time()
    print(end_time - start_time)


# Время выполнения задачи
# 0.14261269569396973
# 0.1496443748474121
# 0.14466333389282227
# 0.14073944091796875
# 0.14543724060058594

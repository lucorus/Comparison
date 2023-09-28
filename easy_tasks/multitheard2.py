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


if __name__ == "__main__":
    # создаём списки для сортировки
    data1 = [random.randint(1, 1000) for _ in range(10)]
    data2 = [random.randint(1, 1000) for _ in range(10)]

    # создаём поток, указывая какую в нём функцию надо выполнять и какие аргументы брать
    th1 = threading.Thread(target=selection_sort, args=(data1,))
    th2 = threading.Thread(target=selection_sort, args=(data2,))

    # запускаем потоки
    th1.start()
    th2.start()

    # Когда первый поток достигает конца своего списка, он вызывает метод join(), чтобы дождаться завершения второго потока
    # Второй поток продолжает получать списки из своего собственного списка до тех пор, пока не достигнет конца своего списка
    th1.join()
    th2.join()

    print(data1)
    print(data2)

    end_time = time.time()
    print(end_time - start_time)

# Время выполнения задачи
# 0.0009968280792236328
# 0.001001119613647461
# 0.0009961128234863281
# 0.0010001659393310547
# 0.0010018348693847656

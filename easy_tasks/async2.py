import asyncio
import random
import time
start_time = time.time()


async def sort_selection(arr):
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


async def main():
    list1 = [random.randint(1, 1000) for _ in range(10)]
    list2 = [random.randint(1, 1000) for _ in range(10)]

    # создаём экземпляр цикла обработки событий
    # (благодаря ему функции работают одновременно в одном потоке, не останавливая другие корутины)
    loop = asyncio.get_event_loop()

    # запускаем функции
    await asyncio.gather(sort_selection(list1), sort_selection(list2))

    print(list1)
    print(list2)

    end = time.time()
    print(end - start_time)


if __name__ == "__main__":
    asyncio.run(main())

# Время выполнения задачи
# 0.0010001659393310547
# 0.0010135173797607422
# 0.00099945068359375
# 0.0009996891021728516
# 0.001007080078125

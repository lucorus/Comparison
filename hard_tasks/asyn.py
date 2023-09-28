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
    list1 = [random.randint(1, 1000) for _ in range(10000)]
    list2 = [random.randint(1, 1000) for _ in range(10000)]

    # создаём экземпляр цикла обработки событий
    # (благодаря ему функции работают одновременно в одном потоке, не останавливая другие корутины)
    loop = asyncio.get_event_loop()

    # превращает функции в асинхронные
    tasks = [
        asyncio.ensure_future(sort_selection(list1)),
        asyncio.ensure_future(sort_selection(list2)),
    ]

    # собираем функции из tasks и запускаем их
    await asyncio.gather(*tasks)

    print(list1)
    print(list2)

    end = time.time()
    print(end - start_time)


if __name__ == "__main__":
    asyncio.run(main())

# Время выполнения задачи
# 3.5295867919921875
# 3.5939383000077214
# 3.5026849000132643
# 3.537504000007175
# 3.5447382999991532

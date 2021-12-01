def binary_search(items, element):
    # Инициализация нижней границы
    low = 0

    # Инициализация верхней границы
    high = len(items) - 1

    # количество итераций
    i = 0

    # пока границы не встретятся
    while low <= high:
        print(f"{low}:{high}")
        i += 1

        # середина
        mid = (high + low) // 2

        # предполагаемый элемент
        guess_el = items[mid]

        # если нашли
        if guess_el == element:
            print("Iterations:", i)
            return mid
        # если элемент для поиска меньше, чем предполагаемый
        elif element < guess_el:
            high = mid - 1
        # если элемент для поиска больше, чем предполагаемый
        else:
            low = mid + 1
    print("Iterations:", i)
    return None


print("Index:", binary_search(list(range(1, 15)), 5))

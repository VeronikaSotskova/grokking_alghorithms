# поиск индекса наименьшего элемента
def find_smallest_index(lst: list) -> int:
    smallest_index = 0
    smallest = lst[smallest_index]

    for i in range(1, len(lst)):
        if smallest > lst[i]:
            smallest = lst[i]
            smallest_index = i
    return smallest_index


# сортировка выбором
def selection_sort(lst: list) -> list:
    new_lst = []

    for _ in range(len(lst)):
        smallest_index = find_smallest_index(lst)
        # добавляем наименьший элемент в новый список и удаляем его из входного списка
        new_lst.append(lst.pop(smallest_index))
    return new_lst


print(selection_sort([4, 32, 8, 1, 9, 1, 5, 8, 0]))

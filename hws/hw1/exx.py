def find_index(my_list: list, element: int) -> int:
    if element in my_list:
        return my_list.index(element)
    else:
        return -1
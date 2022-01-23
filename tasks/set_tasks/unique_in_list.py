"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая вернет уникальные элементы списка
"""


def get_unique_in_list(some_list: list) -> set:

    result = tuple(some_list)
    return set(result)


if __name__ == '__main__':
    assert get_unique_in_list([1, 2, 3, 1, 2, 4, 5]) == {1, 2, 3, 4, 5}
    print('Решено!')

"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
На сайте необходимо вывести количество страниц для перехода по ним.
Так как список страниц очень большой, то необходимо вывести первые три и
последние 3, а промежуточные заменить "..."

Написать функцию, которая принимает список и возвращает первые три и последние
три элемента
"""
pages = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]


def get_first_3_last_3(collection: list) -> tuple:

    first_3 = collection[:3]
    last_3 = collection[-3:]
    return first_3, last_3


if __name__ == '__main__':
    print("Приветствуем нас на нашем сайте!")
    print("Для навигации можете воспользоваться ссылками ниже")
    first, last = get_first_3_last_3(pages)
    print(f"{' '.join(first)} ... {' '.join(last)}")

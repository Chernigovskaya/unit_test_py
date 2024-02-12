# Создайте программу на Python или Java, которая принимает два списка чисел и выполняет следующие действия:
# a. Рассчитывает среднее значение каждого списка.
# b. Сравнивает эти средние значения и выводит соответствующее сообщение:
# - ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
# - ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
# - ""Средние значения равны"", если средние значения списков равны.

import pytest
class Average:
    def average(self, array: list[float]) -> float:
        return sum(array) / len(array)

    def comparison_averages(self, array1, array2):
        if len(array1) == 0 or len(array2) == 0:
            return 'есть пустой список'
        else:
            average_1 = self.average(array1)
            average_2 = self.average(array2)

        if average_1 < average_2:
            return 'Второй список имеет большее среднее значение'

        elif average_1 > average_2:
            return 'Первый список имеет большее среднее значение'

        else:
            return 'Средние значения равны'


class TestAverage:

    def test_empty_1(self):
        average = Average()
        assert average.comparison_averages([], [1, 2, 3]) == 'есть пустой список'

    def test_empty_2(self):
        average = Average()
        assert average.comparison_averages([1, 2, 3], []) == 'есть пустой список'

    def test_empty(self):
        average = Average()
        assert average.comparison_averages([], []) == 'есть пустой список'

    def test_first_greater(self):
        average = Average()
        result = average.comparison_averages([1, 2, 3], [1, 2])
        assert result == 'Первый список имеет большее среднее значение'

    def test_second_greater(self):
        average = Average()
        assert average.comparison_averages([1, 2, 3], [1, 2, 5]) == 'Второй список имеет большее среднее значение'

    def test_equal(self):
        average = Average()
        assert average.comparison_averages([1, 2, 3], [1, 2, 3]) == 'Средние значения равны'





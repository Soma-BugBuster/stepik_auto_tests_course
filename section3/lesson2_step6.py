"""Как можно проверить ожидаемый результат? Для этого используется встроенная в Python инструкция assert,
которая проверяет истинность утверждений. assert True не приводит к выводу дополнительных сообщений, а вот assert
False вызовет исключение AssertionError."""

"""Если условие не выполнено, то в консоли выводится лог ошибки с названием файла и номером строчки,
 в которой произошла ошибка, а также тип ошибки AssertionError"""

# assert abs(-42) == -42

# assert abs(-42) == -42, "Should be absolute value of a number"

"""в сообщении об ошибке всегда лучше выводить оба значения: то, которое ожидалось, и то, которое получили по факту"""
# def test_list_comparison():
#     # Фактический результат
#     actual_result = [1, 2, 3]
#
#     # Ожидаемый результат
#     expected_result = [1, 2, 3, 4]
#
#     # Сравнение
#     assert actual_result == expected_result, f"Тест провалился, поскольку фактический результат '{actual_result}' не "
#                                               f"соответствует ожидаемому '{expected_result}'."

"""Форматирование строк с помощью str.format"""
print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

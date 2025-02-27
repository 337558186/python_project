'''
Description: for循环
Author: duke0552
version: V1.0
Date: 2025-02-27 10:02:45
'''

# 简单的for循环遍历列表
def simple_for_loop():
    """
    简单的for循环遍历列表
    """
    numbers = [1, 2, 3, 4, 5]
    for number in numbers:
        print(number)

# 使用range函数的for循环
def for_loop_with_range():
    """
    使用range函数的for循环
    """
    for i in range(5):
        print(i)

# 遍历字典的for循环
def for_loop_with_dict():
    """
    遍历字典的for循环
    """
    student_scores = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
    for student, score in student_scores.items():
        print(f'{student}: {score}')

# 使用enumerate函数的for循环
def for_loop_with_enumerate():
    """
    使用enumerate函数的for循环
    """
    fruits = ['apple', 'banana', 'cherry']
    for index, fruit in enumerate(fruits):
        print(f'Index {index}: {fruit}')

# 嵌套for循环
def nested_for_loop():
    """
    嵌套for循环
    """
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for row in matrix:
        for element in row:
            print(element)

# 使用列表推导式的for循环
def list_comprehension_for_loop():
    """
    使用列表推导式的for循环
    """
    numbers = [1, 2, 3, 4, 5]
    squares = [number ** 2 for number in numbers]
    print(squares)
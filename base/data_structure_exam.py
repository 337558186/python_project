# 字典的基础用法
def dictionary_example():
    # 创建字典
    my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
    
    # 访问字典中的值
    name = my_dict['name']
    print(f"Name: {name}")
    
    # 修改字典中的值
    my_dict['age'] = 26
    
    # 添加新的键值对
    my_dict['email'] = 'alice@example.com'
    
    # 删除键值对
    del my_dict['city']
    
    # 遍历字典
    for key, value in my_dict.items():
        print(f"{key}: {value}")

# 元组的基础用法
def tuple_example():
    # 创建元组
    my_tuple = (1, 2, 3, 4, 5)
    
    # 访问元组中的值
    first_element = my_tuple[0]
    print(f"First element: {first_element}")
    
    # 元组是不可变的，不能修改元组中的值
    # my_tuple[0] = 10  # 这行代码会报错
    
    # 遍历元组
    for element in my_tuple:
        print(element)

# 列表的基础用法
def list_example():
    # 创建列表
    my_list = [1, 2, 3, 4, 5]
    
    # 访问列表中的值
    first_element = my_list[0]
    print(f"First element: {first_element}")
    
    # 修改列表中的值
    my_list[0] = 10
    
    # 添加新的元素
    my_list.append(6)
    
    # 删除元素
    my_list.remove(3)
    
    # 遍历列表
    for element in my_list:
        print(element)

# 集合的基础用法
def set_example():
    # 创建集合
    my_set = {1, 2, 3, 4, 5}
    
    # 添加元素到集合
    my_set.add(6)
    
    # 删除集合中的元素
    my_set.remove(3)
    
    # 检查元素是否在集合中
    if 2 in my_set:
        print("2 is in the set")
    
    # 遍历集合
    for element in my_set:
        print(element)

    # 数据类型转换的基础用法
    def type_conversion_example():
        # 整数转换为字符串
        num = 123
        num_str = str(num)
        print(f"Integer to string: {num_str} (type: {type(num_str)})")
                
        # 字符串转换为整数
        num_str = "456"
        num = int(num_str)
        print(f"String to integer: {num} (type: {type(num)})")
                
        # 字符串转换为浮点数
        float_str = "3.14"
        num_float = float(float_str)
        print(f"String to float: {num_float} (type: {type(num_float)})")
                
        # 列表转换为元组
        my_list = [1, 2, 3]
        my_tuple = tuple(my_list)
        print(f"List to tuple: {my_tuple} (type: {type(my_tuple)})")
                
        # 元组转换为列表
        my_tuple = (4, 5, 6)
        my_list = list(my_tuple)
        print(f"Tuple to list: {my_list} (type: {type(my_list)})")
                
        # 列表转换为集合
        my_list = [1, 2, 2, 3, 4]
        my_set = set(my_list)
        print(f"List to set: {my_set} (type: {type(my_set)})")
                
        # 集合转换为列表
        my_set = {5, 6, 7}
        my_list = list(my_set)
        print(f"Set to list: {my_list} (type: {type(my_list)})")
                
        # 字典的键转换为列表
        my_dict = {'a': 1, 'b': 2, 'c': 3}
        keys_list = list(my_dict.keys())
        print(f"Dictionary keys to list: {keys_list} (type: {type(keys_list)})")
                
        # 字典的值转换为列表
        values_list = list(my_dict.values())
        print(f"Dictionary values to list: {values_list} (type: {type(values_list)})")

    # 调用数据类型转换示例方法
    type_conversion_example()

# 调用示例方法
if __name__ == "__main__":
    dictionary_example()
    tuple_example()
    list_example()
    set_example()
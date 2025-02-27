def if_statement_example():
    # 如果条件为真，则执行以下代码块
    x = 10
    if x > 5:
        print("x 大于 5")

def if_else_statement_example():
    # 如果条件为真，则执行第一个代码块，否则执行第二个代码块
    x = 3
    if x > 5:
        print("x 大于 5")
    else:
        print("x 小于或等于 5")

def if_elif_else_statement_example():
    # 如果第一个条件为真，则执行第一个代码块，否则检查下一个条件
    # 如果第二个条件为真，则执行第二个代码块，否则执行最后的代码块
    x = 7
    if x > 10:
        print("x 大于 10")
    elif x > 5:
        print("x 大于 5 且小于或等于 10")
    else:
        print("x 小于或等于 5")

def nested_if_statement_example():
    # 嵌套的 if 语句
    x = 8
    if x > 5:
        if x < 10:
            print("x 大于 5 且小于 10")
        else:
            print("x 大于或等于 10")
    else:
        print("x 小于或等于 5")
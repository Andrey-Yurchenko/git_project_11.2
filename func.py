def foo():
    """
    вывод все заглавные
    """
    user_input = input()
    return user_input.upper()

def foo2():
    """
    вывод первые заглавные
    :return:
    """
    user_input = input()
    return user_input.title()

print(foo2())
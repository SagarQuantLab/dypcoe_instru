# def function_name():
#     pass

def my_decorator(func):
    def wrapper(*args, **kwargs):

        if not isinstance(args[0], int):
            raise ValueError("First input is not int")
        if not isinstance(args[1], int):
            raise ValueError("Second input is not integer")
        
        if len(kwargs) > 0:
            key_list = kwargs.keys()
            if not isinstance(kwargs[key_list[0]], int):
                raise ValueError("First position input is not integer")
            if not isinstance(kwargs[key_list[1]], int):
                raise ValueError("Second position input is not integer")
        else:
            kwargs.setdefault("third_num", 0)
            kwargs.setdefault("fourth_num", 0)
            
        
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def addition(first_num, second_num, third_num, fourth_num):
    sum = first_num + second_num + third_num + fourth_num
    return sum


sum = addition(2, 3)
# sum = addition('A', 3)
# sum = addition(2, 3, third_num=4, fourth_num=5)
sum = addition(2, 3, third_num='C', fourth_num=5)
print(sum)
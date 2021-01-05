# coding=<utf-8>

""" 
(ref1) https://youtu.be/HGOBQPFzWKo?t=11663
(ref2) https://github.com/python-engineer/python-engineer-notebooks/blob/master/advanced-python/13-Decoratos.ipynb
(ref3) https://www.python-engineer.com/courses/advancedpython/13-decorators/

[데코레이터]
- 합성함수를 예쁘게 덮어씌우는 방법 
"""
import functools


def start_end_decorator(func):
    
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper


def print_name():
    print('Alex')



def composite1(func1, func2):
    print_name = func1(func2)
    print_name()



@start_end_decorator
def composite_deco():
    print("Alex")


#############################

def start_end_decorator_3(func):
    
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper


@start_end_decorator_3
def add_5(x):
    return x + 5


#############################




if __name__ == "__main__": 

    composite1( start_end_decorator,  print_name )
    
    print(end="\n")

    composite_deco()

    print(end="\n")

    result = add_5(10)
    print(result)

    
    







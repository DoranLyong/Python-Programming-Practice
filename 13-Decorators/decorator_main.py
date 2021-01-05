# coding=<utf-8>

""" 
(ref1) https://youtu.be/HGOBQPFzWKo?t=11663
(ref2) https://github.com/python-engineer/python-engineer-notebooks/blob/master/advanced-python/13-Decoratos.ipynb
(ref3) https://www.python-engineer.com/courses/advancedpython/13-decorators/

[데코레이터]
- 합성함수를 예쁘게 덮어씌우는 방법 

1. function decorators 
2. class decorators 
"""
import functools


""" 1. function decorators

@mydecorator 
def dosomething():
    pass 


mydecorator 함수는 dosomething() 함수를 인수로 받아 
그 기능을 가져다 쓸 수 있다. 

함수의 이름을 다른 함수의 인수로 전달할 수 있는 이유는 
Python에서 함수 객체는 일등 시민(first-class citizen)으로 다루기 때문이다. 
"""

def start_end_decorator(func):
    
    def wrapper():
        
        print("Start deco")
        func()
        print("End deco")
    
    return wrapper     


def print_name():
    print("python_python")



@start_end_decorator
def print_name2():
    print("python_decorator")



def decorator_func(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("do something")
        result = func(*args, **kwargs)
        print("end something")
        return result

    return wrapper

@ decorator_func
def add5(x):
    return x + 5 




""" 2. class decorators

"""







if __name__ == "__main__": 

    # 데코레이터가 없다면... 
    print_name = start_end_decorator(print_name)
    print_name()


    # 데코레이터가 있다면... 
    print_name2()

    result = add5(15)
    print(result)



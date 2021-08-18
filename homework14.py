from functools import wraps
import re
from typing import Union


# task 1 Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
def logger(func):
    @wraps(func)
    def wrap(*args):
        print(f'{func.__name__} called with {args}')
        print(func(*args))
    return wrap


@logger
def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y


@logger
def square_all(*args: Union[int, float]) -> Union[int, float]:
    return [arg ** 2 for arg in args]


# task 2 Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
def stop_words(words: list):
    def insert_stop_words(func):
        @wraps(func)
        def wrap(name):
            result = func(name)
            results = ''
            for word in re.findall(r"[\w']+|[.,!?;]", result):
                if word in words:
                    results += ('* ')
                else:
                    results += (word + ' ')
            print(results)
        return wrap
    return insert_stop_words


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return (f"{name} drinks pepsi in his brand new BMW!")


# task 3 Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments: # max_length: 15 # type_: str # contains: [] - list of symbols that an argument
# should contain. If some of the rules' checks returns False, the function should return  False and print the reason
# it failed; otherwise, return the result.

def arg_rules(type_: type, max_length: int, contains: list):
    def check_rules(func):
        @wraps(func)
        def wrap(name):
            if type(name) != type_:
                print('incorrect type: should be string')
            if len(name) > max_length:
                print('incorrect length: should not be more than 15')
            if list not in contains:
                print("incorrect name: should contain ['05' and'@']")
            else:
                print('everything is correct')
                return func(name)
        return wrap
    return check_rules


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

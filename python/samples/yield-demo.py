# -*- coding:utf-8 -*-
# Example for usage of yield
# @author Tang Ling
# @email tangling.life@gmail.com

def yield_demo():
    """Yield demo
    """
    n = 0
    while n < 100 :
        n += 1
        yield n
def yield_demo1():
    """
    """
    i = 0 
    i = i + 1
    yield 'yield is ',i

def fib(max):
    n,a,b = 0,0,1
    while n < max :
        yield b
        a,b = b , a + b
        n = n + 1

if __name__ == '__main__':
    for n in fib(20):
        print n,



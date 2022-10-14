'''
Created on 2022/10/14

@author: t20cs050
'''
def fibo(n):
    if n == 0 or n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)
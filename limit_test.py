from random import random
from time import time

def bitwise_flags():
    bitwise_num = 0
    for k in range(3):
        for j in range(36000):
            bitwise_num &= ~(1 << j)
            if random() < 0.5:
                bitwise_num += 1 << j

def list_flags():
    big_list = [None]*36000
    for k in range(3):
        for j in range(36000):
            big_list[j] = False
            if random() < 0.5:
                big_list[j] = True

start = time()
bitwise_flags()
end = time()
print("Bitwise:", end-start)
start = time()
list_flags()
end = time()
print("List:", end-start)
# Huh... Expected bitwise to be faster, but list is faster.
#!/usr/bin/env python3

import itertools

def find_cont(arr):
     arrlen = len(arr)
     def cont_end(begin):
         count = itertools.count(arr[begin])
         for i in range(begin, arrlen):
             if next(count) != arr[i]:
                 return i
         return arrlen

     begin = 0
     while begin < arrlen:
         end = cont_end(begin)
         yield arr[begin:end] if end - begin > 1 else arr[begin]
         begin = end


if __name__ == '__main__':
    arr = [1,1,1,2,3,4,5,8,10,22,24,25,26,66]
    print(list(find_cont(arr)))


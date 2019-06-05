**链接**

[请教一道算法题，如下，谢谢](<https://segmentfault.com/q/1010000012007378/a-1020000018606430>)

**问题描述**

> 有一个数组[1,1,1,2,3,4,5,8,10,22,24,25,26,66]，
> 请写一个方法把数组变成[1,1,[1,2,3,4,5],8,10,22,[24,25,26],66]
> 就是把里面连续递增的数字归成一个数组，没思路，有没有好的方案？

**我的回答**

```python
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


arr = [1,1,1,2,3,4,5,8,10,22,24,25,26,66]         
print(list(find_cont(arr)))
```


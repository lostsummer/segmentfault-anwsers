**链接**

[求个随机整数的 算法](https://segmentfault.com/q/1010000017987193)

**问题描述**

> 从1到100的整数中随机10个，然后和为100的组合有哪些？

** 我的回答 **

```python
import itertools

"""
算法有两个重要的优化点:
    1. 组合中的最大BIGGEST有限制，也就是考虑前9个数和最小的情况
    2. 组合按生序排列的首元素有最大限制，首元素是我们递归试算的起始点
"""

BIGGEST = 100 - sum(range(1, 10))
MAX_HEAD = list(itertools.takewhile(lambda x:sum(x) <= 100, (range(1, 101)[i:i+10] for i in range(0, 100))))[-1][0]

def fetch(current, selected=[]):
    if current <= BIGGEST and len(selected) < 10:
        selected_ = selected + [current]
        sum_val = sum(selected_)
        n = len(selected_)
        if sum_val == 100 and n == 10:
            yield selected_
        elif sum_val < 100 and n < 10:
            for i in range(current+1, 100 - sum_val + 1):
                yield from fetch(i, selected_)
                
choices = [c for h in range(1, MAX_HEAD + 1) for c in fetch(h)]
for c in choices:
    print(','.join(str(i) for i in c))
```


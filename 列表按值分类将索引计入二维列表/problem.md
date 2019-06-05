**链接**

[Python：如何将列表中的数字进行分类排序，返回一个存放索引值的二维列表？](https://segmentfault.com/q/1010000017833429/a-1020000017897505)

**问题描述**

> 快速非支配排序问题
>
> 有下面两个列表：
> front = [[]]
> n = [2,1,0,2,3,0,0,1,2,5]
>
>先要将n中相同数值的索引，如n[1]=n[7]=1，n[9]=5进行归类排序，并存于front中
>
>结果：front = [[2,5,6],[1,7],[0,3,8],[4],[9]]



**我的回答**

```python
from collections import defaultdict
n = [2,1,0,2,3,0,0,1,2,5]
d = defaultdict(list)
for index, item in enumerate(n):
    d[item].append(index)
    
front = [d[i] for i in sorted(d)]
```


**链接**

[python中如何将三维列表转化为二维列表？](https://segmentfault.com/q/1010000018943256)

**问题描述**

A=[[[1,2],[1,3],[2,5]],[[2,4],[2,5],[2,6]],[[3,5],[3,6]]]
想转化为B=[[1,2],[1,3],[2,5],[2,4],[2,5],[2,6],[3,5],[3,6]]

**我的回答**

题目明确是三维数组还好办，
如果不确定每个元素的数组维度，需要做一个深度遍历
以下为python3代码：

```
def dfs(tree):
    for i in tree:
        if type(i) == list:
            yield from dfs(i)
        else:
            yield tree


B = list(dfs(A))
```
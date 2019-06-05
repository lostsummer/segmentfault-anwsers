**链接**

[两个list，如何判断A中的元素是否存在B的元素中](https://segmentfault.com/q/1010000019041939/a-1020000019124847)

**问题描述**

问题：
list_a = [key1,key2,key3...keyn]
list_b = ['1234343key1','weewqsfsdfkey2',........'lkadsadsadsa']

list_a，可以理解为一个关键字集合；
list_b，可以理解为一个长字符串集合，每个元素都比较长，可能包括list_a中元素，也可能不包括。

如何判断list_a中元素是否包含在list_b中。最常用的方法是双层for循环：

```
    for b in list_b:
        for a in list_a:
            if a in b:
                print(a)
```

这种方式的时间复杂度为O(m*n)，数据量大就GG。
所以求问比较快速的算法

**我的回答**

似乎大部分回答并没有解决时间复杂度问题，大家在考虑消减循环层次时忽略了字符串匹配本身的复杂度。
假设：

```
len(key) == 3
len(long_str1) == 10
len(long_str2) == 10
```

你们说下面哪组更耗时？
1.

```
key in long_str1
key in long_str2
```

2.

```
key in (long_str1 + long_str2)
```

想必大家心中有答案了，第1组匹配两个字符串要进行 (10-3)*2 轮比较，第2组是(10*2)-3轮，并且`long_str1 + long_str2`产生了新的子串，逻辑上是错误的。

楼主的问题到底有没有更低时间复杂度的解决方法，我觉得有，但要牺牲空间。
最坏情况下，list_b中的每个long_str元素，都要做n次 `key in long_str` 判断，n越大，耗时就越可观；反过来说同样，key要同每个long_str做`for key in long_str`操作...

预先把所有的long_str的所有子串放入哈希表，就能把一个遍历list_b并逐个字串匹配key的计算，缩减到复杂度为O(1)的哈希查询操作。先做个准备 [python求字符串集的所有子串](https://segmentfault.com/q/1010000011783745)

看完上面链接的问题，你知道把list_b转换成一个哈希也不难（我们用set）

```
set_a = {s[i:j+1] for s in list_b for i in range(len(s)) for j in range(i, len(s))}
for i in list_a:
    if i in set_a:
        print(i)
```

因为对于每个long_str，都有其长度的**阶乘**个子串，所以这个set_a会很大。如果这个问题约束key是定长，那还好些
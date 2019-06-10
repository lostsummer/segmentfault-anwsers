**链接**

[python 中怎么对json数组按某个字段进行排序（这个字段是字母加数字）](https://segmentfault.com/q/1010000019265326)

**问题描述**

我有这样一个json数组

```
a = [
        {"id":863,"hostname":"hdfs"},
        {"id":822,"hostname":"admin"},
        {"id":865,"hostname":"Spark-1"},
        {"id":1074,"hostname":"Spark-10"},
        {"id":867,"hostname":"Spark-2"},
        {"id":1014,"hostname":"Spark-11"}
    ]
```

通过sort按 `hostname`字段排序

```
a.sort(key = lambda x:x["hostname"])
```
得到的是这样的结果`Spark-10` 在`Spark-2`前面

```
[
    {"id":822,"hostname":"admin"},
    {"id":863,"hostname":"hdfs"},
    {"id":865,"hostname":"Spark-1"},
    {"id":1074,"hostname":"Spark-10"},
    {"id":1014,"hostname":"Spark-11"},
    {"id":867,"hostname":"Spark-2"},

]
```

而我希望得到这样一个结果
```
[
    {"id":822,"hostname":"admin"},
    {"id":863,"hostname":"hdfs"},
    {"id":865,"hostname":"Spark-1"},
    {"id":867,"hostname":"Spark-2"},
    {"id":1074,"hostname":"Spark-10"},
    {"id":1014,"hostname":"Spark-11"}
]
```
 请问我改如何进行处理


**我的回答**

最简单的方法当然是把数字部分格式化比较，因为最根本的还是要基于字符串比较，而且出现数字的位置可能不定，要用好正则的分组。

假设数字部分最大位数为三位，可以把key函数写成这样 (py3)
```python3
import re

def keyFormat(x):
	def numberFormat(matched):
	    n = matched.group("number")
	    return f'{n:>03}'

	return re.sub('(?P<number>\d+)', numberFormat, x['hostname'])


a.sort(key=keyFormat)
```

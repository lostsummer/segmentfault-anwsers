#!/usr/bin/env python3

import re

a = [
        {"id":863,"hostname":"hdfs"},
        {"id":822,"hostname":"admin"},
        {"id":865,"hostname":"Spark-1"},
        {"id":1074,"hostname":"Spark-10"},
        {"id":867,"hostname":"Spark-2"},
        {"id":1014,"hostname":"Spark-11"}
    ]


def keyFormat(x):
    def numberFormat(matched):
        n = matched.group("number")
        return f'{n:>03}'

    return re.sub('(?P<number>\d+)', numberFormat, x['hostname'])


if __name__ == '__main__':
    a.sort(key=keyFormat)
    print(a)

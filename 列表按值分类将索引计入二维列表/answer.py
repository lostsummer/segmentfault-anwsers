#!/usr/bin/env python3

from collections import defaultdict
n = [2,1,0,2,3,0,0,1,2,5]
d = defaultdict(list)
if __name__ == '__main__':
    for index, item in enumerate(n):
        d[item].append(index)

    front = [d[i] for i in sorted(d)]
    print(front)

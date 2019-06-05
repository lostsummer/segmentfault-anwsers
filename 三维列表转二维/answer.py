#!/usr/bin/env python3

def dfs(tree):
    for i in tree:
        if type(i) == list:
            yield from dfs(i)
        else:
            yield tree

if __name__ == '__main__':
    A=[[[1,2],[1,3],[2,5]],[[2,4],[2,5],[2,6]],[[3,5],[3,6]]]
    B = list(dfs(A))
    print(B)


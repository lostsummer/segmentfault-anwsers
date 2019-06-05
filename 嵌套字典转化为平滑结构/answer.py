#!/usr/bin/env python

from collections import namedtuple
from collections.abc import Iterable

Node = namedtuple("Node", ["keys", "value"])
Node.__new__.__defaults__ = ((), None)

nested_json = {
        "a": 1,
        "b": [35, 26],
        "c": [{
                "d": [2, 3, 4],
                "e": [
                    {
                        "f": 1,
                        "g": 2
                        }
                    ]
            }],
        "h": {}
        }


def flattern(nested):
    def dfs(node):
        ks, nv = node
        if nv and isinstance(nv, Iterable):
            if type(nv) == list:
                kvs = enumerate(nv)
            elif type(nv) == dict:
                kvs = nv.items()
            for k, v in kvs:
                n = Node(keys=ks+(str(k),), value=v)
                yield from dfs(n)
        else:
            yield node

    root = Node(keys=(), value=nested)
    return {'.'.join(keys):value for keys, value in dfs(root)}


if __name__ == '__main__':
    print(flattern(nested_json))

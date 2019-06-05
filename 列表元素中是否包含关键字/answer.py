#!/usr/bin/env python3

list_a = ['key1','key2','key3']
list_b = ['1234343key1','weewqsfsdfkey2','lkadsadsadsa']

if __name__ == '__main__':
    set_a = {s[i:j+1] for s in list_b for i in range(len(s)) for j in range(i, len(s))}
    for i in list_a:
        if i in set_a:
            print(i)

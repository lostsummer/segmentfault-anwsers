#!/usr/bin/env python3

#!/usr/bin/env python3

from collections import defaultdict
from intervaltree import Interval, IntervalTree
from multiprocessing import Pool, JoinableQueue, Process


def intervalDict(filename):
    with open(filename, 'r') as f:
        d = defaultdict(list)
        r = (l.strip().split() for l in f)
        for i in r:
            y = (i[0], int(i[2]), int(i[3]))
            d[i[1]].append(y)
        for k, v in d.items():
            d[k] = IntervalTree(
                    Interval(s, e, u) for u, s, e in v)
        return d


def readQ(d, q):
    while True:
        b = q.get(block=True)
        q.task_done()
        for l in b.split('\n'):
            r = l.strip().split()
            try:
                flag = r[2]
            except IndexError:
                continue
            if flag == "gene":
                k, start, end, idname = r[0], int(r[3])-1, int(r[4])+1, r[-1]
                for s, e, u in d[k][start:end]:
                    print(u, idname)



def fileBlocks(filename, size):
    with open(filename, 'r') as f:
        block = f.read(size)
        while block:
            # 多按行读取一次，保证block中无截断行
            tail = f.readline()
            yield block+tail
            block = f.read(size)


def writeQ(filename, block_size, q):
    for b in fileBlocks(filename, block_size):
        q.put(b)
    q.join()

if __name__ == '__main__':
    d = intervalDict('1.txt')
    q = JoinableQueue(0)
    producer = Process(target=writeQ, args=('genemark.gff3', 1024*1024, q))
    customers = [Process(target=readQ, args=(d, q)) for i in range(8)]
    producer.start()
    [c.start() for c in customers]
    producer.join()
    [c.terminate() for c in customers]
    [c.join() for c in customers]

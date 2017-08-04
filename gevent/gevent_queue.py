"""
    Gevent.queue could be used as Blocking Queue
    queue.put_nowait() if queue is not full, put it immediate, else throw Full Exception
    queue.put() has a optional param block, if block is "True", put will block.
    Author: xiangtian.hu
    Date: 2017-8-4
"""

import gevent
from gevent.queue import Queue

tasks = Queue()


def worker(n):
    while not tasks.empty():
        task = tasks.get()
        print('Worker %s got task %s' % (n, task))
        gevent.sleep(0)

    print('Quitting time!')


def boss():
    for i in range(1,25):
        tasks.put_nowait(i)

gevent.spawn(boss).join()

gevent.joinall([
    gevent.spawn(worker, 'steve'),
    gevent.spawn(worker, 'john'),
    gevent.spawn(worker, 'nancy'),
])
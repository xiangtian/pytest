"""
    group using
    Author: xiangtian.hu
    Date: 2017-8-4
"""
import gevent
from gevent.pool import Group


def talk(msg):
    for i in range(3):
        print(msg)

g1 = gevent.spawn(talk, 'bar')
g2 = gevent.spawn(talk, 'foo')

group = Group()
group.add(g1)
group.add(g2)
group.join()




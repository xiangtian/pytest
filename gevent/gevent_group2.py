"""
    using group.map to get result.
    result from imap is in order(add order), imap_unordered has no order
    Author: xiangtian.hu
    Date: 2017-8-4
"""
from gevent import getcurrent
from gevent.pool import Group
group = Group()


def hello_from(n):
    print('Size of group %s' % len(group))
    print('Hello from Greenlet %s' % id(getcurrent()))
    return n

# Could use "imap" replace of map, imap return a iterable
x = group.map(hello_from, range(3))
print(type(x))
print(x)
"""
    Using AsyncResult to get Result from another thread
    async_result.get() will block util async_result.set is called.
    Author: xiangtian.hu
    Date: 2017-8-4
"""

import gevent
from gevent.event import AsyncResult

ar = AsyncResult()


def setter():
    """
    After 3 seconds set the result of a.
    """
    gevent.sleep(3)
    ar.set('Hello!')


def waiter():
    """
    After 3 seconds the get call will unblock after the setter
    puts a value into the AsyncResult.
    """
    print(ar.get())

gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
])
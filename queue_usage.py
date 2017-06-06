"""
    if not call queue.task_done, task_queue.join() will hang there
    So task_done should be called after one item get from the queue had been processed
"""
from queue import Queue
import threading


class Consumer(threading.Thread):
    def __init__(self, tasks):
        threading.Thread.__init__(self)
        self.queue = tasks

    def run(self):
        while True:
            # using queue empty to exit consumer
            if self.queue.empty():
                break
            task = self.queue.get()
            print(task)
            self.queue.task_done()


if __name__ == "__main__":
    task_queue = Queue()
    for i in range(6):
        task_queue.put(i)

    for i in range(5):
        t = Consumer(task_queue)
        t.start()

    task_queue.join()
    print("join called")


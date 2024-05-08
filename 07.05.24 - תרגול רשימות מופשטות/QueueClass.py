class Queue(object):
    def __init__(self):
        self._queue = list()
    def enqueue(self, data: object):
        self._queue.append(data)

    def is_empty(self):
        return len(self._queue is None)

    def dequeue(self) -> object:
        return self._queue.pop(0)

    def head(self):
        return self._queue.pe
    def print_q(self):
        for i in self._queue:
            print(i)

if __name__ == "__main__":
    def queue_negative(a: list):
        q = Queue()
        for i in a:
            if i < 0:
                q.enqueue(i)
        return q

    my_q = queue_negative([1, -2, 5, -8, 9])
    my_q.print_q()
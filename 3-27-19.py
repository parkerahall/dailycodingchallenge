import time
import datetime
import threading

lock = threading.Lock()
function_timestamps = {}

class ActThread(threading.Thread):
    def __init__(self, f, N, args):
        super(ActThread, self).__init__()
        self.f = f
        self.N = N
        self.args = args

    def run(self):
        now = datetime.datetime.now()
        lock.acquire()
        function_timestamps[self.f] = now
        lock.release()
        time.sleep(self.N / 1000.)
        lock.acquire()
        if function_timestamps[self.f] == now:
            self.f(self.args)
        lock.release()

def debounce(f, N):
    function_timestamps[f] = None
    def debounced_f(*args):
        act_thread = ActThread(f, N, args)
        act_thread.start()
    return debounced_f

f = debounce(lambda x: print(x), 1000)
for i in range(7):
    f(i)
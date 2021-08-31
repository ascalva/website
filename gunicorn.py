from multiprocessing import cpu_count
from os              import environ


def max_workers() :
    return cpu_count()

bind         = "0.0.0.0:" + environ.get("PORT", "5000")
max_requests = 1000
timeout      = 120
worker_class = "gevent"
workers      = int(environ.get("WORKER_NUM", max_workers()))
threads      = workers

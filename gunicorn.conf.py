"""
Gunicorn configuration. Picked up automatically when running `gunicorn config.wsgi`
from the project root. Every value can be overridden with an environment variable.

Railway runs one container per replica, so scale with WEB_CONCURRENCY (processes)
and GUNICORN_THREADS (threads per process) rather than adding replicas first.
"""

import multiprocessing
import os

bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"

# Workers: default to 2 x CPU + 1, capped so small Railway plans don't OOM.
_default_workers = min(multiprocessing.cpu_count() * 2 + 1, 4)
workers = int(os.environ.get("WEB_CONCURRENCY", _default_workers))
threads = int(os.environ.get("GUNICORN_THREADS", "2"))
worker_class = "gthread"

timeout = int(os.environ.get("GUNICORN_TIMEOUT", "30"))
graceful_timeout = 30
keepalive = 5

# Recycle workers periodically to avoid slow memory growth.
max_requests = int(os.environ.get("GUNICORN_MAX_REQUESTS", "1000"))
max_requests_jitter = 100

# Logs go to stdout/stderr so Railway captures them.
accesslog = "-"
errorlog = "-"
loglevel = os.environ.get("GUNICORN_LOG_LEVEL", "info")
access_log_format = '%(h)s "%(r)s" %(s)s %(b)s %(M)sms "%(f)s" "%(a)s"'

# Railway's proxy sits in front of the app; trust its X-Forwarded-* headers.
forwarded_allow_ips = "*"

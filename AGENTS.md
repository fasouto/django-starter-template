# AGENTS.md

Instructions for AI coding agents (Claude Code, Codex, Cursor, Copilot, etc.) working in this repository.
Humans: the same information is in `readme.md` in a friendlier order.

## What this is

A minimal, production-ready Django 5.2 LTS starter that deploys to [Railway](https://railway.com) with one click.
Python 3.13, PostgreSQL via psycopg 3, gunicorn, WhiteNoise for static files, `uv` for dependencies.
Keep it minimal: this is a template people build on, not an application.

## Commands

All commands run through `uv`. Never call `pip` or a bare `python`.

```bash
uv sync --dev                                  # install deps (creates .venv)
uv run python manage.py migrate                # apply migrations
uv run python manage.py runserver              # dev server on :8000
uv run pytest                                  # tests (pytest-django, --reuse-db is on)
uv run ruff check --fix . && uv run ruff format .   # lint + format; CI fails on either
uv run python manage.py makemigrations --check --dry-run   # CI fails if migrations are missing
SECRET_KEY=$(openssl rand -hex 32) ALLOWED_HOSTS=example.com \
  uv run python manage.py check --deploy --settings=config.settings.production
```

Local dev defaults to SQLite (`db.sqlite3`) via `.env`; copy `.env.example` to `.env` first.
`docker compose up` gives Django + Postgres 17 instead.

## Layout

```
apps/<name>/         Django apps. Import as `apps.<name>`, register as "apps.<name>".
config/settings/     base.py (shared) -> development.py / production.py
config/templates/    Project templates: base.html, 403/404/500.html, robots.txt
config/static/       Project static files (css/base.css, js/app.js, img/)
config/urls.py       Root URLconf; includes apps.base.urls, admin, /health/
gunicorn.conf.py     Production server config (workers, threads, logging, PORT)
railway.toml         Railway build/deploy: collectstatic at build, migrate pre-deploy
```

## Conventions

- **Adding an app:** `mkdir apps/myapp && uv run python manage.py startapp myapp apps/myapp`,
  then add `"apps.myapp"` to `INSTALLED_APPS` in `config/settings/base.py` and include its urls in `config/urls.py`.
  Set `name = "apps.myapp"` in its `AppConfig`.
- **Settings:** read configuration from environment variables with `env(...)` (django-environ).
  Never hardcode secrets. New production knobs go in `production.py` with a sensible default and a comment.
- **Templates:** extend `base.html`. App templates live in `apps/<name>/templates/<name>/`.
- **Tests:** pytest functions in `apps/<name>/tests.py` using the `client`, `admin_client`, `db` fixtures from pytest-django.
  Every new view gets at least a status-code test.
- **Style:** ruff with `E W F I UP B DJ S C4 SIM`, line length 120. Fix lint before finishing a task.
- **Dependencies:** `uv add <pkg>` / `uv add --dev <pkg>`. Commit the updated `uv.lock`.
- **Migrations:** commit them. Run `makemigrations` after model changes.
- **Do not** change the `sys.path`, reintroduce `requirements.txt`, or add a `Procfile`; Railway reads `railway.toml`.

## Railway deployment facts

- Builder is Railpack; it reads `.python-version` (3.13) and `uv.lock`.
- Build: `collectstatic`. Pre-deploy: `migrate`. Start: `gunicorn config.wsgi` (config in `gunicorn.conf.py`).
- Health check: `GET /health/` returns `{"status": "ok"}` and pings the database.
- Railway injects `DATABASE_URL`, `PORT`, and `RAILWAY_PUBLIC_DOMAIN`. Production settings add the public
  domain to `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` automatically. Custom domains must be added to both
  variables by hand (`CSRF_TRUSTED_ORIGINS` needs the `https://` prefix).
- Scale with `WEB_CONCURRENCY` (gunicorn processes) and `GUNICORN_THREADS` before adding replicas.
- The filesystem is ephemeral. Media uploads need a Railway Volume mounted at `public/media` or S3 via django-storages.
- Background jobs: add a second Railway service from the same repo with a different start command
  (e.g. a Celery worker) and a Redis service; do not run workers inside the web process.

## Definition of done

`uv run ruff check . && uv run ruff format --check . && uv run pytest` all pass, no missing migrations,
and `readme.md` is updated if behaviour visible to a template user changed.

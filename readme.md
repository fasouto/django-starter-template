<p align="center">
  <img src="config/static/img/django-pony.png" alt="Django Pony" width="80">
</p>

<h1 align="center">Django Starter Template</h1>

A production-ready Django 5.2 LTS starter template for [Railway](https://railway.com). Python 3.13, PostgreSQL, gunicorn, WhiteNoise, `uv`, CI included, and written so that both people and AI coding agents can build on it.

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/django-starter-template?referralCode=iZa9TM&utm_medium=integration&utm_source=template&utm_campaign=generic)

## Deploy to Railway

Click the button above to deploy this template. Railway will:

1. Create a new Django web service
2. Provision a PostgreSQL database
3. Set `DATABASE_URL` and `SECRET_KEY` automatically
4. Run migrations on deploy
5. Start the application with gunicorn

Your app will be live in under a minute.

### Environment variables

These are set automatically by Railway. Override them in your service settings if needed:

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Auto-generated |
| `DATABASE_URL` | PostgreSQL connection string | Provided by Railway |
| `ALLOWED_HOSTS` | Extra comma-separated hostnames | `.railway.app` + your Railway domain |
| `CSRF_TRUSTED_ORIGINS` | Extra full URLs for POST requests (e.g. `https://example.com`) | `https://<your Railway domain>` |
| `DJANGO_SETTINGS_MODULE` | Settings module | `config.settings.production` |
| `WEB_CONCURRENCY` | gunicorn worker processes | `min(2 x CPU + 1, 4)` |
| `GUNICORN_THREADS` | threads per worker | `2` |

Railway injects `RAILWAY_PUBLIC_DOMAIN`, and the production settings add it to `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` for you, so login, admin, and forms work on the generated `*.up.railway.app` domain with zero configuration.

**Custom domains:** add the domain to `ALLOWED_HOSTS` and `https://yourdomain.com` to `CSRF_TRUSTED_ORIGINS`. Without the latter, POST requests (login, admin, forms) return 403.

## Local Development

### Option A: uv (recommended)

Prerequisites: [Python 3.13+](https://python.org), [uv](https://docs.astral.sh/uv/getting-started/installation/)

```bash
git clone https://github.com/fasouto/django-starter-template.git
cd django-starter-template

# Install dependencies
uv sync --dev

# Set up environment
cp .env.example .env

# Run migrations and create admin user
uv run python manage.py migrate
uv run python manage.py createsuperuser

# Start development server
uv run python manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000). The admin panel is at [http://localhost:8000/admin/](http://localhost:8000/admin/).

```bash
# Run tests
uv run pytest

# Lint and format (CI enforces both)
uv run ruff check --fix .
uv run ruff format .
```

### Option B: Docker Compose

Prerequisites: [Docker](https://docs.docker.com/get-docker/)

```bash
git clone https://github.com/fasouto/django-starter-template.git
cd django-starter-template

cp .env.example .env

# Start Django + PostgreSQL 17
docker compose up

# In another terminal:
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

Open [http://localhost:8000](http://localhost:8000). Code changes reload automatically.

## Project Structure

```
.
├── .github/
│   ├── workflows/ci.yml     # Lint, tests on Postgres, deploy checks, migration check
│   └── dependabot.yml       # Weekly grouped dependency updates
├── AGENTS.md                # Instructions for AI coding agents (CLAUDE.md points here)
├── apps/
│   └── base/                # Default app (home page, health check, tests)
│       ├── templates/base/  # App templates
│       ├── tests.py         # Example tests
│       ├── urls.py
│       └── views.py
├── config/                  # Django project package
│   ├── settings/
│   │   ├── base.py          # Shared settings
│   │   ├── development.py   # Dev settings (DEBUG=True, SQLite)
│   │   └── production.py    # Production settings (Postgres, security)
│   ├── static/              # Project-level static files
│   │   └── css/base.css
│   ├── templates/           # Project-level templates (base.html, error pages)
│   ├── asgi.py
│   ├── urls.py
│   └── wsgi.py
├── docker-compose.yml       # Local dev with Docker (Django + Postgres)
├── Dockerfile.dev           # Dev container
├── gunicorn.conf.py         # Production server: workers, threads, logging, PORT
├── pyproject.toml           # Dependencies and tool config
├── railway.toml             # Railway deployment config
├── uv.lock                  # Locked dependencies
└── manage.py
```

## What's Included

- **[Django 5.2 LTS](https://docs.djangoproject.com/en/5.2/)**: supported until April 2028
- **[PostgreSQL](https://www.postgresql.org/)** via psycopg3, modern async-capable adapter
- **[WhiteNoise](https://whitenoise.readthedocs.io/)**: serve static files without nginx, with brotli compression
- **[django-environ](https://django-environ.readthedocs.io/)**: configure via environment variables and `.env` files
- **[Argon2](https://docs.djangoproject.com/en/5.2/topics/auth/passwords/#using-argon2-with-django)** password hashing (winner of the Password Hashing Competition)
- **Split settings** for separate development and production configurations
- **Health check** at `/health/`, returns JSON for Railway monitoring
- **Tuned gunicorn** (`gunicorn.conf.py`): threaded workers sized for Railway plans, access logs to stdout, proxy headers trusted, all overridable via env vars
- **Zero-config hosts on Railway**: `RAILWAY_PUBLIC_DOMAIN` feeds `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS`
- **GitHub Actions CI**: ruff, pytest against Postgres 17, `check --deploy`, and a missing-migrations check on every PR
- **Dependabot** for Python, Actions, and Docker base images
- **AGENTS.md**: commands, layout, and conventions for AI coding agents, so Claude Code, Codex, Cursor, or Copilot extend the project the right way
- **[django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/)**: SQL queries, templates, cache inspection (dev only)
- **[ruff](https://docs.astral.sh/ruff/)** for linting and formatting
- **[pytest](https://docs.pytest.org/) + [pytest-django](https://pytest-django.readthedocs.io/)** for testing

## Working with AI coding agents

The repo ships an `AGENTS.md` (with `CLAUDE.md` pointing at it) that tells agents how to run, test, lint, and deploy the project, plus the conventions to follow when adding apps, settings, or dependencies. Open the project in Claude Code, Codex, Cursor, or Copilot and ask for a feature; the agent gets the right commands and layout without you explaining the template first. CI runs the same checks the agent is told to run, so a green pull request means the change is deployable to Railway.

## Customization

### Adding a new app

```bash
mkdir apps/myapp
uv run python manage.py startapp myapp apps/myapp
```

Then add `"apps.myapp"` to `INSTALLED_APPS` in `config/settings/base.py`, set `name = "apps.myapp"` in the generated `AppConfig`, and include its URLs in `config/urls.py`. Apps are imported as `apps.myapp`.

### Replacing the CSS

The included `config/static/css/base.css` is minimal and framework-free. Replace it with Bootstrap, Tailwind, or any CSS framework you prefer.

### Adding Celery

Add `celery[redis]` to your dependencies, create `config/celery.py`, and add a Redis service to your Railway project or `docker-compose.yml`.

## License

MIT. See [LICENSE](LICENSE).

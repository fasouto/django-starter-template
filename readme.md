# django-starter-template

A production-ready Django 5.2 LTS starter template for [Railway](https://railway.com).

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/template/TODO)

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
| `ALLOWED_HOSTS` | Comma-separated hostnames | `.railway.app` |
| `CSRF_TRUSTED_ORIGINS` | Full URLs for POST requests (e.g. `https://myapp.up.railway.app`) | `[]` |
| `DJANGO_SETTINGS_MODULE` | Settings module | `config.settings.production` |

**Important:** If you add a custom domain, add it to both `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` (with `https://` prefix). Without `CSRF_TRUSTED_ORIGINS`, POST requests (login, admin, forms) will return 403.

## Local Development

### Option A: uv (recommended)

Prerequisites: [Python 3.12+](https://python.org), [uv](https://docs.astral.sh/uv/getting-started/installation/)

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

# Lint and format
uv run ruff check .
uv run ruff format .
```

### Option B: Docker Compose

Prerequisites: [Docker](https://docs.docker.com/get-docker/)

```bash
git clone https://github.com/fasouto/django-starter-template.git
cd django-starter-template

cp .env.example .env

# Start Django + PostgreSQL
docker compose up

# In another terminal:
docker compose exec web uv run python manage.py migrate
docker compose exec web uv run python manage.py createsuperuser
```

Open [http://localhost:8000](http://localhost:8000). Code changes reload automatically.

## Project Structure

```
.
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
├── pyproject.toml           # Dependencies and tool config
├── railway.toml             # Railway deployment config
├── uv.lock                  # Locked dependencies
└── manage.py
```

## What's Included

- **[Django 5.2 LTS](https://docs.djangoproject.com/en/5.2/)** — supported until April 2028
- **[PostgreSQL](https://www.postgresql.org/)** via psycopg3 — modern async-capable adapter
- **[WhiteNoise](https://whitenoise.readthedocs.io/)** — serve static files without nginx, with brotli compression
- **[django-environ](https://django-environ.readthedocs.io/)** — configure via environment variables and `.env` files
- **[Argon2](https://docs.djangoproject.com/en/5.2/topics/auth/passwords/#using-argon2-with-django)** — password hashing (winner of the Password Hashing Competition)
- **Split settings** — separate development and production configurations
- **Health check** — `/health/` endpoint returns JSON for Railway monitoring
- **[django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/)** — SQL queries, templates, cache inspection (dev only)
- **[ruff](https://docs.astral.sh/ruff/)** — linting and formatting
- **[pytest](https://docs.pytest.org/) + [pytest-django](https://pytest-django.readthedocs.io/)** — testing

## Customization

### Adding a new app

```bash
mkdir apps/myapp
uv run python manage.py startapp myapp apps/myapp
```

Then add `"myapp"` to `INSTALLED_APPS` in `config/settings/base.py`.

### Replacing the CSS

The included `config/static/css/base.css` is minimal and framework-free. Replace it with Bootstrap, Tailwind, or any CSS framework you prefer.

### Adding Celery

Add `celery[redis]` to your dependencies, create `config/celery.py`, and add a Redis service to your Railway project or `docker-compose.yml`.

## License

MIT — see [LICENSE](LICENSE).

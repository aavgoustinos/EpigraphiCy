# EpigraphiCy /(Developer README)

## Highlights

- Django 5-based web application
- Apps: `core`, `epigraphy`
- Uses `django-ckeditor`, `django-jazzmin` and `django-storages` (S3) for media/static management
- Templates located in `venetianinscriptions/templates`
- Static assets under `venetianinscriptions/static`

## Quick start (development)

These commands are for Windows PowerShell (default shell in this workspace).

1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

3. Set environment variables (at minimum)

```powershell
# $env:DJANGO_SETTINGS_MODULE = 'core.settings'
# $env:SECRET_KEY = 'replace-with-a-secret-key'
# $env:DEBUG = '1'
# If using a DB URL or AWS credentials, set them here as well
```

4. Apply migrations and create a superuser

```powershell
python manage.py migrate
python manage.py createsuperuser
```

5. Run the development server

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Production notes

- This project expects to be configurable for external storage (S3) via `django-storages` (boto3 present in `requirements.txt`).
- Ensure `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` and any AWS credentials (if used) are set in environment or a secure `.env` file.
- Collect static files before deploying: `python manage.py collectstatic --noinput`.
- Configure a production-ready WSGI/ASGI server such as Gunicorn/uvicorn behind a reverse proxy.

## Project structure (high level)

  - `rootfolder/` - Django project package
  - `core/` - project settings, wsgi/asgi
  - `epigraphy/` - main app: models, views, admin, migrations
  - `media/`, `static/`, `templates/` - assets and templates
  - `manage.py` - Django CLI entrypoint
  - `requirements.txt` - pinned Python dependencies


## Tests

Run tests with:

```powershell
python manage.py test
```


## License

See the `LICENSE` file in the repository root.

## Contact

Project maintainer: repository owner

---

This developer README provides quick practical steps to install and run the project locally. If you'd like, I can:

- Replace the main `README.md` with this content (I can do that if you want)
- Add a shorter `README.md` for the public site and keep the developer README separate
- Add a `docs/` folder with the original academic abstract and references

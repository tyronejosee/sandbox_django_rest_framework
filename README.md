# Sandbox: Django Rest Framework

```bash
python manage.py dumpdata hospital.Doctor --output=apps/hospital/fixtures/doctor_data.json
python manage.py loaddata apps/hospital/fixtures/doctor_data.json


python manage.py loaddata doctor_data
```

## Pre-commit

Install hooks

```bash
pre-commit install
```

Clean cache

```bash
pre-commit clean
pre-commit gc
```

Run pre-commit (local)

```bash
pre-commit run --all-files
```

Add commit

```bash
git add .
git commit -m "chore: tests for pre-commit hooks"
```

Run isort (global)

```bash
isort .
```

Combine migrations

```bash
python manage.py squashmigrations products 0001_initial 0002_alter_product_description
python manage.py migrate
```

## Packages

- [ ] django-split-settings
- [ ] django-allauth
- [ ] django-rest-auth
- [ ] django-braces (mixins)
- [ ] django-compressor
- [ ] django-countries
- [ ] django-crispy-forms
- [ ] django-db-mailer
- [ ] django-el-pagination
- [ ] django-extensions
- [ ] drf-extra-fields
- [ ] django-filters
- [ ] django-fsm
- [x] django-jet (DEPRECATED)
- [x] django-modeltranslation
- [ ] django-newsletter
- [ ] django-phonenumber-field
- [ ] django-push-notifications
- [ ] django-solo
- [ ] django-treebeard
- [ ] PyJWT
- [x] django-redis
- [ ] django-wkhtmltopdf
- [x] django-import-export
- [ ] sentry-sdk
- [x] django-ckeditor
- [ ] geopy
- [ ] django-rest-knox
- [x] drf-spectacular
- [x] easy-thumbnails
- [ ] django-oscar
- [ ] django-oscar-api
- [ ] django-oscar-invoices
- [ ] django-debug-toolbar
- [ ] pytest-django
- [ ] pytest-cov

## Favorites

- [x] django-ckeditor
- [x] Django MPTT

## Elasticsearch Commands

```bash

python manage.py search_index --create
python manage.py search_index --populate

```

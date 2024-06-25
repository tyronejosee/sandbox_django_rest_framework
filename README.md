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

## Favorites

- [x] Django MPTT

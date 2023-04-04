export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/


# pytest --cov --cov-report=html:coverage_re
pytest --cov . --ignore="./gunicorn_config.py"

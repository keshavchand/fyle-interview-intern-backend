export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/


pytest --cov ./core --cov-report=html:coverage_re
# pytest --cov ./core --ignore="./gunicorn_config.py"

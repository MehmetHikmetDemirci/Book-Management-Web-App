FROM python:3.9

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

ENV DJANGO_SETTINGS_MODULE=BookManagementSystem.settings

ENV PORT 8000
EXPOSE 8000

CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
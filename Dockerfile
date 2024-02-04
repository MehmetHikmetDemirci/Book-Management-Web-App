# Python resmi imajını temel alarak başla
FROM python:3.9

# Çalışma dizinini ayarla
WORKDIR /app

# requirements.txt dosyanızı Docker image'ına kopyala
COPY requirements.txt ./

# requirements.txt'deki paketleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını container'a kopyala
COPY . .

# Statik dosyaları topla
RUN python manage.py collectstatic --noinput

ENV DJANGO_SETTINGS_MODULE=BookManagementSystem.settings

ENV PORT 8000
EXPOSE 8000

COPY entrypoint.sh ./
RUN chmod +x entrypoint.sh

# Gunicorn ile uygulamayı çalıştırma komutu
CMD ["./entrypoint.sh"]

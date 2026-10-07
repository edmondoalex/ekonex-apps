FROM python:3.12-slim-bookworm
LABEL io.hass.name="Ekonex Installer - Avvio" \
      io.hass.description="Configurazione iniziale GHCR" \
      io.hass.type="addon" \
      io.hass.version="0.1.0-test8" \
      io.hass.arch="amd64"
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY app.py /app/app.py
COPY static/ /app/static/
COPY logo.png /app/static/logo.png
CMD ["python", "/app/app.py"]

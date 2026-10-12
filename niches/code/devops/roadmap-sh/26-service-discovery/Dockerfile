# 26-service-discovery/Dockerfile - Run the built-in Python HTTP app
FROM python:3.12-slim-bookworm@sha256:782412e85d0f0984994c290652577d4018aff08145c85b262bb63dc0c7522254

# Copy only the app and run without root or package installs
WORKDIR /app
COPY src/app.py ./
USER 65532:65532
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
CMD ["python", "app.py"]

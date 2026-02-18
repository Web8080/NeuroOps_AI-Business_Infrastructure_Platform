# Build from repo root
FROM python:3.11-slim
WORKDIR /app
ENV PYTHONPATH=/app
COPY services/crm/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY services/crm .
COPY shared /app/shared
EXPOSE 8002
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]

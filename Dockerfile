# Stage 1: Builder
FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --user -r requirements.txt

# Stage 2: Production Image
FROM python:3.12-slim
WORKDIR /app

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY . .

EXPOSE 8000

ENTRYPOINT ["uvicorn", "src.main.web:app"]
CMD ["--host", "0.0.0.0", "--port", "8001"]

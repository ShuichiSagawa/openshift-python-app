FROM python:3.11-slim

WORKDIR /app

# 依存関係のインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードのコピー
COPY app.py .

# 非rootユーザーで実行
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8080

# Gunicornで起動
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:app"]
# demo-app 镜像
# 注意指令顺序：requirements.txt 先 COPY，这样代码改动不会破坏 pip 层缓存
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir flask==3.0.3

COPY app.py .

ENV APP_VERSION=1.0.0
EXPOSE 8000

CMD ["python", "app.py"]

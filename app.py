"""demo-app: 一个最小 Flask 应用，专门用于 Jenkins CI/CD 练习。

接口：
  GET /health  健康检查（部署验证用）
  GET /        首页，显示版本号
"""
from flask import Flask, jsonify

import os

APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"app": "demo-app", "version": APP_VERSION, "message": "Hello from Jenkins CI/CD!"})


@app.route("/health")
def health():
    # 练习「破坏性实验」时：把这里改成 return "", 500 就能模拟坏版本
    return jsonify({"status": "ok", "version": APP_VERSION})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

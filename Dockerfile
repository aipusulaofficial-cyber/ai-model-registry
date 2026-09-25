FROM python:3.12-slim
WORKDIR /app
COPY . .
CMD ["python","-c","from model_registry import Registry; print('model registry ready')"]

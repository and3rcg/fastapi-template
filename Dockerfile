FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN apt update && apt install -y --no-install-recommends build-essential
RUN pip install -r requirements.txt

RUN useradd -m nonroot
USER nonroot

COPY app /app

CMD ["fastapi", "run", "main.py", "--port", "8000"]

# example docker commands for building the image and running it:
    # docker build -t fastapi:v0.1 .
    # docker run -p 8000:8000 fastapi:v0.1

# Stage 1: Build
FROM python:3.8-alpine as build

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache build-base

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf ~/.cache/pip

WORKDIR /app
COPY . .

# Stage 2: Release
FROM python:3.8-alpine as release

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY --from=build /usr/local/lib/python3.8 /usr/local/lib/python3.8

WORKDIR /app
COPY --from=build /app .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
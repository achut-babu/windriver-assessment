# Instructions

## To Run App in Docker

### Build docker image

```bash
$ docker image build -t achut123/encrypt-decrypt:latest .
```

### Run App

```bash
$ docker run -p 5000:5000 achut123/encrypt-decrypt:latest
```

### Test APIs

#### 1. Health Check API

```bash
curl --location --request GET 'http://localhost:5000/api/health'
```

#### 2. Encrypt API

```bash
$ curl --location --request POST 'http://localhost:5000/api/encrypt' \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "input": "asdsaas"
  }'
```

#### 3. Decrypt API

```bash
$ curl --location --request POST 'http://localhost:5000/api/decrypt' \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "input": "YXNkc2Fhcw=="
  }'
```

### Run unit test and coverage report

```bash
$ docker run achut123/encrypt-decrypt:latest pytest tests.py
$ docker run achut123/encrypt-decrypt:latest coverage run tests.py
$ docker run achut123/encrypt-decrypt:latest coverage report
```

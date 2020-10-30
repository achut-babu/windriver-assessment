FROM python:3.8-alpine
ADD . /app/
WORKDIR /app
ENV PORT 5000
ENV FLASK_ENV development
RUN pip install -r requirements.txt
RUN apk add bash
CMD [ "/bin/bash", "./scripts/run", "python", "manage.py", "runserver", "--host", "0.0.0.0"]

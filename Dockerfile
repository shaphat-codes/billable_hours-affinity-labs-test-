FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /billable_hours

COPY requirements.txt /billable_hours

COPY . /billable_hours

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
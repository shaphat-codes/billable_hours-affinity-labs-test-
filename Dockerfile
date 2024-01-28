#setting base image
FROM python:3.8-alpine

#for logging
ENV PYTHONUNBUFFERED 1

#for not creating .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

#specifying our working directory
WORKDIR /billable_hours

#copying requirements.txt file to the working directory
COPY requirements.txt /billable_hours

#copying the content of the backend application into our Docker container.
COPY . /billable_hours

#the starting command for our container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
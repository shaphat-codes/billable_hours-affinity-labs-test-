# Billable hours project.
This is a web api that accepts  a timesheet (in csv format) as input and automatically 
generates invoices for each company.

## Installation
### Using Virtualenv
Install virtualenv if you don't have it already.
```bash
pip install virtualenv
```
Create virtual environment
```bash
virtualenv env
```
Activate virtual envvironment
```bash
./env/Scripts/activate
```
Run the Django server
```bash
python manage.py runserver
```

### Using Docker
Build the docker container
```bash
docker build -t billable_hours .
```
Run docker container
```bash
docker run -p 8000:8000 --name billable_hours_container billable_hours
```

## Tests
Tests were written using django tests (timetracking/tests.py)
To run tests, run the command below in the project's root directory
```bash
python manage.py test
```

## Sample response
![Local Image](./images/sample_response.jpg)

## API Testing
Click [here](https://www.postman.com/supply-specialist-10494686/workspace/affinity-labs/collection/26840405-457318da-fe47-4901-a3e7-ef89472d2fd3?action=share&creator=26840405) to test the endpoints in postman.

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
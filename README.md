# P2P Geeks
Mock Interview Scheduler
Final Project for Senior Design CS-4523 

## Testing Frontend

## Running the Project Locally

In order to try running this application locally on your computer, start
by forking or cloning the main branch of this repository within the desired
project directory on your local machine.

Then, create and start a virtual environment: <br />
`virtualenv env` <br /> 
`source env/bin/activate` <br />

Install the project dependencies: <br />
`pip install -r requirements.txt` <br />

Then run <br />
`python manage.py makemigrations` <br />
`python manage.py migrate` <br />

And now you should be able to start the development server and play with a local
version of P2P-Geeks (on localhost:8000) <br />
`python manage.py runserver` <br />
 
## Directory Structure
The main Django application folder is p2p_geeks.

The rest of the content is seperated as follows:
- apps (contains all backend components)
- static (images/css/js)
- templates (html)

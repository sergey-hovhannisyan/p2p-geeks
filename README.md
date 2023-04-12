# P2P Geeks
Mock Interview Scheduler

Final Project for Senior Design CS-4523 

## Install and run the project locally

In order to try running this application locally on your computer, start
by forking and cloning the main branch of this repository within the desired
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
`python manage.py runserver`
 
## Directory Structure

We are following recommended guidelines for a standard Django app. Our project directory is structured as follows:
- p2p_geeks/ (main Django app)
- apps/ (contains all Django modules for various backend features)
- templates/ (HTML)
- static/ (all static assets i.e css/js/images)
# P2P Geeks
Mock Interview Scheduler
Final Project for Senior Design CS-4523 

## _Testing Frontend_

## _Install and run the project locally_

In order to try running this application locally on your computer, start
by forking and cloning the main branch of this repository within the desired
project directory on your local machine. 

Then, create and start a virtual environment:

`virtualenv env`
`source env/bin/activate`

Install the project dependencies:
`pip install -r requirements.txt`

Then run

`python manage.py makemigrations`
`python manage.py migrate`

And now you should be able to start the development server and play with a local
version of P2P-Geeks (on localhost:8000)

`python manage.py runserver`
 
## _Understanding the Directory Structure_

The name of this project is P2P-Geeks as well as the top level directory. 
Using standard Django structuring conventions, our main application is
named after this directory as p2p_geeks.

All templates (HTML) are within the templates folder with their adjacent
assets (i.e CSS, JS, images) stored in the static folder. All sub 
applications for backend development can be found within the apps folder.
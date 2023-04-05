# p2p_geeks
Mock Interview Scheduler for CS-4523. 

# _Testing Frontend_

# _Install and run the project locally_

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
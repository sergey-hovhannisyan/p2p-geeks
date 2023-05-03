# P2P Geeks
Mock Interview Scheduler
Final Project for Senior Design CS-4523 

## Authors
- Sergey Hovhannisyan
- Sean Balakhanei
- Chenny Yun
- Arnav Kanwal

## Running the Project Locally

### Installation Prerequisites

Prerequisites for installation:
- Latest version of PostgreSQL (initialize a server and create a database named `p2pdb`)
- Python 3.8 or higher
- `pip install Django psycopg2`
- `pip install virtualenv`

### Project and Database Setup

Clone or fork the repository in the desired project folder destination on your local computer. <br />

Then, create and start a virtual environment (commands are slightly different for Windows users): <br />
`virtualenv env` <br /> 
`source env/bin/activate` <br /> 

You should see (env) on the side of you terminal prompt now. Leave this tab open.  

Install the project dependencies: <br />
`pip install -r requirements.txt` <br />

Open a new tab on your terminal and log into the database you created for Postgres. Run the following commands: <br />
`CREATE USER testuser WITH PASSWORD 'password';` <br />
`ALTER ROLE testuser SET client_encoding TO 'utf8';` <br />
`ALTER ROLE testuser SET default_transaction_isolation TO 'read committed';` <br />
`ALTER ROLE testuser SET timezone TO 'UTC';` <br />
`GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;` <br />

Go back to the terminal tab which should point to your project directory and have the virtual environment setup and active. Then type the following commands: <br />
`psql p2pdb -c "GRANT ALL ON ALL TABLES IN SCHEMA public to testuser;"` <br />
`psql p2pdb -c "GRANT ALL ON ALL SEQUENCES IN SCHEMA public to testuser;"` <br />
`psql p2pdb -c "GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to testuser;"` <br />


Then run <br />
`python manage.py makemigrations` <br />
`python manage.py migrate --run-syncdb` <br />

### Initialize the Database with test values

Create a superuser (administrator in Django) to manage your account. To do this, type:<br />
`python manage.py createsuperuser` <br />

After doing this, you should be able to start the development server and play with a local version of P2P-Geeks (localhost:8000): <br />
`python manage.py runserver` <br />

In your preferred browser, type localhost:8000/admin and hit enter. Sign into the administrator tab with your superuser credentials.
You should see all the tables listed within your database. 
<br />
Under categories, create two categories called "General" and "Resources". Then click on view site, and while navigating the website, go ahead 
and create at least 3 sample users in order to experiment with features such as network matching (connect). You are now ready to start using P2P-Geeks!
 
## Directory Structure
The main Django application folder is p2p_geeks.

The rest of the content is seperated as follows:
- apps (contains all backend components)
- static (images/css/js)
- templates (html)

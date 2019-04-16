##Requirements:
- Python 2.7
- mySql 5.7+

###To run the app follow these directions:

1. Clone the github repo (git clone https://github.com/slopezLf/feed_api).
2. cd into the appropriate directory (cd feed_api).
3. If you use virtualenv, set it up and activate.
4. Install python dependencies (pip install -r requirements.txt).
5. Initialize the db:
  - The `feed_api` database needs to be created before running the application: `mysql -h 127.0.0.1 --port 3306 -u root -ppassword -e "create database feed_api"`. You can go ahead and change the `user`, `password` and `host`, if those are different from the ones in the command. If this is the case, make sure to change them on `models/base.py` in the line that creates the database engine (`engine = create_engine('mysql+pymysql://root:password@localhost/feed_api')`).
  - Open a python shell.
  - Import the init function: `from models.base import init_db`. Make sure that virtualenv is acive and you are in the `feed_api` folder.
  - Run `init_db()`. 
6. Run the app `python app.py`

This will launch the flask server, which is currently configured to run on the local host (127.0.0.1:5000) and is also in debug mode.

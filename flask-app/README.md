# Flask Web App

##### Set the environment variables

Replace the values in **.env.example** with your values and rename this file to **.env**:

- `FLASK_APP`: Entry point of your application; should be `wsgi.py`.
- `FLASK_ENV`: The environment in which to run your application; either `development` or `production`.
- `FLASK_DEBUG`: `1` to enable debugging or `0` to disable.
- `SECRET_KEY`: This can be any string (the longer the more secure).
- `DBHOST`: Set the host address of the Postgres database. If you're using `docker compose` to launch the app, check the ipv4 in the docker-compose.yml file.
- `DBUSER` `DBPASS` `DBNAME`: Postgres database credentials.
- `BASE_URL`: URL where the application will be deployed.
- `VERIFICATION_EMAIL`: Email address to send verification code
- `VERIFICATION_EMAIL_PASS`: Verification email password. If using a google email address you’ll need to setup an app password. You can find [instructions here](https://support.google.com/accounts/answer/185833?hl=en).
- `LIMIT_REGISTRATION_DOMAINS`: If "True" user registration will be limited to the emails in the flask-app/app/email_domains.json file
  <br>

###### Run the application

To run the container independent of the database:

1. Install requirements:

- `pip install -r requirements.txt`

2. Start the app with `flask run` or `python wsgi.py`.

3. To run the app using Docker use `docker build -t "flask-app" .` then `docker run -d --name flask-dash-app -p 5555:5000 flask-app`

4. Check that the app is running at http://localhost:5555

You can also run the app using docker

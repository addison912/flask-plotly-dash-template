# Flask Template Monorepo

This application has two Docker containers:

1. ##### Flask App
   - Serves the Flask web application which allows users to register and login.
   - Serves Plotly Dash apps with authentication provided by the parent Flask app.
2. ##### Postgres DB
   - Contains the user database for the Flask app.

Each container can be run independently (see the README in the flask-app and postgres-db directories), or simultaneously.

## Getting Started

1. To launch the app in developement mode, rename and edit the **.env.example** file to **.env** in both the flask-app and postgres-db directories.

2. Start the application using `docker compose build && docker compose up -d`.

3. Stop the application using `docker compose down`.

4. After making changes to the app run `docker compose build && docker compose up -d`

## Troubleshooting

To create a clean build, remove the docker images and restart the containers

```
docker compose down
docker image rm flask-app-mono-repo_app flask-app-mono-repo_db
docker compose up -d
```

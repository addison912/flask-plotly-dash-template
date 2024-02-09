# Postgres Database

### Getting Started

Replace the values in `postgres-db/.env.example` with your values and rename this file to `.env`:

- `POSTGRES_PASSWORD` should match the `DBPASS` set in the flask-app .env file.
- `POSTGRES_USER` should match the `DBUSER` set in the flask-app .env file.
- `POSTGRES_DB` should match the `DBNAME` set in the flask-app .env file.

To build the container without using ```docker compose```.
```docker build -t "postgres-db" .```

Run the container.
```docker run -dit --name postgres-db -p 5433:5432 --env-file ./.env postgres-db```

Start the container.
```docker start postgres-db```

For a container shell.
```docker exec -it postgres-db /bin/bash```

For psql terminal.
```docker exec -it postgres-db psql -U flask_user -d flask_app```

### Backing up Data

To create a backup of the database on the host machine, run:
```docker exec postgres_db bash -c 'pg_dump -U flask_user flask_app > flask_app.sql' && docker cp postgres_db:/flask_app.sql .```
This will create a backup file called ```flask_app.sql``` in the current working directory.


To build the postgres_db image using a backup of the database, rename the backup file to ```init_flask_app.sql``` and replace the ```init_flask_app.sql``` file in this directory with the new file. Then build the image.
FROM postgres:14.5

COPY init_pg.sql /docker-entrypoint-initdb.d/
COPY init_flask_app.sql /docker-entrypoint-initdb.d/

# CMD ./init_db.sh
# RUN psql -U ${POSTGRES_USER} -d flask_app < init_flask_app.sql

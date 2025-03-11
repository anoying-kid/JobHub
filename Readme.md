# Postgres setup in Docker


```bash
docker run -d --name my_postgres -e POSTGRES_DB=mydatabase -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -p 5432:5432 postgres:latest
```
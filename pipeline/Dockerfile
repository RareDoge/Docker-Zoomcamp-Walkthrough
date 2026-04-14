FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code
# Add virtual environment to PATH so we can use installed packages
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked


COPY ingest_data.py .

ENTRYPOINT ["python", "ingest_data.py"]


# docker run -it --rm \
# -e POSTGRES_USER="root" \
# -e POSTGRES_PASSWORD="root" \
# -e POSTGRES_DB="ny_taxi" \
# -v ny_taxi_postgres_data:/var/lib/postgresql \
# -p 5432:5432 \
# --network=pg-network \
# --name pgdatabase \
# postgres:18

# docker run -it --rm \
# --network=pg-network \
# taxi_ingest:v001 \
# --pg-user=root \
# --pg-pass=root \
# --pg-host=pgdatabase \
# --pg-port=5432 \
# --pg-db=ny_taxi \
# --target-table=yellow_taxi_trips_2021_1 \
# --chunksize=100000
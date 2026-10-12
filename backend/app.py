import os
from datetime import datetime

import psycopg
from fastapi import FastAPI

app = FastAPI()

DATABASE_URL = os.environ["DATABASE_URL"]


def get_conn():
    return psycopg.connect(DATABASE_URL)


@app.on_event("startup")
def init_db():
    with get_conn() as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS visits ("
            "id SERIAL PRIMARY KEY, "
            "visited_at TIMESTAMP DEFAULT now())"
        )


@app.get("/")
def read_root():
    return {"message": "Ahoj z backendu!"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/time")
def get_time():
    return {"time": datetime.now().isoformat()}


@app.post("/api/visit")
def add_visit():
    with get_conn() as conn:
        cur = conn.execute("INSERT INTO visits DEFAULT VALUES RETURNING id")
        new_id = cur.fetchone()[0]
    return {"inserted_id": new_id}


@app.get("/api/visits")
def list_visits():
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT id, visited_at FROM visits ORDER BY id"
        ).fetchall()
    return {
        "count": len(rows),
        "visits": [{"id": r[0], "visited_at": r[1].isoformat()} for r in rows],
    }

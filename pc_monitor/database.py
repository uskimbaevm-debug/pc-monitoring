import sqlite3
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
DB_PATH = DATA_DIR / "monitoring.db"


def connection():
    DATA_DIR.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = connection()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS metrics (
    id INTEGER PRIMARY KEY,
    timestamp TEXT NOT NULL,
    cpu_percent REAL NOT NULL,
    ram_percent REAL NOT NULL,
    disk_percent REAL NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

def insert_metrics(metrics):
    conn = connection()

    conn.execute("""
        INSERT INTO metrics (
            timestamp,
            cpu_percent,
            ram_percent,
            disk_percent
        )
        VALUES (?, ?, ?, ?)
    """, (
        metrics["timestamp"],
        metrics["cpu_percent"],
        metrics["ram_percent"],
        metrics["disk_percent"],
    ))

    conn.commit()
    conn.close()

def get_metrics():
    conn = connection()


    cursor = conn.execute("""
    SELECT * FROM metrics
    ORDER BY id
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows

if __name__ == "__main__":
    create_table()
    rows = get_metrics()

    if not rows:
        print("В базе пока нет замеров")
    else:
        for row in rows:
            print(row)
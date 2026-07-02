import sqlite3
from datetime import datetime

DB_NAME = "realestate.db"

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analysis_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        listing_text TEXT,
        quality_score INTEGER,
        seo_score INTEGER,
        missing_fields TEXT,
        explanation TEXT,
        improved_listing TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_analysis(listing_text, result):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO analysis_results (
        listing_text,
        quality_score,
        seo_score,
        missing_fields,
        explanation,
        improved_listing,
        created_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        listing_text,
        result.get("quality_score"),
        result.get("seo_score"),
        str(result.get("missing_fields")),
        str(result.get("explanation")),
        result.get("improved_listing"),
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()

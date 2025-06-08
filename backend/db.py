import psycopg2
import os
from dotenv import load_dotenv

# Load env vars from .env file
load_dotenv()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            sslmode=os.getenv("DB_SSLMODE")
        )
        print("✅ Connected to database.")
        return conn
    except Exception as e:
        print("❌ Database connection failed:", e)
        return None


if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        print("Current DB time:", cur.fetchone())
        cur.close()
        conn.close()
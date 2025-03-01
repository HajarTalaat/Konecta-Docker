from flask import Flask
import os
import psycopg2

app = Flask(__name__)

# Get database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

@app.route('/')
def hello():
    message = os.getenv("APP_MESSAGE", "Hello, Docker!")
    
    # Check PostgreSQL connection
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.close()
        db_status = "Connected to Database!"
    except Exception as e:
        db_status = f"Database connection failed: {str(e)}"

    return f"<h1>{message}</h1><p>{db_status}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


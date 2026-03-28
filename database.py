#creates and manages the sqlite database and all tables.
import sqlite3

DB_Name = "Maestro_vortex.db"

def the_talents():
    return sqlite3.connect(DB_Name)

def connect_db():
    conn = the_talents()
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS portfolio (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            title        TEXT NOT NULL,
            category     TEXT,
            tools        TEXT,
            url          TEXT, 
            description  TEXT,
            date_added   TEXT             
               ) 
""")
    
    c.execute("""
        CREATE TABLE IF NOT EXISTS jobs(
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            title        TEXT NOT NULL,
            company      TEXT,
            location     TEXT, 
            job_type     TEXT,
            field        TEXT, 
            salary       TEXT,
            deadline     TEXT,
            description  TEXT,
            apply_link   TEXT,
            date_added   TEXT                   
              )    
""")
    
    c.execute("""
        CREATE TABLE IF NOT EXISTS applications(
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            job_id        INTEGER,
            job_title     TEXT,
            company       TEXT, 
            cover_note    TEXT,
            status        TEXT DEFAULT 'Submitted',
            date_applied  TEXT,
            FOREIGN KEY (job_id) REFERENCES JOBS(id)                
              )
""")
    
    conn.commit()   
    conn.close()  
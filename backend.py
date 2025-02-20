#Aiden Fatta
#12/6/2024
#Revised backend for the VITA Volunteer Management System

import sqlite3

def connect():
    # Connects to and creates the volunteer database
    conn = sqlite3.connect("volunteers.db")
    cur = conn.cursor()
    # Create volunteer table
    cur.execute("CREATE TABLE IF NOT EXISTS volunteer(id INTEGER PRIMARY KEY, name TEXT, job TEXT,"
        " affiliation TEXT, email TEXT, phone INTEGER)")
    # Create experience table
    cur.execute("CREATE TABLE IF NOT EXISTS experience(id INTEGER PRIMARY KEY, title TEXT UNIQUE, description TEXT)")
    # Create volunteer_experience bridge table
    cur.execute("CREATE TABLE IF NOT EXISTS volunteer_experience(volunteer_id INTEGER, experience_id INTEGER,"
        " dateObtained TEXT, expirationDate TEXT, PRIMARY KEY (volunteer_id, experience_id),"
        " FOREIGN KEY (volunteer_id) REFERENCES volunteer(id),"
        " FOREIGN KEY (experience_id) REFERENCES experience(id))")
    conn.commit()
    conn.close()

def view_volunteer():
    conn = sqlite3.connect("volunteers.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM volunteer")
    rows = cur.fetchall()
    conn.close()
    return rows

def view_experiences():
    conn = sqlite3.connect("volunteers.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM experience")
    rows = cur.fetchall()
    conn.close()
    return rows

def search_volunteer(name="", job="", affiliation="", email="", phone=""):
    conn = sqlite3.connect("volunteers.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM volunteer WHERE name=? OR job=? OR affiliation=? OR email=? OR phone=?",
        (name, job, affiliation, email, phone))
    rows = cur.fetchall()
    conn.close()
    return rows

def search_volunteer_by_id(id=""):
    conn = sqlite3.connect("volunteers.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM volunteer WHERE id=?", (id,))
    rows = cur.fetchall()
    conn.close()
    return rows

def search_experiences(title="", desc=""):
    conn = sqlite3.connect("volunteers.db")
    cur = conn.cursor()
    cur.execute( "SELECT * FROM experience WHERE (title=? OR description=?",
        (title, desc))
    rows = cur.fetchall()
    conn.close()
    return rows

def join_bridge(ownerid):
    conn = sqlite3.connect("volunteers.db")
    cur = conn.cursor()
    cur.execute("""
        SELECT experience_id, title, description, dateObtained, expirationDate, volunteer_id
        FROM volunteer_experience
        JOIN experience ON volunteer_experience.experience_id = experience.id
        WHERE volunteer_id=?
    """, (ownerid,))
    rows = cur.fetchall()
    conn.close()
    return rows

def insert_volunteer(name, job, affiliation, email, phone):
    conn = sqlite3.connect("volunteers.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO volunteer VALUES(null,?,?,?,?,?)", (name, job, affiliation, email, phone))
    conn.commit()
    conn.close()

def insert_experience(title, desc, obtained, expiration, ownerid):
    conn = sqlite3.connect("volunteers.db")
    cur = conn.cursor()
    #Check if experience already exists in database
    cur.execute("SELECT id FROM experience WHERE title=?", (title,))
    row = cur.fetchone()

    #If experience already exists in database, it's id is retreived for the insert into bridge method
    if row:
        experience_id=row[0]
    #If experience doesn't exist it's added and it's id is retrieved with lastrowid
    else:
        cur.execute("INSERT INTO experience (title, description) VALUES (?, ?)", (title, desc))
        conn.commit()
        experience_id = cur.lastrowid
    conn.close()
    insert_into_bridge(experience_id, ownerid, obtained, expiration)

def insert_into_bridge(experience_id, ownerid, obtained, expiration):
    conn = sqlite3.connect("volunteers.db")
    cur = conn.cursor()
    # Insert into volunteer_experience table
    cur.execute("INSERT INTO volunteer_experience (experience_id, volunteer_id, dateObtained, expirationDate) VALUES (?, ?, ?, ?)", (experience_id, ownerid, obtained, expiration))
    conn.commit()
    conn.close()

def update_volunteer(id, name="", job="", affiliation="", email="", phone=""):
    conn = sqlite3.connect("volunteers.db")
    cur = conn.cursor()
    cur.execute("UPDATE volunteer set name=?, job=?, affiliation=?, email=?, phone=? WHERE id=?",
                (name, job, affiliation, email, phone, id))
    conn.commit()
    conn.close()

def update_experience(ownerid="", id="", title="", desc="", obtained="", expiration=""):
    conn = sqlite3.connect("volunteers.db")
    cur = conn.cursor()
    cur.execute("UPDATE experience SET title=?, description=? WHERE id=?", (title, desc, id))
    conn.commit()
    conn.close()
    update_experience_bridge(id, ownerid, obtained, expiration)

def update_experience_bridge(id, ownerid, obtained, expiration):
    conn = sqlite3.connect("volunteers.db")
    cur = conn.cursor()
    cur.execute("UPDATE volunteer_experience SET dateObtained=?, expirationDate=? WHERE experience_id=? AND volunteer_id=?", (obtained, expiration, id, ownerid))
    conn.commit()
    conn.close()

def delete_volunteer(id):
    conn = sqlite3.connect("volunteers.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM volunteer WHERE id=?", (id,))
    conn.commit()
    conn.close()

def delete_experience(id):
    conn = sqlite3.connect("volunteers.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM volunteer_experience WHERE experience_id=?", (id,))
    conn.commit()
    conn.close()

connect()

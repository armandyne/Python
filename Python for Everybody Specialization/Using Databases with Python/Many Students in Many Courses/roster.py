import json
import sqlite3

file = 'roster_data.json'
json_data = json.loads(open(file).read())

db = sqlite3.connect('coursedb.sqlite')
cur = db.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

for r in json_data:
    User_name = r[0]
    Course_title = r[1]
    role = r[2]
    
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( User_name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (User_name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( Course_title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (Course_title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )
    
    db.commit()
    
    
import sqlite3
connection = sqlite3.connect("projects.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE projects
    (url TEXT, descr TEXT, income INTEGER)
""")
cursor.execute("""INSERT INTO projects VALUES 
    ('giraffes.io', 'Uber, but with giraffes', 1900),
    ('petpetting.com', 'Pet petting service', 2800),
    ('awesomehands.com', 'Working as a hand model', 3),
    ('hummingpro.io', 'Online courses about humming', 120000)
""")
connection.commit()
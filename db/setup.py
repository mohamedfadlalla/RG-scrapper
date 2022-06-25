import sqlite3

def ConnectDB(file):
    #Creating Database and tables
    conn2 = sqlite3.connect(file)
    cur2 = conn2.cursor()

    return conn2, cur2


def Setup(file):
    #Creating Database and tables
    conn2 = sqlite3.connect(file)
    cur2 = conn2.cursor()

    # Create Skill TABLE
    cur2.execute('''
        CREATE TABLE IF NOT EXISTS Skill (
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
          title TEXT UNIQUE
        )
    ''')

    # Profile TABLE
    cur2.execute('''
        CREATE TABLE IF NOT EXISTS Profile (
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
          name TEXT UNIQUE,
          country TEXT,
          degree TEXT,
          publications INTEGER,
          reads INTEGER,
          citation INTEGER,
          projects INTEGER,
          most_p TEXT,
          email TEXT,
          aff TEXT, 
          department TEXT,
          url TEXT UNIQUE
          )
    ''')

    # Create Institute TABLE
    cur2.execute('''
        CREATE TABLE IF NOT EXISTS Institute (
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
          name TEXT UNIQUE,
          contry TEXT UNIQUE

        )
    ''')

    # Publication TABLE
    cur2.execute('''
        CREATE TABLE IF NOT EXISTS Publication (
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
          title TEXT UNIQUE,
          url TEXT UNIQUE,
          doi TEXT UNIQUE
    )
    ''')

    # Create Projects TABLE
    cur2.execute('''
        CREATE TABLE IF NOT EXISTS Projects (
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
          project TEXT UNIQUE,
          url TEXT UNIQUE

        )
    ''')

    # Create Projects TABLE
    cur2.execute('''
        CREATE TABLE IF NOT EXISTS Globe (
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
          url TEXT UNIQUE,
          status INTEGER
        )
    ''')

    ###many to many tables###
    #skilled table
    cur2.executescript('''
    CREATE TABLE Skilled (
      skill_id   INTEGER,
      profile_id INTEGER,
      PRIMARY KEY (skill_id, profile_id)
    )
    ''')

    cur2.executescript('''
    CREATE TABLE Affiliation (
      institue_id   INTEGER,
      profile_id INTEGER,
      started TEXT,
      ended TEXT,
      position TEXT,
      PRIMARY KEY (institue_id, profile_id)
    )
    ''')

    cur2.executescript('''
    CREATE TABLE Published (
      publication_id INTEGER,
      profile_id INTEGER,
      authorship TEXT,
      PRIMARY KEY (publication_id, profile_id)
    )
    ''')

    cur2.executescript('''
    CREATE TABLE Projected (
      project_id INTEGER,
      profile_id INTEGER,
      PRIMARY KEY (project_id, profile_id)
    )
    ''')

    cur2.executescript('''
    CREATE TABLE Network (
      net_id INTEGER,
      profile_id INTEGER,
      PRIMARY KEY (net_id, profile_id)
    )
    ''')
    
    return conn2, cur2
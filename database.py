import mysql.connector


host = ''
username = ''
password = ''
database = ''
def getDB():
    with open('databaselogin.txt') as f:
        creds = f.readline()
    credlist = creds.split(';')
    host = credlist[0]
    username = credlist[1]
    password = credlist[2]
    database = credlist[3]

    DB = mysql.connector.connect(
    host=host,
    user=username,
    password=password,
    database=database,
    port=3306
    ) 
    return DB

def getReqSingle(uid:int) -> int:
    DB = getDB()
    cursor = DB.cursor()

    cursor.execute(f"SELECT REQUESTS FROM requests WHERE UID={uid}")
    requests = cursor.fetchone()
    if not len(requests) == 0:
        return requests[0]
    else:
        return 0


def getAmmountUsers() -> int:
    DB = getDB()
    cursor = DB.cursor()
    cursor.execute("SELECT UID FROM requests")
    all = cursor.fetchall()
    return len(all)


def getReqOrdered(page:int = 1):
    DB = getDB()
    cursor = DB.cursor()
    
    if page == 1:
        cursor.execute(f"SELECT UID, REQUESTS FROM requests ORDER BY REQUESTS DESC LIMIT 10")
    else: 
        page = page * 10 -1
        cursor.execute(f"SELECT UID, REQUESTS FROM requests ORDER BY REQUESTS DESC LIMIT 10 OFFSET {page}")
    return cursor.fetchall()

def incrementReq(uid:int) -> None:
    DB = getDB()
    cursor = DB.cursor()
    reqs = getReqSingle(uid)

    if reqs == 0:
        addUser(uid)
    else:
        reqs += 1
        cursor.execute(f"UPDATE requests SET REQUESTS={reqs} WHERE UID={uid}")
    DB.commit()

def addUser(uid:int) -> None:
    DB = getDB()
    cursor = DB.cursor()
    cursor.execute(f"INSERT INTO requests (UID, REQUESTS, LASTREQ, STREAK) VALUES ({uid}, 1, 0, 0)")

def getStreakSingle():
    #TODO: make streak system
    pass

def incrementStreak(uid:int):
    #TODO: make sreak system
    pass


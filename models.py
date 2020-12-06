from db_con import db


def signin(username,password):
    myCursor = db.cursor(dictionary=True)
    query = "SELECT * FROM tbl_users WHERE username = '{0}' AND password = '{1}'".format(username,password)
    myCursor.execute(query)
    return myCursor.fetchone()

def get_countSheet():
    myCursor = db.cursor(dictionary=True)
    query = "SELECT * FROM tbl_countsheet"
    myCursor.execute(query)
    return myCursor.fetchall()

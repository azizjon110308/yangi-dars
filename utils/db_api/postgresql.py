import psycopg2


def send_ex(command):
    mydb = psycopg2.connect(user = "Databases",
                            password = "2008",
                            host = "127.0.0.1",
                            port = "5432",
                            database = "NEW_DATABASE_INFO")
    mycursor = mydb.cursor()

    mycursor.execute(command)
    res = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    mydb.close()
    return res
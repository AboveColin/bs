import sql.setup as setup
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import functions as function
import init as init

now = init.datetime.now()
dt = now.strftime("%Y-%m-%d %H:%M:%S")

if setup.check_already_exists() == False:
    setup.create_Tables()

def get_artistID(Artist):
    Cursor = init.DB_con.cursor()
    Cursor.execute("SELECT DISTINCT ID FROM Artists WHERE Name = '"+str(Artist)+"';")
    
    Results = Cursor.fetchall()
    return Results[0][0]

def check_exist_track(Title, Artist1):
    Cursor = init.DB_con.cursor()
    Cursor.execute("SELECT ID FROM Tracks WHERE Title = '"+Title+"' AND by_Artist1 = '"+str(get_artistID(Artist1))+"';")
    if len(Cursor.fetchall()) == 0:
        return False
    else:
        return True

def check_exist_artist(Artist):
    Cursor = init.DB_con.cursor()
    Cursor.execute("SELECT ID FROM Artists WHERE Name = '"+str(Artist)+"';")
    if len(Cursor.fetchall()) == 0:
        return False
    else:
        return True

def insert_new_track(Title, Artists_Array):
    Cursor = init.DB_con.cursor()
    if len(Artists_Array) == 1:
        sql = "INSERT INTO Tracks (Title, Date_Added, by_Artist1) VALUES (%s, %s, %s)"
        val = (str(Title), str(dt), str(get_artistID(Artists_Array[0])))
    elif len(Artists_Array) == 2:
        sql = "INSERT INTO Tracks (Title, Date_Added, by_Artist1, by_Artist2) VALUES (%s, %s, %s, %s)"
        val = (str(Title), str(dt), str(get_artistID(Artists_Array[0])), str(get_artistID(Artists_Array[1])))
    elif len(Artists_Array) == 3:
        sql = "INSERT INTO Tracks (Title, Date_Added, by_Artist1, by_Artist2, by_Artist3) VALUES (%s, %s, %s, %s, %s)"
        val = (str(Title), str(dt), str(get_artistID(Artists_Array[0])), str(get_artistID(Artists_Array[1])), str(get_artistID(Artists_Array[2])))
    Cursor.execute(sql, val)
    init.DB_con.commit()

def insert_new_artist(Artist):
    Cursor = init.DB_con.cursor()
    sql = "INSERT INTO Artists (Name) VALUES ('"+str(Artist)+"');"
    Cursor.execute(sql)
    init.DB_con.commit()



def insert_to_db(Title, Artist_Array):

    for x in range(len(Artist_Array)):

        if check_exist_artist(Artist_Array[x]) == False:
            insert_new_artist(Artist_Array[x])
            
    if check_exist_track(Title, Artist_Array[0]) == False:
        insert_new_track(Title, Artist_Array)
        if init.args.discord_webhook:
            function.discord_notification(Title, Artist_Array)

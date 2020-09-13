import MySQLdb

class GetInfo:

    def __init__(self, UserID):
        self.UserID = UserID

    def Info(self):

        db = MySQLdb.connect(host='dylan9012.mysql.pythonanywhere-services.com',
                            user='dylan9012',
                            password='destiny1',
                            db='dylan9012$default',
                            )

        cur = db.cursor()

        db.set_character_set('utf8')
        cur.execute('SET NAMES utf8;')
        cur.execute('SET CHARACTER SET utf8;')
        cur.execute('SET character_set_connection=utf8;')

        cur.execute('SELECT UserID, Name, Age, Disability_or_specialty, Location, Carer_or_client gender, Email, Gender, Phone_number, Password FROM Account WHERE UserID = ' + self.UserID + ';')

        r = cur.fetchall()
        db.close()
        return list(r[0])


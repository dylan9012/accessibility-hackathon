import MySQLdb

class GetContacts:

    def __init__(self, LikedID):
        self.LikedID = LikedID

    def FindContacts(self):

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

        cur.execute('SELECT Phone_number, Email FROM Account WHERE UserID = ' + self.LikedID + ';')

        r = cur.fetchall()
        db.close()
        return list(r[0])


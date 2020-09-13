import MySQLdb

class FindLikes:

    def __init__(self, LikerID, LikedID):
        self.LikerID = LikerID
        self.LikedID = LikedID

    def Like (self):

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


        cur.execute('INSERT INTO Likes VALUES (' + self.LikerID +', ' + self.LikedID + ', true);')
        db.commit()


        cur.execute('SELECT UserID_of_liked, UserID FROM Likes WHERE UserID = ' + self.LikedID + ' AND UserID_of_liked = ' + self.LikerID + ';')

        result = cur.fetchall()

        res = list(result[0])
        print(res)
        print([self.LikerID, self.LikedID])
        if res == [int(self.LikerID), int(self.LikedID)]:
            cur.execute('SELECT Name, Gender, Age, Location FROM Account WHERE UserID = ' + self.LikedID + ';')
            i = cur.fetchall()
            db.close()
            return i

        else:
            db.close()
            return False


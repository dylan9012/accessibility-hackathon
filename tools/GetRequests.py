import MySQLdb
from tools.codes_to_km import GreatCircleDistance

class GetRequest:

    def __init__(self, id):
        self.id = id

    def FindRequests(self):


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

        cur.execute('SELECT Location from Account where UserID = ' + self.id +';')
        t = cur.fetchall()
        location = list(t[0])[0]


        cur.execute('SELECT LikerID, Account.Name, Account.Gender, Account.Age, Account.Location FROM Likes, Account WHERE LikedID = ' + self.id + ' AND Likes.LikerID = Account.UserID;')



        r = cur.fetchall()
        db.close()
        final = list(r[0])
        for x in final:
            x[4] = x.append(GreatCircleDistance(location, x[4]))



        return final

if __name__ == "__main__":
    pass

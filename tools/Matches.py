import MySQLdb
from tools.codes_to_km import GreatCircleDistance

class FindMatches:

    def __init__(self, id):
        self.id = id

    def PotentialMatches(self):

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

        cur.execute('SELECT Location, Max_distance, Needs_or_specialty, UserID, Carer_or_client FROM Account WHERE UserID = ' + str(id) + ';')
        r = cur.fetchall()
        UserValues = list(r[0])

        cur.execute('SELECT Location, max_distance, Needs_or_specialty, Account.UserID, age, gender FROM Account, Likes WHERE Needs_or_specialty = "' + UserValues[2] + '" AND Carer_or_client != ' + UserValues[4] + ' AND Like.UserID != ' + self.ID +' AND Account.UserID != Like.UserID_of_liked')
        s = cur.fetchall()
        potentials1 = [list(i) for i in s]

        for k in potentials1:
            if k[3] == int(id):
                potentials1.remove(k)
                break
            else:
                pass

        for i in potentials1:
            i.append(GreatCircleDistance(UserValues[0], i[0]).get_distance())

        finalmatches = []

        for q in potentials1:
            if q[6] < UserValues[1]:
                finalmatches.append(q)

        return finalmatches

        db.close()

if __name__ == "__main__":
    pass

import MySQLdb


class ValidateLogIn:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def log_in(self):

        db = MySQLdb.connect(host='dylan9012.mysql.pythonanywhere-services.com',
                             user='dylan9012',
                             password='destiny1',
                             db='dylan9012$default'
                             )

        cur = db.cursor()

        db.set_character_set('utf8')
        cur.execute('SET NAMES utf8;')
        cur.execute('SET CHARACTER SET utf8;')
        cur.execute('SET character_set_connection=utf8;')
        cur.execute("select Email from Account;")
        result = cur.fetchall()
        x = list(result)
        email1 = [list(y) for y in x]
        emails = [str(z)[2:len(str(z)) - 2] for z in email1]
        if self.email not in emails:
            return False
            db.close()
        else:
            cur.execute('SELECT Password FROM Account Where Email = ' + '"' + self.email + '";')
            r = cur.fetchall()
            final_pass = str(r)[3:len(r) - 6]
            if final_pass == self.password:
                cur.execute('SELECT UserID FROM Account Where Email = ' + '"' + self.email + '";')
                i = cur.fetchall()
                identity = (int(str(i)[2:len(i) - 5]))
                db.close()
                return identity

            else:
                db.close()
                return False


if __name__ == "__main__":
    pass

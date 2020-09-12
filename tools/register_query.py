import MySQLdb


class ValidateSignUp:

    def __init__(self, email, name, age, needs_or_specialty, max_distance, location, carer_or_client, gender,
                 phone_number, password):
        self.email = email
        self.name = name
        self.age = age
        self.needs_or_specialty = needs_or_specialty
        self.max_distance = max_distance
        self.location = location
        self.carer_or_client = carer_or_client
        self.gender = gender
        self.phone_number = phone_number
        self.photo = '01'
        self.password = password

    def sign_up(self):

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
        if self.email in emails:
            db.close()
            return False
        else:
            su = (
                    'INSERT INTO Account VALUES (NULL, "' + self.name + '", "' + self.age + '", "' + self.needs_or_specialty + '", "' + self.max_distance + '", "' + self.location + '", "' + self.carer_or_client + '", "' + self.email + '", "' + self.gender + '", "' + self.phone_number + '", "' + self.photo + '", "' + self.password + '");')
            cur.execute(su)
            db.close()
            return True


if __name__ == "__main__":
    pass

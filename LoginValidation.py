import MySQLdb

email = 'eyuael@yahoo.co.uk'
password = 'hello'

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
number_of_rows = cur.execute("select Email from Account");
result = cur.fetchall()
x = list(result)
email1 = [list(y) for y in x]
emails = [str(z)[2:len(str(z))-2] for z in email1]
if email not in emails:
    print('error: account doesnt exist')
else:
    n = cur.execute('SELECT Password FROM Account Where Email = ' + '"'+email+'";')
    r = cur.fetchall()
    finalpass = str(r)[3:len(r)-6]
    if finalpass == password:
        print("Logging in")
        k = cur.execute('SELECT UserID FROM Account Where Email = ' + '"'+email+'";')
        i = cur.fetchall()
        ID=(int(str(i)[2:len(i)-5]))
    else:
        print("error: incorrect password")
db.close()
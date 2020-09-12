import MySQLdb

email = 'isaac@yahoo.co.uk'
Name = 'Isaac'
age = '19'
Needs_or_specialty = 'blind'
Max_distance = '6'
Location = 'SS00RG'
Carer_or_client = 'true'
gender = 'F'
phone_number = '07914123456'
Photo = '01'
password = 'hi'


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
if email  in emails:
    print('error: account already exists')
else:
    su = ('INSERT INTO Account VALUES (NULL, "' + Name + '", "' + age +'", "' + Needs_or_specialty +'", "'+ Max_distance +'", "'+ Location +'", "'+ Carer_or_client +'", "'+ email  +'", "'+ gender +'", "'+ phone_number +'", "'+ Photo +'", "'+ password + '");')
    cur.execute(su)
    print('signup was successful')

number_of_rows = cur.execute("select * from Account");

result = cur.fetchall()

print(result)

db.close()
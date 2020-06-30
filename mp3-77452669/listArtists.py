import pymysql
import cgi

db = pymysql.connect(host='localhost',
                     user='gallery',
                     passwd='eecs118',
                     db= 'gallery')
cur = db.cursor()

form = cgi.FieldStorage()

print("Content-Type: text/html") #HTML is following
print()
print("<html>")
print("<body>")

#link to go to 'Home'
print("<a href='77452669_index.py'>Home</a>")

#link to go to 'Manage Artists'
print("<a href='manageArtist.py'>Manage Artists</a>")

print("<H1>List of Artists</H1>")

sql="SELECT * FROM artist" #read from gallery table
cur.execute(sql)

print('<p>Artist ID --- Name --- Birth Year --- Country --- Description</p>')
for row in cur.fetchall(): #grab from all the tuples
	print('<p>' + str(row[0]) + ' --- ' + str(row[1]) + ' --- ' + str(row[2]) + ' --- ' + str(row[3]) + ' --- ' + str(row[4]) + '</p>')

print("</body>")
print("</html>")
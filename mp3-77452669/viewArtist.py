import pymysql
import cgi

db = pymysql.connect(host='localhost',
                     user='gallery',
                     passwd='eecs118',
                     db= 'gallery')
cur = db.cursor()

form = cgi.FieldStorage()

artist_id_str = str(form.getvalue('artist_id'))
sql="SELECT * FROM artist WHERE artist_id=" + artist_id_str #read from artist table
cur.execute(sql)

row = cur.fetchone()
artist_name_pass = str(row[1])
artist_birth_pass = str(row[2])
artist_country_pass = str(row[3])
artist_description_pass = str(row[4])

print("Content-Type: text/html") #HTML is following
print()
print("<html>")
print("<body>")

#link to go to 'Home'
print("<a href='77452669_index.py'>Home</a>")

print('<form action="viewImage.py">')
print('<input id="image_id" name="image_id" type="hidden" value="' + str(form.getvalue('image_id')) + '">')
print('<input type="submit" value="Go Back to Image" />') #Submit Button

print('<p>Artist: ' + artist_name_pass + '</p>')				#Artist
print('<p>Birth Year: ' + artist_birth_pass + '</p>')			#Birth Year
print('<p>Country: ' + artist_country_pass + '</p>')			#Country
print('<p>Description: ' + artist_description_pass + '</p>')	#Description

print("</body>")
print("</html>")
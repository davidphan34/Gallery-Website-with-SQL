#Manage Artists python file
# - can put in a new artist
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

#Link to go back to listGalleries
print("<a href='listArtists.py'>Go Back</a>")

#display that Artist is Modified
if str(form.getvalue('artist_name_modify')) != 'None': #to ensure that we're putting something in the table
	print("<H1><font color='red'>Artist Modified!!</font></H1>")

#display if Artist is Added
if str(form.getvalue('artist_name_input')) != 'None': #to ensure that we're putting something in the table
	print("<H1><font color='red'>Artist Added!!</font></H1>")

print("<H1>Create New Artist</H1>")
print('<form action="manageArtist.py">')

#------------------------------------------Input for Artist------------------------------------------#
print('<p>--Name: <input type="text" name="artist_name_input"/></p>')         	 	#Input Artist Name
print('<p>--Birth Year: <input type="text" name="artist_birth_input"/></p>')		#Input Artist Birth
print('<p>--Country: <input type="text" name="artist_country_input"/></p>')			#Input Artist Country
print('<p>--Description: <input type="text" name="artist_description_input"/></p>')	#Input Artist Description
#-----------------------------------------------------------------------------------------------------#

print('<input type="submit" value="Submit" />') #Submit Button

print("</form>")

#------------------------------------------Modify Artist Details------------------------------------------#
print('<form action="manageArtist.py">')
print("</br><H1>Modify Artist Details</H1>")
print('<p>--Artist ID for Artist to be modified: <input type="text" name="artist_id_modify"/></p>')	#Input Artist ID
print('<p>--New Name: <input type="text" name="artist_name_modify"/></p>')								#modify Artist Name
print('<p>--New Birth Year: <input type="text" name="artist_birth_modify"/></p>')						#modify Artist Birth
print('<p>--New Country: <input type="text" name="artist_country_modify"/></p>')						#modify Artist Country
print('<p>--New Description: <input type="text" name="artist_description_modify"/></p>')				#modify Artist Description

print('<input type="submit" value="MODIFY Details" />') #Submit Button

print("</form>")

if str(form.getvalue('artist_name_modify')) != 'None': #to ensure that we're putting something in the table
	sql = "UPDATE artist SET name ='" + str(form.getvalue('artist_name_modify')) + "', birth_year ='" + str(form.getvalue('artist_birth_modify')) + "', country ='" + str(form.getvalue('country')) + "', description = '" + str(form.getvalue('artist_description_modify')) + "' WHERE artist_id='" + str(form.getvalue('artist_id_modify')) + "'"
	cur.execute(sql)
	db.commit()
#-----------------------------------------------------------------------------------------------------#
print("</body>")
print("</html>")

#sql queries
if str(form.getvalue('artist_name_input')) != 'None': #to ensure that we're putting something in the table
	sql = ("""INSERT IGNORE INTO artist(name, birth_year, country, description) 
	VALUES(%s,%s,%s,%s)""")
	#get values from the form and put it into  the database
	val = (str(form.getvalue('artist_name_input')), str(form.getvalue('artist_birth_input')), 
		str(form.getvalue('artist_country_input')), str(form.getvalue('artist_description_input')))
	#val = (galleryNameInput, galleryDescript)
	cur.execute(sql, val)
	db.commit() #use commit to save the changes you made to the database

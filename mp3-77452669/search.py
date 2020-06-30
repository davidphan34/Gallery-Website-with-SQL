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

#Click to go to 'List of Galleries'
print("<a href='listGalleries.py'>List of Galleries</a>")

if(form):
	print('<H1><font color ="red">Search Result Produced! Scroll Down for Results!</font></H1>')


#========================================SEARCH FUNCTIONS========================================#
#-------------------------------search images by type-------------------------------#
print('<form action="search.py">')
print('<H1>Search Image by Type: </br><input type="text" name="image_type_search"/></H1>')#Input Image Title
print('<input type="submit" value="Search by Type" />') #Submit Button
print("</form>")
#-------------------------------search images by year-------------------------------#
print('<form action="search.py">')
print('</br><H1>Search Image Between Years</H1>')#Input Image Title
print('<p>--Start at Year: <input type="text" name="image_start_year_search"/></p>')#Start Year
print('<p>--End at Year: <input type="text" name="image_end_year_search"/></p>')#End Year
print('<input type="submit" value="Search by Year" />') #Submit Button
print("</form>")
#-------------------------------search images by artist-------------------------------#
print('<form action="search.py">')
print('</br><H1>Search Image by Artist Name: </br><input type="text" name="image_artist_search"/></H1>')#Input Image Title
print('<input type="submit" value="Search by Artist" />') #Submit Button
print("</form>")
#-------------------------------search images by location-------------------------------#
print('<form action="search.py">')
print('</br><H1>Search Image by Location: </br><input type="text" name="image_location_search"/></H1>')#Input Image Title
print('<input type="submit" value="Search by Location" />') #Submit Button
print("</form>")
#-------------------------------search artist by country-------------------------------#
print('<form action="search.py">')
print('</br><H1>Search Artist by Country: </br><input type="text" name="artist_country_search"/></H1>')#Input Image Title
print('<input type="submit" value="Search by Country" />') #Submit Button
print("</form>")
#-------------------------------search artist by birth year-------------------------------#
print('<form action="search.py">')
print('</br><H1>Search Artist by Birth Year: </br><input type="text" name="artist_birth_year_search"/></H1>')#Input Image Title
print('<input type="submit" value="Search by Birth Year" />') #Submit Button
print("</form>")
#================================================================================================#



#========================================PRINT RESULTS========================================#
if str(form.getvalue('image_type_search')) != 'None':
	sql = "SELECT * FROM image NATURAL JOIN detail WHERE type ='" + str(form.getvalue('image_type_search')) + "'"
	cur.execute(sql)
	for row in cur.fetchall():
		print('<form action="viewImage.py">') 														#opens the 'View Image' page
		print('<input id="image_id" name="image_id" type="hidden" value="' + str(row[0]) + '">')	#sets a hidden value to the cgi which is the image_id
		print('<input type="image" src="' + str(row[3]) + '" name="image_stuff" class="btTxt submit" id="image_stuff" width="' + str(row[8]) + '" height="' + str(row[9]) + '"/>')
		print('<p>' + str(row[2]) + '</p>')
		print('</form>')
elif str(form.getvalue('image_start_year_search')) != 'None' and str(form.getvalue('image_end_year_search')) != 'None':
	sql = "SELECT * FROM image NATURAL JOIN detail WHERE year >='" + str(form.getvalue('image_start_year_search')) + "' and year <= '" + str(form.getvalue('image_end_year_search')) + "'"
	cur.execute(sql)
	for row in cur.fetchall():
		print('<form action="viewImage.py">') 														#opens the 'View Image' page
		print('<input id="image_id" name="image_id" type="hidden" value="' + str(row[0]) + '">')	#sets a hidden value to the cgi which is the image_id
		print('<input type="image" src="' + str(row[3]) + '" name="image_stuff" class="btTxt submit" id="image_stuff" width="' + str(row[8]) + '" height="' + str(row[9]) + '"/>')
		print('<p>' + str(row[2]) + '</p>')
		print('</form>')
elif str(form.getvalue('image_artist_search')) != 'None':
	sql = "SELECT * FROM image NATURAL JOIN (SELECT artist_id, name FROM artist) as s1 NATURAL JOIN detail WHERE name ='" + str(form.getvalue('image_artist_search')) + "'"
	cur.execute(sql)
	for row in cur.fetchall():
		print('<form action="viewImage.py">') 														#opens the 'View Image' page
		print('<input id="image_id" name="image_id" type="hidden" value="' + str(row[0]) + '">')	#sets a hidden value to the cgi which is the image_id
		print('<input type="image" src="' + str(row[4]) + '" name="image_stuff" class="btTxt submit" id="image_stuff" width="' + str(row[9]) + '" height="' + str(row[10]) + '"/>')
		print('<p>' + str(row[3]) + '</p>')
		print('</form>')
elif str(form.getvalue('image_location_search')) != 'None':
	sql = "SELECT * FROM image NATURAL JOIN detail WHERE location ='" + str(form.getvalue('image_location_search')) + "'"
	cur.execute(sql)
	for row in cur.fetchall():
		print('<form action="viewImage.py">') 														#opens the 'View Image' page
		print('<input id="image_id" name="image_id" type="hidden" value="' + str(row[0]) + '">')	#sets a hidden value to the cgi which is the image_id
		print('<input type="image" src="' + str(row[3]) + '" name="image_stuff" class="btTxt submit" id="image_stuff" width="' + str(row[8]) + '" height="' + str(row[9]) + '"/>')
		print('<p>' + str(row[2]) + '</p>')
		print('</form>')
elif str(form.getvalue('artist_country_search')) != 'None':
	sql = "SELECT * FROM artist WHERE country ='" + str(form.getvalue('artist_country_search')) + "'"
	cur.execute(sql)
	print('<p>Artist ID --- Name --- Birth Year --- Country --- Description</p>')
	for row in cur.fetchall():
		print('<p>' + str(row[0]) + ' --- ' + str(row[1]) + ' --- ' + str(row[2]) + ' --- ' + str(row[3]) + ' --- ' + str(row[4]) + '</p>')
elif str(form.getvalue('artist_birth_year_search')) != 'None':
	sql = "SELECT * FROM artist WHERE birth_year ='" + str(form.getvalue('artist_birth_year_search')) + "'"
	cur.execute(sql)
	print('<p>Artist ID --- Name --- Birth Year --- Country --- Description</p>')
	for row in cur.fetchall():
		print('<p>' + str(row[0]) + ' --- ' + str(row[1]) + ' --- ' + str(row[2]) + ' --- ' + str(row[3]) + ' --- ' + str(row[4]) + '</p>')

	
#=============================================================================================#

print("</body>")
print("</html>")
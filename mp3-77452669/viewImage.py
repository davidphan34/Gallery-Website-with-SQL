#View Image python file
# - can view the Image Name and details
import pymysql
import cgi

db = pymysql.connect(host='localhost',
                     user='gallery',
                     passwd='eecs118',
                     db= 'gallery')
cur = db.cursor()

form = cgi.FieldStorage()

image_id_str = str(form.getvalue('image_id'))
sql="SELECT * FROM image NATURAL JOIN detail WHERE image_id=" + image_id_str #read from image natural joined with detail table
cur.execute(sql)

row = cur.fetchone()
image_title_pass = str(row[2]) 			#get title from tuple
image_link_pass = str(row[3]) 			#link
image_gallery_id_pass = str(row[4])		#gallery_id
detail_year_pass = str(row[6]) 			#year
detail_type_pass = str(row[7]) 			#type
detail_width_pass = str(row[8])			#width
detail_height_pass = str(row[9]) 		#height
detail_location_pass = str(row[10]) 	#location
detail_description_pass = str(row[11])	#description

detail_artist_id_pass = str(row[5]) #get artist id

sql="SELECT * FROM artist WHERE artist_id=" + detail_artist_id_pass
cur.execute(sql)

artist_row = cur.fetchone()
artist_name_pass = str(artist_row[1]) #get artist name

print("Content-Type: text/html") #HTML is following
print()
print("<html>")
print("<body>")

#link to go to 'Home'
print("<a href='77452669_index.py'>Home</a>")

#Click to go to 'Manage Image'
print('<form action="viewGallery.py">')
print('<button type="submit" name="gallery_id" value ="' + image_gallery_id_pass + '" class="btn-link">View Gallery</button>')
print('</form>')

print('<H1>Title: ' + image_title_pass + '</H1>')										#Title
print('<img id="myimage" src=' + image_link_pass + ' width ="' + detail_width_pass + '" height ="' + detail_height_pass + '">') #setting up image values
print("<p>Image ID:" + str(form.getvalue('image_id')) + "</p>")							#image ID
print('<p id="final_artist">Artist: ' + artist_name_pass + '</p>')						#Artist
print('<p id="final_year">Year: ' + detail_year_pass + '</p>')							#Year
print('<p id="final_location">Location: ' + detail_location_pass + '</p>')				#Location
print('<p id="final_descrip">Brief Description: ' + detail_description_pass + '</p>')	#Description

print('<form action="viewArtist.py">')
#put artist_id into cgi
print('<input id="artist_id" name="artist_id" type="hidden" value="' + detail_artist_id_pass + '">')
print('<input id="image_id" name="image_id" type="hidden" value="' + str(form.getvalue('image_id')) + '">')
print('<input type="submit" value="View more info about Artist" />') #Submit Button
print("</form>")
print("</body>")
print("</html>")
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
print('<form action="viewGallery.py">')
print('<button type ="submit" name ="gallery_id" value ="' + str(form.getvalue("gallery_id")) + '" class="btn-link">Go Back to Gallery View</button></br>')
print("</form>")

print("<H1>Create New Image</H1>")
print('<form action="manageImage.py">')

print("<p>Gallery ID: " + str(form.getvalue('gallery_id')) + "</p>")
if str(form.getvalue('image_title_input')) != 'None':
	print('<p><strong><font size="+3">Image Submitted!!</font></strong></p>')

if str(form.getvalue('image_id_delete')) != 'None':
	print('<p><strong><font size="+3">Image Deleted!!</font></strong></p>')

if (str(form.getvalue('image_title_modify')) != 'None') and (str(form.getvalue('image_link_modify')) != 'None') and (str(form.getvalue('detail_year_modify')) != 'None'):
	print('<p><strong><font size="+3">Image Modified!!</font></strong></p>')

#ensure that gallery_id gets passed through cgi
print('<input id="gallery_id" name="gallery_id" type="hidden" value="' + str(form.getvalue("gallery_id")) + '">')

#============================================Input for Image============================================#
print('<p>--Image Title: <input type="text" name="image_title_input"/></p>')#Input Image Title
print('<p>--Image Link: <input type="text" name="image_link_input"/></p>')	#Input Link
print('<p>--Artist ID: <input type="text" name="image_artist_input"/></p>')	#Input Artist ID

#----------Details for Image----------#
print('<p>Details for Image</p>')
print('<p>--Year: <input type="text" name="detail_year_input"/></p>')				#Input Year
print('<p>--Type: <input type="text" name="detail_type_input"/></p>')				#Input Type
print('<p>--Width: <input type="text" name="detail_width_input"/></p>')				#Input Width
print('<p>--Height: <input type="text" name="detail_height_input"/></p>')			#Input Height
print('<p>--Location: <input type="text" name="detail_location_input"/></p>')		#Input Location
print('<p>--Description: <input type="text" name="detail_description_input"/></p>')	#Input Description
#=======================================================================================================#

if (str(form.getvalue('image_title_input')) != 'None') and (str(form.getvalue('image_link_input')) != 'None') and (str(form.getvalue('detail_year_input')) != 'None') and (str(form.getvalue('detail_type_input')) != 'None'):
	#-----------------------------input into image-----------------------------#
	sql = ("""INSERT IGNORE INTO image(title, link, gallery_id, artist_id) 
	VALUES(%s,%s,%s, %s)""") # %s is a place holder for inserting a variable here
	#get values from the form and put it into  the database
	val = (str(form.getvalue('image_title_input')), str(form.getvalue('image_link_input')), str(form.getvalue('gallery_id')), str(form.getvalue('image_artist_input')))
	cur.execute(sql, val)
	db.commit() #use commit to save the changes you made to the database

	#------------get last tuple------------#
	sql = "SELECT * FROM image ORDER BY image_id DESC"
	cur.execute(sql)
	image_result = cur.fetchone()

	#-----------------------------input into detail-----------------------------#
	sql = ("""INSERT IGNORE INTO detail(image_id, year, type, width, height, location, description) 
	VALUES(%s,%s,%s,%s,%s,%s,%s)""") # %s is a place holder for inserting a variable here
	#get values from the form and put it into  the database
	val = (str(image_result[0]), str(form.getvalue('detail_year_input')), str(form.getvalue('detail_type_input')), str(form.getvalue('detail_width_input')), str(form.getvalue('detail_height_input')), str(form.getvalue('detail_location_input')), str(form.getvalue('detail_description_input')))
	cur.execute(sql, val)
	db.commit() #use commit to save the changes you made to the database

	#------------get last tuple------------#
	sql = "SELECT * FROM detail ORDER BY detail_id DESC"
	cur.execute(sql)
	detail_result = cur.fetchone()

	#------------modify to match detail id of image table to detail table------------#
	sql = "UPDATE image SET detail_id ='" + str(detail_result[0]) + "' WHERE image_id ='" + str(image_result[0]) + "'"
	cur.execute(sql)
	db.commit()

print('<input type="submit" value="Submit" />') #Submit Button

print("</form>")

#==================================================cgi pass for deleting tuple==================================================#
print('<form action="manageImage.py">')
print('</br><p><font size="+2">Delete Image</font></p>')
print('<input id="gallery_id" name="gallery_id" type="hidden" value="' + str(form.getvalue("gallery_id")) + '">')
print('<p>Image ID: <input type="text" name="image_id_delete"/></p>')#Delete Image ID
print('<input name="delete_button" type="submit" value="DELETE IMAGE" />') #Submit Button
print("</form>")

if (str(form.getvalue('image_id_delete')) != 'None'):
	sql = "DELETE FROM image WHERE image_id ='" + str(form.getvalue('image_id_delete')) + "'"
	cur.execute(sql)
	db.commit()
	sql = "DELETE FROM detail WHERE image_id ='" + str(form.getvalue('image_id_delete')) + "'"
	cur.execute(sql)
	db.commit()
#===============================================================================================================================#


#==========================================================Modify for Image==========================================================#
print('<form action="manageImage.py">')
print('</br><p><font size="+2">Modify Image</font></p>')
print('<input id="gallery_id" name="gallery_id" type="hidden" value="' + str(form.getvalue("gallery_id")) + '">')
print('<p>--Image ID of the Image that you want you modify: <input type="text" name="image_id_modify"/></p>')#Image ID
print('<p>--New Image Title: <input type="text" name="image_title_modify"/></p>')		#Modify Image Title
print('<p>--New Image Link: <input type="text" name="image_link_modify"/></p>')	#Modify Link
print('<p>--New Artist ID: <input type="text" name="image_artist_modify"/></p>')	#Modify Link

#----------Modify Details for Image----------#
print('<p>Modify Details for Image</p>')
print('<p>--New Year: <input type="text" name="detail_year_modify"/></p>')				#modify Year
print('<p>--New Type: <input type="text" name="detail_type_modify"/></p>')				#modify Type
print('<p>--New Width: <input type="text" name="detail_width_modify"/></p>')			#modify Width
print('<p>--New Height: <input type="text" name="detail_height_modify"/></p>')			#modify Height
print('<p>--New Location: <input type="text" name="detail_location_modify"/></p>')		#modify Location
print('<p>--New Description: <input type="text" name="detail_description_modify"/></p>')#modify Description

print('<input type="submit" value="Modify Image" />') #Submit Button
print("</form>")

if (str(form.getvalue('image_title_modify')) != 'None') and (str(form.getvalue('image_link_modify')) != 'None') and (str(form.getvalue('detail_year_modify')) != 'None'):
	sql = "UPDATE image SET title ='" + str(form.getvalue('image_title_modify')) + "', link ='" + str(form.getvalue('image_link_modify')) + "' WHERE image_id ='" + str(form.getvalue('image_id_modify')) + "'"
	cur.execute(sql)
	db.commit()
	sql = "UPDATE detail SET year ='" + str(form.getvalue('detail_year_modify')) + "', type ='" + str(form.getvalue('detail_type_modify')) + "', width ='" + str(form.getvalue('detail_width_modify')) + "', height ='" + str(form.getvalue('detail_height_modify')) + "', location ='" + str(form.getvalue('detail_location_modify')) + "', description ='" + str(form.getvalue('detail_description_modify')) + "' WHERE image_id ='" + str(form.getvalue('image_id_modify')) + "'"
	cur.execute(sql)
	db.commit()
#====================================================================================================================================#




print("</body>")
print("</html>")
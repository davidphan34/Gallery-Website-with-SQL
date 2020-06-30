#View Gallery python file
# - can view the Gallery Name and Description
# - can view the images in Gallery
# - can go to 'Manage Image'
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

sql="SELECT * FROM gallery" #read from gallery table
cur.execute(sql)

for row in cur.fetchall(): 								#grab from all the tuples
	if str(row[0]) == str(form.getvalue('gallery_id')): #if the ID matches
		gallery_name = str(row[1]) 						#set variable for gallery name
		gallery_description = str(row[2]) 				#set variable for gallery description

print("<H1>Gallery '" + gallery_name + "'</H1>") 						#set gallery_name as Header
print("<p> Description: " + gallery_description + "</p>")				#set gallery description
print("<p> Gallery ID: " + str(form.getvalue('gallery_id')) + "</p>")	#set gallery id

sql="SELECT * FROM image NATURAL JOIN detail WHERE gallery_id = " + str(form.getvalue('gallery_id')) #make sure it's all from the gallery we are viewing
cur.execute(sql)
num_of_images = 0
for row in cur.fetchall():
	num_of_images = num_of_images + 1
print("<p> There are " + str(num_of_images) + " image(s) in this Gallery</p>")

#Click to go to 'Manage Image'
print('<form action="manageImage.py">')
print('<button type="submit" name="gallery_id" value ="' + str(form.getvalue('gallery_id')) + '" class="btn-link">Manage Images</button>')
print('</form>')

#natural join the image and detail tables to get information needed
sql="SELECT * FROM image NATURAL JOIN detail WHERE gallery_id = " + str(form.getvalue('gallery_id')) #make sure it's all from the gallery we are viewing
cur.execute(sql)
for row in cur.fetchall():
	print('<form action="viewImage.py">') 														#opens the 'View Image' page
	print('<input id="image_id" name="image_id" type="hidden" value="' + str(row[0]) + '">')	#sets a hidden value to the cgi which is the image_id
	print('<input type="image" src="' + str(row[3]) + '" name="image_stuff" class="btTxt submit" id="image_stuff" width="' + str(row[8]) + '" height="' + str(row[9]) + '"/>')
	print('<p>' + str(row[2]) + '</p>')
	print('</form>')																			#sets the image to submit with other formatting stuff for the image

print("</body>")
print("</html>")
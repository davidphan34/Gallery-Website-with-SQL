#Manage Galleries python file
# - can put in a new gallery
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
print("<a href='listGalleries.py'>Go Back</a>")

#display that Gallery is Modified
if str(form.getvalue('gallery_name_modify')) != 'None': #to ensure that we're putting something in the table
	print("<H1><font color='red'>Gallery Modified!!</font></H1>")
	
#display if Gallery is Added
if str(form.getvalue('gallery_name_input')) != 'None': #to ensure that we're putting something in the table
	print("<H1><font color='red'>Gallery Added!!</font></H1>")

#------------------------------------------Input for Gallery------------------------------------------#
print("<H1>Create New Gallery</H1>")
print('<form action="manageGallery.py">')

print('<p>--Gallery Name: <input type="text" name="gallery_name_input"/></p>')         	 		#Input Gallery Name
print('<p>--Gallery Description: <input type="text" name="gallery_description_input"/></p>')	#Input Description

print('<input type="submit" value="Submit" />') #Submit Button

print("</form>")

#sql queries
if str(form.getvalue('gallery_name_input')) != 'None':
	sql = ("""INSERT IGNORE INTO gallery(name, description) 
	VALUES(%s,%s)""") # %s is a place holder for inserting a variable here
	#get values from the form and put it into  the database
	val = (str(form.getvalue('gallery_name_input')), str(form.getvalue('gallery_description_input')))
	cur.execute(sql, val)
	db.commit() #use commit to save the changes you made to the database
#-----------------------------------------------------------------------------------------------------#



#------------------------------------------Modify Gallery Details------------------------------------------#
print("</br><H1>Modify Gallery</H1>")
print('<form action="manageGallery.py">')
print('<p>--Gallery ID for Gallery to be modified: <input type="text" name="gallery_id_modify"/></p>') 
print('<p>--New Gallery Name: <input type="text" name="gallery_name_modify"/></p>')         	 	#modify Gallery Name
print('<p>--New Gallery Description: <input type="text" name="gallery_description_modify"/></p>')	#modify Description

print('<input type="submit" value="Submit" />') #Submit Button

print("</form>")

if str(form.getvalue('gallery_id_modify')) != 'None':
	sql = "UPDATE gallery SET name ='" + str(form.getvalue('gallery_name_modify')) + "', description ='" + str(form.getvalue('gallery_description_modify')) + "' WHERE gallery_id ='" + str(form.getvalue('gallery_id_modify')) + "'"
	cur.execute(sql)
	db.commit()
#-----------------------------------------------------------------------------------------------------#




print("</body>")
print("</html>")



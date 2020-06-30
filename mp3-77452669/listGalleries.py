#David Phan
#77452669
#20 November 2019
#python file to list the galleries
# - Can go to 'Manage Galleries'
# - Can go to 'View Gallery'
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

#link to go to 'Manage Galleries'
print("<a href='manageGallery.py'>Manage Galleries</a>")

#link to go to 'Search'
print("<a href='search.py'>Search</a>")


print("<H1>List of Galleries</H1>")

sql="SELECT * FROM gallery" #read from gallery table
cur.execute(sql)

print("<p>Gallery ID --- Name --- Description</p>")

print('<form action="viewGallery.py">')
for row in cur.fetchall(): #grab from all the tuples
	print('<button type ="submit" name ="gallery_id" value ="' + str(row[0]) + '" class="btn-link"> ' 
		+ str(row[0]) + ' --- ' + str(row[1]) + ' --- ' + str(row[2]) + '</button></br>')
	#print("<a href='http://localhost:8080/test/cgi-bin/viewGallery.py?gallery_name=" + str(row[1]) + "'>" + str(row[1]) + "</a>")
	#print("<p>" + str(row[0]) + " --- " + str(row[1]) 
		#+ " --- " + str(row[2]) + "</p>")
#print("<input type = 'submit' value = 'Go to Gallery'>")

print("</form>")
print("</body>")
print("</html>")

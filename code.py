##C:\Users\piyus\OneDrive\Documents\GitHub\IITCAssignment\430\Project\code.py
"""Implement bfs's algorithm for finding shortest path between 2 station in NY subway problem ,which is the Main project for the problem
1)	Graph ,it has vertices and edge, in vertices we gave -1 to those which dosn't have relation. vertices has values with its equivalent index that we can use to find the edge value
2)	bfs method with 3 parameterss, 1st is base node,from where the analysis should start, 2nd is all the vertices and in the end is all the edge
3)	Exeution section
"""
"""------------------------------------------
...
....Fetch Data from user
.....input param : void   
.....Output :    returns data inserted by the user
----------------------------------------------"""
def fetchStopId():
	data = input("Enter Station Name : ")
	mycur.execute("select stop_id,stop_name from padb.stop_master where stop_name like '%" + data +"%' and location_type = 1")
	##return [str(record[0]) for record in mycur.fetchall()]
	return mycur.fetchall()


def matrix():
	vertices=station.keys()
	edges=[]

	mycur.execute("select src_stop_id,dest_stop_id,duration from subway_graph;")
	x= mycur.fetchall()
	for i1,i in enumerate(vertices):
		r=[]
		for i2,j in enumerate(vertices):
			##row_count=mycur.execute("select distinct duration from subway_graph where src_stop_id='"+i+"' and dest_stop_id='"+j+"';")
			##a= mycur.fetchall()
			for row in x:
				if row[0]==i and row[1]==j:
					r.append(row[2])
				else:
					r.append(-1)
			"""if a:
				r.append(a)
			else:
				r.append(-1)
		edges[i1]=r"""
	print (edges)
##def graphVal():

	##for a in s:
	##	graph.setdefault(a[0],a[1])


def bfsPath(sourceStation,destinationStation):
	stack=[] #empty Stack to maintain the paths
	exploredNode =set() #explored node
	stack.append([sourceStation])
	while stack:
		path=stack.pop(0) #Popout the first element from the stack
		node = path[-1] #Consider the right most element of the path
		if node == destinationStation:
			return path
			"""return 'Optimum path to reach from ' + str(sourceStation) +' to ' +\
 str(destinationStation) + ' is '+ str(path)"""
		##logic to get associated nodes
		g=[]
		##print (graph)
		for a in graph:
			if (a[0]==node):
				g.append(a[1])
		for nxtNodes in g:
		    #To avoid circular loop and not to enter node which is already explored
		    if nxtNodes not in exploredNode:
			    newpath = list(path)
			    newpath.append(nxtNodes)
			    stack.append(newpath)
		exploredNode.add(node)
		##print (exploredNode)
	##return 'Path Not found'
	return 

print("hello")
import mysql.connector
conn=mysql.connector.connect(user='root',password='gadha',host='localhost',database='padb')
mycur=conn.cursor()
mycur.execute("select  stop_id,stop_name from stop_master where location_type=1;")
s = mycur.fetchall()
station ={}
graph={}
for a in s:
	station.setdefault(a[0],a[1])
	
mycur.execute("select distinct src_stop_id,dest_stop_id,src_stop_route_id,duration from subway_graph;")
graph = mycur.fetchall()
##print(graph)

##print (station)	
##mycur.execute("select * from  padb.subway_graph")
print ("---------Source Station ------------")
source = fetchStopId()
for i,tempSource in enumerate(source):
	print(str(i)+':\t'+str(tempSource))
indexSource=int(input("Please Enter Index of source ..:\t\a"))
print ("---------Destination Station ------------")
destination = fetchStopId()
#print(destination)
for i,tempSource in enumerate(destination):
	print(str(i)+':\t'+str(tempSource))
indexDest=int(input("Please Enter Index of Destination ..:\t\a"))
sourceStation=source[indexSource][0]
destinationStation=destination[indexDest][0]
path= bfsPath(sourceStation,destinationStation)

if path:
	totalTimeTaken=0
	print ('Optimum path to reach from ' + station[sourceStation] +' to ' +\
 station[destinationStation] + ' is :')
	prevStation=''
	prevLine=0
	for a in path:
		currLine=0
		print(station[a])
		if (prevStation !=''):
			for b in graph:
				if (b[0]==prevStation and b[1]==a):
					totalTimeTaken+=b[3]
					currLine=b[2]
					print('\t\tPrevious Station :'+station[prevStation]+' |  Time Taken :'+str(b[3])+' |  Line # :'+str(b[2]))
					break
			
			if (prevLine!=0 and prevLine!=currLine):
				totalTimeTaken+=60 ##additing time for line change
				print("--------Line Change--------")
		prevLine=currLine
		prevStation=a
		
else:
	print('Path not found')
	
print('\n Total Time taken to reach to destination is \t\a:'+str(totalTimeTaken) +' sec')
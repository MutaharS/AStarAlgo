import math
import time
import json
import functions
import matplotlib.pyplot as plt
from collections import deque

# Syed Mutahar Shah, assignment done with no partner

########################FUNCTIONS########################
# Calculates the distance between two nodes in the graph
def dist_between_nodes(node1,node2):
    x1 = int(name_to_coord[node1][0])   # get the x value of node1
    y1 = int(name_to_coord[node1][1])   # get the y value of node1
    x2 = int(name_to_coord[node2][0])   # get the x value of node2
    y2 = int(name_to_coord[node2][1])   # get the y value of node 2
    return euclidean(x1,y1,x2,y2)       # return the euclidean distance between the nodes

# A star algorithm using the shortest distance 
# shortest_distance(adjacency_list, start node, end node, boolean value for step-by-step print)
def shortest_distance(graph, start, end, printout):
    cost[start] = 0                                 # set the path to initial node as zero
    fn[start] = cost[start] + dist_to_goal[start]   # fn = distance travelled + heuristic
    undiscovered = set()                            # set of undiscovered nodes
    discovered = []                                 # list of discovered nodes
    explored = set()                                # set of all nodes that have been explored (expanded nodes)
    parent = {}                                     # map of node to its parent (used to trace the optimal path after)
    # Mark all vertices as undiscovered
    for item in graph:                              # for every node in the graph:
        undiscovered.add(item)                      # add the node to the undiscovered set
    # Add root node to discovered set
    undiscovered.remove(start)                      # start by adding start node to discovered list
    discovered.append(start)                        # (remove from undiscovered simultaneously)

    # Choose cheapest fn_value node 'v' in discovered nodes, set it as explored and remove from discovered
    while(len(discovered) > 0):                     # while there are still nodes to explore:
        temp = []                                   #   temporary list to hold the fn_values of discovered nodes
        for v in discovered:                        #   for each node 'v' in discovered
            temp.append(int(fn[v]))                 #       add its fn value to the temp list
        cheapest = min(temp)                        #   Let cheapest be the minimum value of the list of fn values
        # temp.index(cheapest) will be the index of the cheapest fn value in temp, the indices of discovered and temp 
        # correspond to the same node, so v becomes the node at discovered[index] where index = temp.index(cheapest)
        v = discovered[temp.index(cheapest)]        
        explored.add(v)                             # Add v to the explored list, since we will now expand the node
        discovered.remove(v)                        # remove it from discovered now that it has been added to explored

        # If the cheapest node found is the target node 'O', then we are done since we have found that the
        # cheapest fn to follow is the target node, no better path can exist
        if(v == "O"):
            break
        
        # This is for the printout at the end if the user selects to have a step-by-step solution
        string = ""
        string2 = ""
        t = adj_list[v]
        for n in t:
            string = string + str(n) + " "

        # For each neighbor of v, add to discovered if not already found
        for n in adj_list[v]:                       # For each neighbor node of node v:
            if(n in undiscovered):                  #   if the neighbor is undiscovered:
                undiscovered.remove(n)              #       remove from undiscovered
                discovered.append(n)                #       add it to discovered list
            if(n in explored):           
            # if an item has been added to explored, it must have been the cheapest option, 
            # and thus could not find a better path for it, so we can continue to next neighbor            
                continue
            # Otherwise calculate the fn_value and update its parent if it is a better fn_value
            # cost[v] is the distance to v on this path from start, 
            # cost[n] is the distance from start to v, plus the distance from v to n
            cost[n] = cost[v] + dist_between_nodes(v,n)     
            # Now f(n) = dist_trav + heuristic
            fn_value = cost[n] + dist_to_goal[n]

            # Update values if necessary
            if(fn[n] == -1 or fn[n] > fn_value): # If we have not yet calculated fn or if we have found a shorter route to n:
                parent[n] = v                    #    update parent of n as v (for optimal path finding)
                fn[n] = fn_value                 #    update fn value of node n

        # This is for print if step-by-step selected, will print out each possible path and its values
        for n in discovered:
                string2 = string2 + str(n) + "(" + str(fn[n]) + ") "
        if(printout):
            print("*************************************************************")
            print("City selected: " + v)
            print("Possible nodes to travel: " + string)
            print("Node at end of best possible path: ")
            print(string2)
            print("*************************************************************\n")
    return trace(parent,start,end)  # At end of A star return path from the start node to the end node

# Trace(map of node to its parent, start node, end node) (works backward from target node to start node to find path)
def trace(parent, start, end):
    path = []                   # start with empty path
    node = end                  # current node is the end node "O"
    while(node != start):       # while the current node is not the start node:    
        path.append(node)       #    append the current node to path
        node = parent[node]     #    current node is set as parent of current node
    path.append(node)           # Once we have reached the start node, we also append the start node to path
    path.reverse()              # since path elements were appended backwards, must reverse the path
    return path                 # return the final optimal path

# Print the final solution path in two ways depending on algorithm used (fewest nodes or shortest distance)
def final_path_print(path,selection):
    path_total = 0
    # selection = 0 is fewest nodes, selection = 1 is shortest_distance
    if(selection):
        print("The final solution path is: ")
        for i in range(0,len(path)-1):
            path_total = path_total + dist_between_nodes(path[i],path[i+1])
            print(path[i] + " to " + path[i+1] + " distance: " + str(dist_between_nodes(path[i],path[i+1])))
    else:
        print("The final solution path is: ")
        for i in range(0,len(path)-1):
            path_total = path_total + 1
            print(path[i] + " to " + path[i+1] + " distance: " + str(1))
    print("Total path length: " + str(path_total))
    
# Calculate the euclidean distance between two points (x1,y1) and (x2,y2)
def euclidean(x1,y1,x2,y2):
    return math.sqrt( (x2-x1)**2 + (y2-y1)**2 )

# Fewest nodes algorithm
def fewest_nodes(graph, start, end, printout):
    q = deque()                                     # Create a queue
    undiscovered = set()                            # undiscovered set
    discovered = set()                              # discovered set
    explored = set()                                # explored set
    parent = {}                                     # map of node to its parent
    # Mark all vertices as undiscovered     
    for item in graph:
        undiscovered.add(item)
    # Add initial vertex to queue and mark as discovered
    q.append(start)                                 # append start to queue
    undiscovered.remove(start)                      # remove start from undiscovered
    discovered.add(start)                           # add start node to discovered
    while(len(q) > 0):                              # while the q is not empty
        v = q.popleft()                             # let v be the node at the  head of the queue
        explored.add(v)                             # add v to the explored set
        string = ""                                 # used for printing                         
        for n in adj_list[v]:                       # for each neighbor node n of node v:
            string = string + n + " "               #   add the neighbor to string that will be printed
            if(n in undiscovered):                  #   if the neighbor node is undiscovered:
                parent[n] = v                       #       set the parent of n as v
                undiscovered.remove(n)              #       remove n from undiscovered set
                discovered.add(n)                   #       add n to to discovered set
                q.append(n)                         #       append n to the queue
            if(n == end):                           # if the neighbor n is the end node
                return trace(parent, start, end)    #    return the path from start to end
        if(string != "" and printout == 1):         # if user wants the step-by-step
            print("City selected: " + v)            #   print the possible paths at each step
            print(string)

########################END OF FUNCTIONS########################

# Data structures needed
names = []              # Names contains the name of the corresponding node at maze[r][c]
direction = []          # Direction contains the direction of arrow of node at maze[r][c]
coordinates = []        # Coordinates contains the (x,y) pair of node at maze[r][c]
distance_heuristic = [] # Contains the distance of the corresponding node at maze[r][c]
dist_to_goal = {}       # Map node name to distance_heuristic (e.g. dist_to_goal["R0"] = 193.2175)
name_to_coord = {}      # Maps the node name to its coordinate  
adj_list = {}           # Adjacency list mapping nodes to their neighbors 
cost = {}               # for calculating distance travelled on path

# Contents of maze.txt in the form of multiple 2D arrays
# I can then iterate over each element of the matrix, creating nodes as well as their edges using
# the information contained in each cell
# information will also be used to create a list of nodes to heuristic value

# First read in the maze.txt file and load the necessary data
filein = open("maze.txt", "r")                  # open maze.txt for reading
fileout = open("out.txt", "w")                  # open out.txt for writing (will contain the adjacency list for reference)
header = filein.readline()                      # let header be the first line that contains rows and columns of maze
header = header.split(" ")                      # split the header by spaces
rows = int(header[0])                           # the first element of header is the number of rows
cols = int(header[1])                           # the seconds element of header is the number of columns

# Process the data and store into the above data structures
for line in filein:                             # for every line in maze.txt:
    name_row = []                               #   a row of names as a list
    direction_row = []                          #   a row of directions as a list
    coordinate_row = []                         #   a row of coordinates as a list
    cur_row = line.split(" ")                   #   split the line by spaces
    # cur_row now contains each element of the current row of maze.txt
    # i.e. cur_row = [R0-S-31-40, R1-W-31-55, ..., R6-S-31-69, R7-NW-31-102 ]
    for item in cur_row:                        # for every item (which is a node) in current row:
        details = item.split("-")               #   let details be a list splitting the node by dashes
        # e.g. on first iteration: details = [R6,S,31,69]
        if(details.count("\r\n") > 0):  # at some point details will contain the carriage return and newline, then break
            break
        d1,d2,d3,d4 = details                   # e.g. d1 = R6, d2 = S, d3 = 31, d4 = 69
        name_row.append(d1)                     # append the name of the node to name_row
        direction_row.append(d2)                # append the direction to direction_row
        coordinate_row.append([d3,d4])          # append the coordinate as a pair to coordinate_row
    names.append(name_row)                      # append the name_row to the names list structure
    direction.append(direction_row)             # append the direction_row to the direction list structure
    coordinates.append(coordinate_row)          # append the coordinate_row to the coordinates list structure
    # Thus, we are constructing the names, direction, and coordinate matrices (list of list) row by row

# Create matrix of distance heuristics for each node,
# will later use this to map each node name to its distance heuristic

g_x = int(coordinates[rows-1][cols-1][0])   # Goal x coordinate
g_y = int(coordinates[rows-1][cols-1][1])   # Goal y coordinate

# Iterate over each node of the maze and find straight line distances
for row in coordinates:                         # for each row in coordinates:       
    cur_row = []                                #    temporary current row as list
    for i in range(0,cols):                     #    for every item in the current row:
        #print("X: " + str(row[i][0]) + " Y: " + str(row[i][1]))
        x = int(row[i][0])                      #    x = the x value of the node at maze[r][c]
        y = int(row[i][1])                      #    y = the y value of the node at maze[r][c]
        cur_row.append(euclidean(x,y,g_x,g_y))  # Calculate straight line distance from current node to target node
    distance_heuristic.append(cur_row)            # Construct heuristic matrix row by row

# Map the node name to its coordinate, as well as to its heuristic value
# e.g. name_to_coord["R0"] = [31,40]
#      dist_to_goal["R0"]  = 193.217
for r in range(0,rows):
    for c in range(0, cols):
        name_to_coord[names[r][c]] = coordinates[r][c]
        dist_to_goal[names[r][c]] = distance_heuristic[r][c]
        
# Set up the adjacency list structure by creating an empty neighbor list for each node
for row in names:
    for element in row:
        adj_list[element] = []

# Use to add appropriate edges to nodes (refer to functions.py for function definition)
functions.construct_list(adj_list,names,direction,rows,cols)

# Write out the adjacency list to check that edges are created properly, written to out.txt
for v, n in adj_list.items():
    fileout.write(str(v) + ' >>> '+ str(n) + '\n')

# for keeping track of fn_values
fn = {}                 
for v in adj_list:      # Sentinel value of -1 for uninitialized fn value
    fn[v] = -1

# At this point the adjacency list is completely created, and all data has been processed
# Now we get user input and apply the appropriate algorithm
print("Welcome to the A* algorithm simulator!")
start = raw_input("Please type the start node (e.g. 'R0') : ")      # start node
step = raw_input("Would you like a step-by-step solution? (y/n): ") # step-by-step = y or n
prnt = 0                                                            # print out variable

if(step == 'y'):        # If the user wants step by step:
    prnt = 1               #   prnt = 1 (printout is true)
else:                   # else:
    prnt = 0               #   prnt = 0 (printout is false)

# heur represents heuristic to use
heur = input("Select the heuristic to use (1 - fewest nodes, 2 - straight-line distance): ")
path = []
if(heur == 1):                                              # if heur is 1, use fewest nodes algorithm:
    path = fewest_nodes(adj_list, start, "O", prnt)         # Path contains optimal path after calling algorithm
    if(path != None):                                       #   if a path was found:
        final_path_print(path,0)                            #       print the final solution path for fewest node
if(heur == 2):                                              # if heur is 2:
    path = shortest_distance(adj_list, start, "O", prnt)    #    use shortest_dist algorithm
    if(path != None):                                       #    if path was found:
        final_path_print(path,1)                            #       print the final solution path for shortest_distance

# If a path was not found from start to target then print below
# otherwise plot the points and show animate the path taken
if(path == None):
    print("No path to target node exists")
else:
    path_x = []                                     # List of optimal path x values used for animating path
    path_y = []                                     # List of optimal path y values used for animating path
    x = []                                          # List of x coordinates of every node
    y = []                                          # List of y coordinates of every node
    # x[i] along with y[i] are the (x,y) will be the coordinate of node i, need in this form to plot using scatter
    for point in name_to_coord:                 # For every node e.g. R0, B16, etc :
        x.append(name_to_coord[point][0])       #   append the x value to x[]
        y.append(name_to_coord[point][1])       #   append the y value to y[]

    fig, ax = plt.subplots()                    # create matplot, subplots

    # scatter used to plot the points on the figure marker sets the point shape to be diamonds, c="red" sets the color
    # of the points to be red, alpha sets the trasparency to be 50% 
    plt.scatter(x, y, marker="D", c="red",alpha=0.5)     
    plt.ion()   # sets the plot to be interactive which allows plotting of the line for animating path
    plt.show()  # shows the plot

    # Animate the solution path by adding line between each node in the coordinates of (path_x,path_y)
    for node in path:                               # For every node in optimal path:
        path_x.append(name_to_coord[node][0])       # append node's x value to path_x
        path_y.append(name_to_coord[node][1])       # append node's y value to path_y
        ax.plot(path_x, path_y, 'black', linestyle='-', marker='')      # plot the current path travelled
        plt.pause(1)                                # update plot, pause for 1 s, then continue loop
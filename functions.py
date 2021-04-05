def construct_list(adj_list,names,direction,rows,cols):
    # Fill the adjacency list structure using the directions/colors provided
    for i in range(rows):
        for k in range(cols):
            currentNode = names[i][k]
            color = currentNode[0]
            if (color == 'O'): 
                break

            cur_row = i
            cur_col = k

            # Scan towards direction of arrow
            if(direction[i][k] == "N"):
                while(cur_row-1 >= 0):
                    cur_row = cur_row - 1
                    p_neighbor = names[cur_row][cur_col]
                    if(p_neighbor[0] != color):
                        adj_list[currentNode].append(p_neighbor)
            if(direction[i][k] == "W"):
                while(cur_col-1 >= 0):
                    cur_col = cur_col - 1
                    p_neighbor = names[cur_row][cur_col]
                    if(p_neighbor[0] != color):
                        adj_list[currentNode].append(p_neighbor)
                #print("Heading west")
            if(direction[i][k] == "S"):
                while(cur_row+1 < rows):
                    cur_row = cur_row + 1
                    p_neighbor = names[cur_row][cur_col]
                    if(p_neighbor[0] != color):
                        adj_list[currentNode].append(p_neighbor)
                #print("Heading south")
            if(direction[i][k] == "E"):
                while(cur_col+1 < cols):
                    cur_col= cur_col + 1
                    p_neighbor = names[cur_row][cur_col]
                    if(p_neighbor[0] != color):
                        adj_list[currentNode].append(p_neighbor)
                #print("Heading east")
            if(direction[i][k] == "NW"):
                while(cur_row-1 >= 0 and cur_col-1 >= 0):
                    cur_row = cur_row - 1
                    cur_col = cur_col - 1
                    p_neighbor = names[cur_row][cur_col]
                    if(p_neighbor[0] != color):
                        adj_list[currentNode].append(p_neighbor)
                #print("Heading north-west")
            if(direction[i][k] == "NE"):
                while(cur_row-1 >= 0 and cur_col+1 < cols):
                    cur_row = cur_row - 1
                    cur_col = cur_col + 1
                    p_neighbor = names[cur_row][cur_col]
                    if(p_neighbor[0] != color):
                        adj_list[currentNode].append(p_neighbor)
                #print("Heading north-east")
            if(direction[i][k] == "SW"):
                while(cur_row+1 < rows and cur_col-1 >= 0):
                    cur_row = cur_row + 1
                    cur_col = cur_col - 1
                    p_neighbor = names[cur_row][cur_col]
                    if(p_neighbor[0] != color):
                        adj_list[currentNode].append(p_neighbor)
                #print("Heading south-west")
            if(direction[i][k] == "SE"):
                while(cur_row+1 < rows and cur_col+1 < cols):
                    cur_row = cur_row + 1
                    cur_col = cur_col + 1
                    p_neighbor = names[cur_row][cur_col]
                    if(p_neighbor[0] != color):
                        adj_list[currentNode].append(p_neighbor)
                #print("Heading south-east")
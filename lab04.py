# [['+', '-'], ['+', '+']]. First list is index 0, next is index 1.
# In this case, maze[0, 1] would give us the '-'. 
# Top left most element is [0][0], bottom most element is [n-1][n-1] index.
# x up and down is north(-) south(+)
# y up and down is east(+) west(-)
from Stack import Stack

def printMaze(maze):
	for row in range(len(maze)):
		for col in range(len(maze[0])):
			print("|{:<2}".format(maze[row][col]), sep='',end='')
		print("|")
	return

def solveMaze(maze, start_x, start_y):
    
    steps = 1 # keep track of the number of steps taken. initialize to 1. 

    if maze[start_x][start_y] == 'G':
         return True
    elif maze[start_x][start_y] == ' ':
         maze[start_x][start_y] = steps
    else:
         return False

    stack = Stack() # start at the given starting position
    stack.push([start_x, start_y])

    while not stack.isEmpty():
        x, y = stack.peek() # get the top position on the stack
        
        # check the adjacent positions counterclockwise starting from North
        if maze[x-1][y] == ' ':  # North
            steps += 1 # increment the step count. Steps is now added by 1.
            maze[x-1][y] = steps # update the maze with the new step count.
            stack.push([x-1, y]) # push the new position onto the stack

        elif maze[x-1][y] == 'G':  # North
             return True
        
        elif maze[x][y-1] == ' ': # West
            steps += 1
            maze[x][y-1] = steps
            stack.push([x, y-1])
            
        elif maze[x][y-1] == 'G':  # West
             return True
        
        elif maze[x+1][y] == ' ':  # South
            steps += 1
            maze[x+1][y] = steps
            stack.push([x+1, y])
            
        elif maze[x+1][y] == 'G':  # South
             return True
        
        elif maze[x][y+1] == ' ': # East
            steps += 1
            maze[x][y+1] = steps
            stack.push([x, y+1])
            
        elif maze[x][y+1] == 'G':  # East
             return True
        
        else:
            stack.pop() # removes the element from the stack. 

    return False # if we reach this point, there is no path to the goal

# maze = [
# ['+','+','+','+','G','+'],
# ['+',' ','+',' ',' ','+'],
# ['+',' ',' ',' ','+','+'],
# ['+',' ','+','+',' ','+'],
# ['+',' ',' ',' ',' ','+'],
# ['+','+','+','+','+','+'] ]

# if solveMaze(maze, 4, 4):
#     print("Solved")
# else:
#     print("No solution")

# printMaze(maze)
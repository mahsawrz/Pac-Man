from queue import *

env = []            #This(global variable) list has the current status(- * f) of each house(environment)
q = Queue()         #This(global variable)


def Environment(action='U'):                     #This function can get the new position of the agent and the status of that house.

    hasFood = False                              #Boolean variable to determine whether food is or is not
    (current_position, taken_path) = q.get()     #The tuple is for accessing to agent current position and the path that traversed
    (row, column) = current_position             #Save the position of the agent in row and column

    if env[row][column] == 'f':
        hasFood = True

    #This function returns the position of the agent and the food that the house has and the path it has traveled
    return (row, column), hasFood, taken_path


def Agent(pacman_position):                       #This function obtains the path length along with the list of the path itself.

    q.queue.clear()
    q.put((pacman_position, [pacman_position]))   #The position of the agent is in the queue both as the starting point and the beginning of the path
    situation_checked = set([pacman_position])    #This set maintains houses that have already been visited

    while not q.empty():

        (row, column), hasFood, taken_path = Environment('U')

        #If in the current position of the agent, there is food that returns the length of the path and the path itself.
        # Otherwise one of the top, bottom, left, right actions must be selected due to the absence of a wall and the previously
        # unseen appearance of the house.(not in situation_checked Set )
        if hasFood == True:
            return len(taken_path), taken_path
        for counter_position in [(row, column + 1), (row + 1, column), (row, column - 1), (row - 1, column)]:
            if counter_position not in situation_checked \
                    and env[counter_position[0]][counter_position[1]] != '*':
                q.put((counter_position, taken_path + [counter_position]))
                situation_checked.add(counter_position)

    return 0, []


def main():
    r = 0
    c = 0
    pacman_position = (-1, -1)              #First we assume that the agent does not exist in the environment

    file_env1 = open(r"D:\env1.txt", mode='r')
    file_env2 = open(r"D:\env2.txt", mode='r')
    file_env3 = open(r"D:\env3.txt", mode='r')
    file_env4 = open(r"D:\env4.txt", mode='r')
    files_list = [file_env1, file_env2, file_env3, file_env4]

    for f in files_list:
        env.clear()                            #Clears the list from the previous environment each time
        lines = f.readlines()
        file_row = 0                          #We use this variable to know which file line we are
        for l in lines:
            if file_row == 0:                 #If we are in the first line of the file
                file_firstRow = l.split(',')  #From the first line of the file, we find the number of rows and columns
                r = int(file_firstRow[0])
                c = int(file_firstRow[1])
                file_row += 1                 #We scroll the file, so we go to the next line
            else:
                if (l.find('a') != -1):       #If the agent is in the environment

                    #We subtracted from one line because from the second line,
                    # the environment starts and the first line is extra.

                    pacman_position = (file_row - 1, l.find('a'))   #Found the position of the agent
                    l = l.replace('a', '-')                         #The agent is in motion, so we empty the agent position

                env.append(l)
                file_row += 1

        (taken_path_length, taken_path) = Agent(pacman_position)

        # Puts each of the traversed paths in this variable.
        # We move the counters one by one to start from one
        taken_path = [(i + 1, j + 1) for i, j in taken_path]


        print(f"The length of the path pacman has taken in {taken_path[0]} location is => {taken_path_length}")
        print(f"The path is: {taken_path}\n\n")




if __name__ == '__main__':
    main()


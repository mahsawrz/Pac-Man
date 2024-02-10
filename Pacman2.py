from random import *
from queue import *

env = []
q = Queue()



def Environment(action='U'):     #This function can get the new position of the agent and the status of that house.

    hasFood = False
    current_position, taken_path = q.get()
    row, column = current_position

    if env[row][column] == 'f':
        hasFood = True

    return (row, column), hasFood, taken_path


def Agent(pacman_position):      #This function obtains the path length along with the list of the path itself.

    q.queue.clear()
    q.put((pacman_position, [pacman_position]))
    situation_checked = set([pacman_position])

    while not q.empty():

        (row, column), hasFood, taken_path = Environment('U')

        if hasFood == True:
            return len(taken_path), taken_path
        for counter_position in [(row, column + 1), (row + 1, column), (row, column - 1), (row - 1, column)]:
            if counter_position not in situation_checked \
                    and env[counter_position[0]][counter_position[1]] != '*':
                q.put((counter_position, taken_path + [counter_position]))
                situation_checked.add(counter_position)

    return 0, []


def main():

    m = int(input('Please enter the number of rows : '))
    n = int(input('Please enter the number of columns : '))

    for i in range(m):
        line = []
        for j in range(n):
            if (i == 0 or i == m - 1 or j == 0 or j == n - 1): #There should be a wall around the environment.
                line.append('*')
            else:
                #Fill the surrounding houses
                if (random() < 0.7):
                    line.append('-')
                else:
                    line.append('*')

        env.append(line)

    row = randint(1, m - 2)
    col = randint(1, n - 2)
    env[row][col] = 'a'
    pacman_position = (row, col)
    res = False

    while (not res):

        #We remove the walls around the environment => m-2/n-2
        row = randint(1, m - 2)
        col = randint(1, n - 2)
        if (env[row][col] != 'a'):
            env[row][col] = 'f'
            res = True

    taken_path_length, taken_path = Agent(pacman_position)
    taken_path = [(i + 1, j + 1) for i, j in taken_path]

    print(f"Path Lenght: {taken_path_length}")
    print(f"Path: {taken_path}\n\n")



if __name__ == '__main__':
    main()


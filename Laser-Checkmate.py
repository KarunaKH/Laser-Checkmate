import copy
gameboard=[]
f = open('input0.txt', 'r')
n = int(f.readline())

blocks= list()
my_laser_emitters=list()
opponent_laser_emitters=list()
my_laser_range= list()
opponent_laser_range= list()
safePositions=list()
scoresMatrix=copy.copy(safePositions)
finalsafematrix=list()
new_list = list()

def createGameBoard():
    for row in range(0, n):
        temp = []
        f1 = f.readline()
        for col in range(0, n):
            temp.append(int(f1[col]))
        gameboard.append(temp)

def createLists():
    global my_laser_emitters
    global opponent_laser_emitters
    global my_laser_range
    global opponent_laser_range

    for row in range(0,n):
        for col in range(0,n):
            tuple = (row, col)
            if gameboard[row][col] == 3:
                blocks.append(tuple)
            if gameboard[row][col] == 0:
                safePositions.append(tuple)

    for row in range(0,n):
        for col in range(0,n):
            tuple = (row, col)
            if gameboard[row][col] == 2:
                opponent_laser_emitters.append(tuple)
                opponent_laser_updates(row,col)
            if gameboard[row][col] == 1:
                my_laser_emitters.append(tuple)
                my_laser_updates(row,col)

def my_laser_updates(i, j):
    for x in range(0, 3):
        if j+x+1 < n and gameboard[i][j+x+1] == 0:
            tuple=(i,j+x+1)
            my_laser_range.append(tuple)
            if tuple in safePositions: safePositions.remove(tuple)
        else: break

    for x in range(0, 3):
        if j-x-1 >= 0 and gameboard[i][j-x-1] == 0:
            tuple=(i,j-x-1)
            my_laser_range.append(tuple)
            if tuple in safePositions: safePositions.remove(tuple)
        else: break

    for x in range(0, 3):
        if i-1-x >= 0 and gameboard[i-1-x][j] == 0:
            tuple=(i-1-x,j)
            my_laser_range.append(tuple)
            if tuple in safePositions: safePositions.remove(tuple)
        else: break

    for x in range(0, 3):
        if i+x+1 < n and gameboard[i+x+1][j] == 0:
            tuple=(i+x+1,j)
            my_laser_range.append(tuple)
            if tuple in safePositions: safePositions.remove(tuple)
        else: break

    for x in range(0, 3):
        if i+1+x < n and j-1-x >= 0 and gameboard[i+1+x][j-1-x] == 0:
            tuple=(i+1+x,j-1-x)
            my_laser_range.append(tuple)
            if tuple in safePositions: safePositions.remove(tuple)
        else: break

    for x in range(0, 3):
        if i-1-x >= 0 and j+1+x < n and gameboard[i-1-x][j+1+x] == 0:
            tuple=(i-1-x,j+1+x)
            my_laser_range.append(tuple)
            if tuple in safePositions: safePositions.remove(tuple)
        else: break

    for x in range(0, 3):
        if i+1+x < n and j+1+x < n and gameboard[i+1+x][j+1+x] == 0:
            tuple=(i+1+x,j+1+x)
            my_laser_range.append(tuple)
            if tuple in safePositions: safePositions.remove(tuple)
        else: break

    for x in range(0, 3):
        if i-1-x >= 0 and j-1-x >= 0 and gameboard[i-1-x][j-1-x] == 0:
            tuple=(i-1-x,j-1-x)
            my_laser_range.append(tuple)
            if tuple in safePositions: safePositions.remove(tuple)
        else: break


def opponent_laser_updates(i, j):
    for x in range(0, 3):
        if j+x+1 < n and gameboard[i][j+x+1] == 0:
            tuple=(i,j+x+1)
            opponent_laser_range.append(tuple)
            if tuple in safePositions: safePositions.remove(tuple)
        else: break

    for x in range(0, 3):
        if j-x-1 >= 0 and gameboard[i][j-x-1] == 0:
            tuple=(i,j-x-1)
            opponent_laser_range.append(tuple)
            if tuple in safePositions: safePositions.remove(tuple)
        else: break

    for x in range(0, 3):
        if i-1-x >= 0 and gameboard[i-1-x][j] == 0:
            tuple=(i-1-x,j)
            opponent_laser_range.append(tuple)
            if tuple in safePositions: safePositions.remove(tuple)
        else: break

    for x in range(0, 3):
        if i+x+1 < n and gameboard[i+x+1][j] == 0:
            tuple=(i+x+1,j)
            opponent_laser_range.append(tuple)
            if tuple in safePositions: safePositions.remove(tuple)
        else: break

    for x in range(0, 3):
        if i+1+x < n and j-1-x >= 0 and gameboard[i+1+x][j-1-x] == 0:
            tuple=(i+1+x,j-1-x)
            opponent_laser_range.append(tuple)
            if tuple in safePositions: safePositions.remove(tuple)
        else: break

    for x in range(0, 3):
        if i-1-x >= 0 and j+1+x < n and gameboard[i-1-x][j+1+x] == 0:
            tuple=(i-1-x,j+1+x)
            opponent_laser_range.append(tuple)
            if tuple in safePositions: safePositions.remove(tuple)
        else: break

    for x in range(0, 3):
        if i+1+x < n and j+1+x < n and gameboard[i+1+x][j+1+x] == 0:
            tuple=(i+1+x,j+1+x)
            opponent_laser_range.append(tuple)
            if tuple in safePositions: safePositions.remove(tuple)
        else: break

    for x in range(0, 3):
        if i-1-x >= 0 and j-1-x >= 0 and gameboard[i-1-x][j-1-x] == 0:
            tuple=(i-1-x,j-1-x)
            opponent_laser_range.append(tuple)
            if tuple in safePositions: safePositions.remove(tuple)
        else: break

def calculateScores():
    for p in range(len(safePositions)):
        (i,j)=safePositions[p]

        score=1
        for x in range(0, 3):
            if j+x+1 < n and gameboard[i][j+x+1] == 0:
                score=score+1
            else: break

        for x in range(0, 3):
            if j-x-1 >= 0 and gameboard[i][j-x-1] == 0:
                score=score+1
            else: break

        for x in range(0, 3):
            if i-1-x >= 0 and gameboard[i-1-x][j] == 0:
                score=score+1
            else: break

        for x in range(0, 3):
            if i+x+1 < n and gameboard[i+x+1][j] == 0:
                score=score+1
            else: break

        for x in range(0, 3):
            if i+1+x < n and j-1-x >= 0 and gameboard[i+1+x][j-1-x] == 0:
                score=score+1
            else: break

        for x in range(0, 3):
            if i-1-x >= 0 and j+1+ x < n and gameboard[i - 1 - x][j + 1 + x] == 0:
                score=score+1
            else:
                break

        for x in range(0, 3):
            if i + 1 + x < n and j + 1 + x < n and gameboard[i + 1 + x][j + 1 + x] == 0:
                score=score+1
            else:
                break

        for x in range(0, 3):
            if i - 1 - x >= 0 and j - 1 - x >= 0 and gameboard[i - 1 - x][j - 1 - x] == 0:
                score=score+1
            else:
                break

        scoresMatrix.append(score)

def calculatesafepositions():
    while scoresMatrix:
        pos = 0
        max = scoresMatrix[0]
        for x in range(len(scoresMatrix)):
            if scoresMatrix.__getitem__(x) > max:
                max = scoresMatrix.__getitem__(x)
                pos = x

        p = safePositions.pop(pos)
        finalsafematrix.append(p)
        new_list.append(max)
        scoresMatrix.remove(max)

def laserCheckmate(x, y, maxturn, depth):
    global my_laser_emitters
    global opponent_laser_emitters
    global my_laser_range
    global opponent_laser_range
    global safePositions

    if len(safePositions) == 0:
        myscore = len(my_laser_emitters) + len(my_laser_range)
        opponentscore = len(opponent_laser_emitters) + len(opponent_laser_range)
        if myscore > opponentscore:
            return 1
        elif myscore < opponentscore:
            return -1
        else:
            return 0

    if maxturn:
        res = -100000
        for x in range(len(safePositions)):
            copy_safepositions = copy.copy(safePositions)
            (i,j) = safePositions[x]
            safePositions.remove((i,j))

            copy_my_emitters = copy.copy(my_laser_emitters)
            copy_opponent_emitters = copy.copy(opponent_laser_emitters)
            copy_my_range = copy.copy(my_laser_range)
            copy_opponent_range = copy.copy(opponent_laser_range)

            my_laser_emitters.append((i,j))
            my_laser_updates(i,j)
            res2 = laserCheckmate(i, j, False, depth + 1)

            my_laser_emitters = copy.copy(copy_my_emitters)
            opponent_laser_emitters = copy.copy(copy_opponent_emitters)
            my_laser_range = copy.copy(copy_my_range)
            opponent_laser_range = copy.copy(copy_opponent_range)
            safePositions = copy.copy(copy_safepositions)

            res = max(res, res2)
            if res > 0:
                return 1
        return res

    else:
        res = 100000
        for x in range(len(safePositions)):
            copy_safepositions = copy.copy(safePositions)
            (i, j) = safePositions[x]
            safePositions.remove((i, j))

            copy_my_emitters = copy.copy(my_laser_emitters)
            copy_opponent_emitters = copy.copy(opponent_laser_emitters)
            copy_my_range = copy.copy(my_laser_range)
            copy_opponent_range = copy.copy(opponent_laser_range)

            opponent_laser_emitters.append((i, j))
            opponent_laser_updates(i, j)
            res2 = laserCheckmate(i, j, True, depth + 1)

            my_laser_emitters = copy.copy(copy_my_emitters)
            opponent_laser_emitters = copy.copy(copy_opponent_emitters)
            my_laser_range = copy.copy(copy_my_range)
            opponent_laser_range = copy.copy(copy_opponent_range)
            safePositions = copy.copy(copy_safepositions)

            res = min(res, res2)
            if res < 0:
                return -1
        return res

def minimax_algo():
    global my_laser_emitters
    global opponent_laser_emitters
    global my_laser_range
    global opponent_laser_range
    global safePositions

    result = -1000000
    for x in range(0, len(safePositions)):
        copy_safepositions = copy.copy(safePositions)
        (i,j) = safePositions[x]
        safePositions.remove((i,j))

        copy_my_emitters = copy.copy(my_laser_emitters)
        copy_opponent_emitters = copy.copy(opponent_laser_emitters)
        copy_my_range = copy.copy(my_laser_range)
        copy_opponent_range = copy.copy(opponent_laser_range)

        my_laser_emitters.append((i, j))
        my_laser_updates(i, j)

        result=max(result,laserCheckmate(i,j,False,1))

        my_laser_emitters = copy.copy(copy_my_emitters)
        opponent_laser_emitters = copy.copy(copy_opponent_emitters)
        my_laser_range = copy.copy(copy_my_range)
        opponent_laser_range = copy.copy(copy_opponent_range)
        safePositions = copy.copy(copy_safepositions)

        if result > 0:
            return i,j

def main():
    global safePositions
    createGameBoard()
    createLists()
    calculateScores()
    calculatesafepositions()
    safePositions = copy.copy(finalsafematrix)

    x,y=minimax_algo()
    with open('output.txt', 'w') as f:
        f.write('%d' % x)
        f.write('%s' %" ")
        f.write('%d' % y)

main()


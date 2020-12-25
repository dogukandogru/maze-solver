# -*- coding: utf-8 -*-

import maze
import random
import copy 
import sys
import time
import math
from colorama import Back
from colorama import init
from os import system


def generateStartAndEndPositions(playerCoordinates, targetCoordinates, width, height, strMatrix, i):
    sayiX = random.randrange(1, width*2+1, 1)
    sayiY = random.randrange(1, height*2+1, 1)
    
    
    while strMatrix[sayiX][sayiY] == 'O':
        sayiX = random.randrange(1, width*2+1, 1)
        sayiY = random.randrange(1, height*2+1, 1)
    
    if i==0:
        strMatrix[sayiX][sayiY] = 'X'
        playerCoordinates.append(sayiX)
        playerCoordinates.append(sayiY)
    
    
    while strMatrix[sayiX][sayiY] == 'O' or strMatrix[sayiX][sayiY] == 'X':
        sayiX = random.randrange(1, width*2+1, 1)
        sayiY = random.randrange(1, height*2+1, 1)
    
    strMatrix[sayiX][sayiY] = 'Y'
    targetCoordinates.append(sayiX)
    targetCoordinates.append(sayiY)
    
    


def DFS(strMatrix, playerCoordinates, stack, visited):
    
    stack.append("$")
    stack.append(playerCoordinates)
    visited.append(playerCoordinates)
    
    while True:
        
        if playerCoordinates == '$':
            """
            print(Back.RED + "Path not found")
            print(Back.RESET + "" , end= "")
             """
            temp = list()
            return temp
       

        if strMatrix[playerCoordinates[0]][playerCoordinates[1]]== 'Y':
            return stack
            break
        
        if strMatrix[playerCoordinates[0]-1][playerCoordinates[1]] == ' ' or strMatrix[playerCoordinates[0]-1][playerCoordinates[1]] == 'Y' or strMatrix[playerCoordinates[0]-1][playerCoordinates[1]] == 'X':
            # yukarı duvar değilse 
            newCoordinates = []
            newCoordinates.append(playerCoordinates[0] - 1) 
            newCoordinates.append(playerCoordinates[1]) 
            if newCoordinates not in visited:
                # yukarı hem duvar değil hemde unvisited
                visited.append(newCoordinates)
                stack.append(newCoordinates)
                playerCoordinates = newCoordinates
                continue
            
        if strMatrix[playerCoordinates[0]][playerCoordinates[1]-1] == ' ' or strMatrix[playerCoordinates[0]][playerCoordinates[1]-1] == 'Y' or strMatrix[playerCoordinates[0]][playerCoordinates[1]-1] == 'X':
            # sol duvar değilse 
            newCoordinates = []
            newCoordinates.append(playerCoordinates[0])
            newCoordinates.append(playerCoordinates[1]-1)
            if newCoordinates not in visited:
                # yukarı hem duvar değil hemde unvisited
                visited.append(newCoordinates)
                stack.append(newCoordinates)
                playerCoordinates = newCoordinates
                continue
        
        if strMatrix[playerCoordinates[0]+1][playerCoordinates[1]] == ' ' or strMatrix[playerCoordinates[0]+1][playerCoordinates[1]] == 'Y' or strMatrix[playerCoordinates[0]+1][playerCoordinates[1]] == 'X': 
            # aşağı duvar değilse 
            newCoordinates = []
            newCoordinates.append(playerCoordinates[0]+1)
            newCoordinates.append(playerCoordinates[1])
            if newCoordinates not in visited:
                # yukarı hem duvar değil hemde unvisited
                visited.append(newCoordinates)
                stack.append(newCoordinates)
                playerCoordinates = newCoordinates
                continue
            
        if strMatrix[playerCoordinates[0]][playerCoordinates[1]+1] == ' ' or strMatrix[playerCoordinates[0]][playerCoordinates[1]+1] == 'Y' or strMatrix[playerCoordinates[0]][playerCoordinates[1]+1] == 'X':
            # sağ duvar değilse 
            newCoordinates = []
            newCoordinates.append(playerCoordinates[0])
            newCoordinates.append(playerCoordinates[1]+1)
            if newCoordinates not in visited:
                # yukarı hem duvar değil hemde unvisited
                visited.append(newCoordinates)
                stack.append(newCoordinates)
                playerCoordinates = newCoordinates
                continue
       
    
        stack.pop()
        playerCoordinates = stack[-1]
        continue
    

def BFS(strMatrix, playerCoordinates, queue, visited):
   backtrackingList = []
   path = []
   queue.append(playerCoordinates)
   visited.append(playerCoordinates)
   rawPlayerCoordinates = copy.deepcopy(playerCoordinates)
   while True:
        if strMatrix[playerCoordinates[0]][playerCoordinates[1]] == 'Y':
            
            break
        
        if strMatrix[playerCoordinates[0]-1][playerCoordinates[1]] == ' ' or strMatrix[playerCoordinates[0]-1][playerCoordinates[1]] == 'Y' or strMatrix[playerCoordinates[0]-1][playerCoordinates[1]] == 'X':
            # yukarı duvar değilse 
            newCoordinates = []
            newCoordinates.append(playerCoordinates[0] - 1) 
            newCoordinates.append(playerCoordinates[1])
            if newCoordinates not in visited:
                # yukarı hem duvar değil hemde unvisited
                visited.append(newCoordinates)
                queue.append(newCoordinates)
                
                temp = [newCoordinates, playerCoordinates]
                backtrackingList.append(temp)
                
            
        if strMatrix[playerCoordinates[0]][playerCoordinates[1]-1] == ' ' or strMatrix[playerCoordinates[0]][playerCoordinates[1]-1] == 'Y' or strMatrix[playerCoordinates[0]][playerCoordinates[1]-1] == 'X':
            # sol duvar değilse 
            newCoordinates = []
            newCoordinates.append(playerCoordinates[0])
            newCoordinates.append(playerCoordinates[1]-1)
     
            if newCoordinates not in visited:
                # sol hem duvar değil hemde unvisited
                visited.append(newCoordinates)
                queue.append(newCoordinates)
                
                temp = [newCoordinates, playerCoordinates]
                backtrackingList.append(temp)
                
        
        if strMatrix[playerCoordinates[0]+1][playerCoordinates[1]] == ' ' or strMatrix[playerCoordinates[0]+1][playerCoordinates[1]] == 'Y' or strMatrix[playerCoordinates[0]+1][playerCoordinates[1]] == 'X': 
            # aşağı duvar değilse 
            newCoordinates = []
            newCoordinates.append(playerCoordinates[0]+1)
            newCoordinates.append(playerCoordinates[1])
          
            if newCoordinates not in visited:
                # aşağı hem duvar değil hemde unvisited
                visited.append(newCoordinates)
                queue.append(newCoordinates)
                
                temp = [newCoordinates, playerCoordinates]
                backtrackingList.append(temp)
                
            
        if strMatrix[playerCoordinates[0]][playerCoordinates[1]+1] == ' ' or strMatrix[playerCoordinates[0]][playerCoordinates[1]+1] == 'Y' or strMatrix[playerCoordinates[0]][playerCoordinates[1]+1] == 'X':
            # sağ duvar değilse 
            newCoordinates = []
            newCoordinates.append(playerCoordinates[0])
            newCoordinates.append(playerCoordinates[1]+1)
            
            if newCoordinates not in visited:
                # yukarı hem duvar değil hemde unvisited
                visited.append(newCoordinates)
                queue.append(newCoordinates)
                
                temp = [newCoordinates, playerCoordinates]
                backtrackingList.append(temp)
                
                
        if len(queue) == 0:
            """
            print(Back.RED + "Path not found")
            print(Back.RESET + "" , end= "")
            """
            return []
        playerCoordinates = queue.pop(0)
        
   
   
   backtrackingList.reverse()
   
   path = []
   
   current = ""
   for i in range (len(backtrackingList)):
       if strMatrix[backtrackingList[i][0][0]][backtrackingList[i][0][1]] == 'Y':
           current = backtrackingList[i]
           break
       
   tempTarget = [backtrackingList[i][0][0], backtrackingList[i][0][1]]
   path.append(tempTarget)
   backtrack(backtrackingList, current, path, rawPlayerCoordinates)
   
   return path
        
            
def backtrack(backtrackingList, current, path, playerCoordinates):
    if current[1]  == playerCoordinates:
        path.append(playerCoordinates)
        path.append(current[1])
        return path.reverse()
    
    index = -1
    
    for i in range (len(backtrackingList)):
        if current[1] == backtrackingList[i][0]:
            index = i
            path.append(backtrackingList[i][0])
            break
    
    backtrack(backtrackingList, backtrackingList[index], path, playerCoordinates)
       

def combinePathAndMatrix(path, strMatrix):
    
    if len(path) == 0:
        return
    
    path.pop()
    del(path[0])
    del(path[0])
    
    for i in range (len(path)):
        coordinate = path.pop()
        strMatrix[int(coordinate[0])][int(coordinate[1])] = "3"
        

def printMaze(strMatrix):
    
  
    for i in range (len(strMatrix)):
        if i==0:
            print("\t0", end=" ")
        elif i >= 10:
            print(i, end="")
        else:
            print(i, end=" ")
    print()
    for i in range (len(strMatrix)):
        print(i, end="\t")
        for j in range (len(strMatrix)):
            if strMatrix[i][j] == 'O':
                print(Back.RESET + "██", end="")
            elif strMatrix[i][j] == '3':
                print(Back.BLUE + "  ", end="")
                print(Back.RESET + "" , end= "")
            elif strMatrix[i][j] == 'X':
                print(Back.GREEN + "  ", end="")
                print(Back.RESET + "" , end= "")
            elif strMatrix[i][j] == 'Y':
                print(Back.MAGENTA + "  ", end="")
                print(Back.RESET + "" , end= "")
            
            else:
                print("  ", end="")
        print("")
    
    print("Green : Start Point\nPurple : Target Point")
    

def UCS(strMatrix, playerCoordinates, queue, visited):
    backtrackingList = []
    costMatrix = copy.deepcopy(strMatrix)
    rawPlayerCoordinates = copy.deepcopy(playerCoordinates)
    for i in range (len(costMatrix)):
        for j in range (len(costMatrix)):
            costMatrix[i][j] = random.randrange(1, 10, 1)
    
    
    queue.append(playerCoordinates)
    visited.append(playerCoordinates)
   
    while True:
        if strMatrix[playerCoordinates[0]][playerCoordinates[1]] == 'Y':
            break
        
        if strMatrix[playerCoordinates[0]-1][playerCoordinates[1]] == ' ' or strMatrix[playerCoordinates[0]-1][playerCoordinates[1]] == 'Y' or strMatrix[playerCoordinates[0]-1][playerCoordinates[1]] == 'X':
            # yukarı duvar değilse 
            newCoordinates = []
            newCoordinates.append(playerCoordinates[0] - 1) 
            newCoordinates.append(playerCoordinates[1])
       
            
       
            if newCoordinates not in visited:
                # yukarı hem duvar değil hemde unvisited
                visited.append(newCoordinates)
                queue.append(newCoordinates)
                
                temp = [newCoordinates, playerCoordinates]
                backtrackingList.append(temp)
                
            
        if strMatrix[playerCoordinates[0]][playerCoordinates[1]-1] == ' ' or strMatrix[playerCoordinates[0]][playerCoordinates[1]-1] == 'Y' or strMatrix[playerCoordinates[0]][playerCoordinates[1]-1] == 'X':
            # sol duvar değilse 
            newCoordinates = []
            newCoordinates.append(playerCoordinates[0])
            newCoordinates.append(playerCoordinates[1]-1)
     
            if newCoordinates not in visited:
                # yukarı hem duvar değil hemde unvisited
                visited.append(newCoordinates)
                queue.append(newCoordinates)
                
                temp = [newCoordinates, playerCoordinates]
                backtrackingList.append(temp)
                
        
        if strMatrix[playerCoordinates[0]+1][playerCoordinates[1]] == ' ' or strMatrix[playerCoordinates[0]+1][playerCoordinates[1]] == 'Y' or strMatrix[playerCoordinates[0]+1][playerCoordinates[1]] == 'X': 
            # aşağı duvar değilse 
            newCoordinates = []
            newCoordinates.append(playerCoordinates[0]+1)
            newCoordinates.append(playerCoordinates[1])
          
            if newCoordinates not in visited:
                # yukarı hem duvar değil hemde unvisited
                visited.append(newCoordinates)
                queue.append(newCoordinates)
                
                temp = [newCoordinates, playerCoordinates]
                backtrackingList.append(temp)
                
            
        if strMatrix[playerCoordinates[0]][playerCoordinates[1]+1] == ' ' or strMatrix[playerCoordinates[0]][playerCoordinates[1]+1] == 'Y' or strMatrix[playerCoordinates[0]][playerCoordinates[1]+1] == 'X':
            # sağ duvar değilse 
            newCoordinates = []
            newCoordinates.append(playerCoordinates[0])
            newCoordinates.append(playerCoordinates[1]+1)
            
            if newCoordinates not in visited:
                # yukarı hem duvar değil hemde unvisited
                visited.append(newCoordinates)
                queue.append(newCoordinates)
                
                temp = [newCoordinates, playerCoordinates]
                backtrackingList.append(temp)
                
        if len(queue) > 0:
            minimum = queue[0]
            index = -1
            for i in range (len(queue)):
                if costMatrix[queue[i][0]][queue[i][1]] < costMatrix[minimum[0]][minimum[1]]:
                    minimum = queue[i]
                    index = i
            
        if len(queue) == 0:
            """
            print(Back.RED + "Path not found")
            print(Back.RESET + "" , end= "")
            """
            return []    
        playerCoordinates = queue.pop(index)
        
   
   
    backtrackingList.reverse()
   
    path = []
   
    current = ""
    for i in range (len(backtrackingList)):
       if strMatrix[backtrackingList[i][0][0]][backtrackingList[i][0][1]] == 'Y':
           current = backtrackingList[i]
           break
       
    tempTarget = [backtrackingList[i][0][0], backtrackingList[i][0][1]]
    path.append(tempTarget)
    backtrack(backtrackingList, current, path, rawPlayerCoordinates)
   
    return path
    



def main():
    system('cls')
    init()
    sys.setrecursionlimit(10000)
    size = int(input("Enter maze size between 5-100: "))
    system('cls')
    if size < 5 or size > 100:
        print("Too big or too low maze :(")
        time.sleep(2.5)
        main()
    width = math.ceil((size-1)/2)
    height = math.ceil((size-1)/2)
    
    mazeObj = maze.Maze(width,height)
    mazeObj.randomize()
    strMatrixBFS = mazeObj._to_str_matrix()
    
    printMaze(strMatrixBFS)
    
    
    
    while True:
        print("Do you want to change maze ?\n1- Add wall\n2- Delete wall\n3- Nothing\n")
        optionWall = input()
        if optionWall == '1':    
                print("Where do you want to add wall ? Enter coordinates (e.g >15 27)")
                wallCoord = input()
                wallCoordX = wallCoord[:wallCoord.index(' ')]
                wallCoordY = wallCoord[wallCoord.index(' '):]
                strMatrixBFS[int(wallCoordX)][int(wallCoordY)] = 'O'
                system('cls')
                printMaze(strMatrixBFS)
                
    
        if optionWall == '2':    
                print("Where would you like to remove a wall ? Enter coordinates (e.g >15 27)")
                wallCoord = input()
                wallCoordX = wallCoord[:wallCoord.index(' ')]
                wallCoordY = wallCoord[wallCoord.index(' '):]
                strMatrixBFS[int(wallCoordX)][int(wallCoordY)] = ' '
                system('cls')
                printMaze(strMatrixBFS)
                
        
        if optionWall == '3':
            break


    system('cls')
    printMaze(strMatrixBFS)
    playerCoordinates = []
    targetCoordinates = []
    print("Select an option :\n")
    print("1- Select Start and End Points Automatically")
    print("2- Select Start and End Points Manually\n")
    
    option = input()
    if option == '1':
        print("How many target points do you want ?")
        targetPointCount = input()
        for i in range(int(targetPointCount)):
            generateStartAndEndPositions(playerCoordinates, targetCoordinates, width, height, strMatrixBFS, i)
        system('cls')
        printMaze(strMatrixBFS)
    elif option == '2':
        print("Enter x and y coordinates of starting position (e.g > 15 20 )\n")
        startingPoint = input()
        xCoordOfStarting = startingPoint[:startingPoint.index(' ')]
        yCoordOfStarting = startingPoint[startingPoint.index(' '):]
        strMatrixBFS[int(xCoordOfStarting)][int(yCoordOfStarting)] = 'X'
        playerCoordinates.append(int(xCoordOfStarting))
        playerCoordinates.append(int(yCoordOfStarting))
        system('cls')
        printMaze(strMatrixBFS)
        
        if (playerCoordinates[0] == 0 and playerCoordinates[1] == 0) or (playerCoordinates[0] == 0 and playerCoordinates[1] == len(strMatrixBFS)-1) or (playerCoordinates[0] == len(strMatrixBFS)-1 and playerCoordinates[1] == 0) or (playerCoordinates[0] == len(strMatrixBFS)-1 and playerCoordinates[1] == len(strMatrixBFS)-1):
            print("Player Coordinates can not be corners")
            return
        
        print("How many target points do you want ?")
        targetPointCount = input()
        
        for i in range(int(targetPointCount)):
            print("Enter x and y coordinates of target position (e.g > 10 34 )\n")
            targetPoint = input()
            xCoordOfTarget = targetPoint[:targetPoint.index(' ')]
            yCoordOfTarget = targetPoint[targetPoint.index(' '):]
            
            
            
            strMatrixBFS[int(xCoordOfTarget)][int(yCoordOfTarget)] = 'Y'
            targetCoordinates.append(int(xCoordOfTarget))
            targetCoordinates.append(int(yCoordOfTarget))
            
            system('cls')
            printMaze(strMatrixBFS)
            
            if (targetCoordinates[0] == 0 and targetCoordinates[1] == 0) or (targetCoordinates[0] == 0 and targetCoordinates[1] == len(strMatrixBFS)-1) or (targetCoordinates[0] == len(strMatrixBFS)-1 and targetCoordinates[1] == 0) or (targetCoordinates[0] == len(strMatrixBFS)-1 and targetCoordinates[1] == len(strMatrixBFS)-1):
                print("Target Coordinates can not be corners.")
                return
    
    
    
        
        
        
        
        
    strMatrixDFS = copy.deepcopy(strMatrixBFS)
    strMatrixUCS = copy.deepcopy(strMatrixBFS)
    

    
    print("\nWhich algorithm do you want to use to solve the maze with?")
    print("1- Depth First Search")
    print("2- Breadth First Search")
    print("3- Uniform Cost Search")
    print("4- All of them")
    
    selection = input()
    print()
   
    if selection == "1":
        start_time = time.time()
        queueDFS = []
        visitedDFS = []
        pathDFS = DFS(strMatrixDFS, playerCoordinates, queueDFS, visitedDFS)
        copyPath = copy.deepcopy(pathDFS)
        combinePathAndMatrix(pathDFS, strMatrixDFS)
        system('cls')
        printMaze(strMatrixDFS)
        if len(copyPath) <= 1:
            print(Back.RED + "\nPath not found")
            print(Back.RESET + "" , end= "")
        print("\nRunning time of DFS is %s " % (time.time() - start_time))
        
    elif selection == "2":
        start_time = time.time()
        stackBFS = []
        visitedBFS = []
        pathBFS = BFS(strMatrixBFS, playerCoordinates, stackBFS, visitedBFS)
        copyPath = copy.deepcopy(pathBFS)
        combinePathAndMatrix(pathBFS, strMatrixBFS)
        system('cls')
        printMaze(strMatrixBFS)
        if len(copyPath) == 0:
            print(Back.RED + "\nPath not found")
            print(Back.RESET + "" , end= "")
        print("\nRunning time of BFS is %s " % (time.time() - start_time))
    elif selection == "3":
        start_time = time.time()
        queueUCS = []
        visitedUCS = []
        pathUCS = UCS(strMatrixUCS, playerCoordinates, queueUCS, visitedUCS)
        copyPath = copy.deepcopy(pathUCS)
        combinePathAndMatrix(pathUCS, strMatrixUCS)
        system('cls')
        printMaze(strMatrixUCS)
        if len(copyPath) == 0:
            print(Back.RED + "\nPath not found")
            print(Back.RESET + "" , end= "")
        print("\nRunning time of UCS is %s " % (time.time() - start_time))
    elif selection == "4":
        start_timeDFS = time.time()
        queueDFS = []
        visitedDFS = []
        pathDFS = DFS(strMatrixDFS, playerCoordinates, queueDFS, visitedDFS)
        copyPathDFS = copy.deepcopy(pathDFS)
        combinePathAndMatrix(pathDFS, strMatrixDFS)
        end_timeDFS = time.time()
        
        
        start_timeBFS = time.time()
        stackBFS = []
        visitedBFS = []
        pathBFS = BFS(strMatrixBFS, playerCoordinates, stackBFS, visitedBFS)
        copyPathBFS = copy.deepcopy(pathBFS)
        combinePathAndMatrix(pathBFS, strMatrixBFS)
        end_timeBFS = time.time()
        
        
        
        start_timeUCS = time.time()
        queueUCS = []
        visitedUCS = []
        pathUCS = UCS(strMatrixUCS, playerCoordinates, queueUCS, visitedUCS)
        copyPathUCS = copy.deepcopy(pathUCS)
        combinePathAndMatrix(pathUCS, strMatrixUCS)
        end_timeUCS = time.time()
        
        system('cls')
        print("DFS Solution:\n")
        printMaze(strMatrixDFS)
        print("\nBFS Solution:\n")
        printMaze(strMatrixBFS)
        print("\nUCS Solution:\n")
        printMaze(strMatrixUCS)
        if len(copyPathDFS) <= 1 or len(copyPathBFS) == 0 or len(copyPathUCS) == 0:
            print(Back.RED + "\nPath not found")
            print(Back.RESET + "" , end= "")
        
        print("\nRunning time of DFS is %s " % (end_timeDFS - start_timeDFS))
        print("Running time of BFS is %s " % (end_timeBFS - start_timeBFS))
        print("Running time of UCS is %s " % (end_timeUCS - start_timeUCS))
        
    print("\nDo you want to try again ?")
    print("1-Yes \n2-No")
    selection2 = input()
    if selection2 == "1":
        main()
    elif selection2 == "2":
        return
    
if __name__ == '__main__':
    main()
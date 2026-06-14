import keyboard
import random

'''with open ("/Users/henrytavareswilliams/Documents/maze/firstmaze.txt") as f:
    mainmaze = f.read()
print(mainmaze)'''



def decodemaze(maze):
    z = []
    x = "Hi!"
    with open (maze) as f:
        while not x == "":
            x = f.readline()
            z.append(x.replace("\n",""))
    return z

maze = "/Users/henrytavareswilliams/Documents/maze/firstmaze.txt"

##for i in range(len(maze)):
    ##print(maze[i])

class mazesolver():
    def __init__ (self,spritepos,speed,maze,direction):
        self.spritepos = spritepos
        self.speed = speed
        self.mazeview = maze
        self.walls = [0,0,0,0]
        self.direction = direction
    def rotate(self,rot):
        
        self.direction = (self.direction+rot)%4

    def movebydir(self):
        if self.direction == 0:
            self.spritepos[1]+=1
        elif self.direction == 2:
            self.spritepos[1]-=1
        elif self.direction == 1:
            self.spritepos[0]+=1
        elif self.direction == 3:
            self.spritepos[0]-=1

    def getwalls(self):
        z = self.mazeview.returnmaze()
        for i in range(len(self.walls/2)):
            if z[self.spritepos[1]+((i+1)%(len(self.walls))/2)][self.spritepos[0]+i] == self.decoder[0]:
                self.walls[i]=0
            else:
                self.walls[i]=1
        for i in range(len(self.walls/2)):
            if z[self.spritepos[1]-i][self.spritepos[0]-((i+1)%(len(self.walls))/2)] == self.decoder[0]:
                self.walls[i+len(self.walls)/2]=0
            else:
                self.walls[i+len(self.walls)/2]=1


class lefthandrobot(mazesolver):
    def __init__(self,spritepos,speed,maze,direction):
        super().__init__(spritepos,speed,maze,direction)
    def tick(self):
        self.getwalls()
        for i in range(3):
            if self.walls[(self.direction-i)%4] == 0:
                self.rotate(-i)
                break
        self.movebydir()
        self.mazeview.includebot("*",self.spritepos)
        

        
class mazeviewer():
    def __init__(self,maze,decoder):
        z = []
        x = "Hi!"
        with open (maze) as f:
            while not x == "":
                x = f.readline()
                z.append(x.replace("\n",""))
        z.pop()
        self.maze = z
        self.renderable = z
        self.decoder = decoder
       
        
        
    def startpoint(self):
        for i in range(len(self.maze[0])):
            if (self.maze[0])[i] == self.decoder[0]:
                return (i,0)
    def endpoint(self):
        #print(self.maze[-1])
        for i in range(len(self.maze[-1])):
            if (self.maze[-1])[i] == self.decoder[0]:
                return (len(self.maze),i)
    def returnmaze(self):
        return self.maze
    def includebot(self,character,pos):
        self.renderable[pos[1]] = self.renderable[pos[1]][:pos[0]] + character + self.renderable[pos[1]][pos[0]+1:]
    def rendermaze(self):
        return self.renderable
            
    
mazeview = mazeviewer(maze,(" ","█"))
lefty = lefthandrobot(mazeview.startpoint,1,mazeview,1)
while True:
    keyboard.read_key()
    if keyboard.is_pressed("space"):
        lefty.tick()
        print(mazeview.rendermaze())
print(mazeview.endpoint())

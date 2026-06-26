from random import randrange as r
import os

maze = "/account/Documents/maze/hardmaze.txt"

#class mazeGe


class mazesolver:
    def __init__ (self,spritepos,speed,maze,direction,decoder):
        self.spritepos = spritepos
        self.speed = speed
        self.mazeview = maze
        self.walls = [0,0,0,0]
        self.direction = direction
        self.decoder = decoder
    def rotate(self,rot):
        
        self.direction = (abs((self.direction+rot)%4))

    def movebydir(self):
        #print("hello")
        if self.direction == 0:
            self.spritepos[1]-=1
        elif self.direction == 2:
            self.spritepos[1]+=1
        elif self.direction == 1:
            self.spritepos[0]+=1
        elif self.direction == 3:
            self.spritepos[0]-=1

    def getwalls(self):
        z = self.mazeview.returnmaze()
        if not self.spritepos[1] < 1 :
            if z[self.spritepos[1]-1][self.spritepos[0]] == self.decoder[0]:
                self.walls[0] = 0
            else:
                self.walls[0] = 1
        else:
            self.walls[0] = 1
        if z[self.spritepos[1]][self.spritepos[0]+1] == self.decoder[0]:
                self.walls[1] = 0
        else:
                self.walls[1] = 1
        if not self.spritepos[1] == len(z):
            if z[self.spritepos[1]+1][self.spritepos[0]] == self.decoder[0]:
                self.walls[2] = 0
            else:
                self.walls[2] = 1
        if z[self.spritepos[1]][self.spritepos[0]-1] == self.decoder[0]:
                self.walls[3] = 0

            
        else:
                self.walls[3] = 1
                #print(self.decoder)
                #print("huh")
                #print(z[self.spritepos[1]][self.spritepos[0]-1])
    


       
def setupbreadth(spritepos,speed,maze,direction,decoder):
    
    ID = len(breadthbots)
    breadthbots.append({"botnum":0,"breadthjunct":[],"bots":[]})
    z = maze.returnmaze()
    for i in range(len(z)):
        breadthbots[ID]["breadthjunct"].append("")
        for j in range(len((z[i]))):
            breadthbots[ID]["breadthjunct"][i] = breadthbots[ID]["breadthjunct"][i]+"0"
    breadthbots[ID]["bots"].append(breadthsolver(spritepos,speed,maze,direction,decoder,ID))

def tick(ID):
    z = len(breadthbots[ID]["bots"])
    #print(z)
    for i in range(z):
        if breadthbots[ID]["bots"][i] != "":
            breadthbots[ID]["bots"][i].tick()

        

class breadthsolver(mazesolver):
    def __init__(self,spritepos,speed,maze,direction,decoder,ID):
        super().__init__(spritepos,speed,maze,direction,decoder)
        #self.maze = self.mazeview.returnmaze()
        self.id = ID
        self.botid= breadthbots[self.id]["botnum"]
        breadthbots[self.id]["botnum"]+=1
        #self.movebydir()

    def format(self,junct):
        z = ""
        for i in range(len(junct)):
            z = str(z+junct[i]+"\n")
        return str(z)

    def getwallsspecial(self):
        z = self.mazeview.returnmaze()
        check = [[0,-1],[1,0],[0,1],[-1,0]]
        self.wallsspecial = [0,0,0,0]
        for i in range(len(check)):
            try:
                if z[self.spritepos[1]+check[i][1]][self.spritepos[0]+check[i][0]]== self.decoder[0]:#and not((self.spritepos[1] == 0 and i == 0) or (self.spritepos[1] == len(z) and i == 2)):
                    self.wallsspecial[i] = 0
                elif (self.spritepos[1] == 0 and i ==0) or (self.spritepos == len(z) and i ==2):
                    self.wallsspecial[i] = 0
                else:
                    self.wallsspecial[i] = 1
            except IndexError:
                #print("HA\nHA\nHA\nHA\nHA\nHA\nHA\nHA\nHA\nHA")
                #print(self.format(breadthbots[self.id]["breadthjunct"]))
                #if self.spritepos == self.mazeview.endpoint():
                #print("Finished\nFinding shortest path...")
                while self.spritepos != self.mazeview.startpoint():
                    #print("hi")
                    os.system('clear')
                    self.direction = int(breadthbots[self.id]["breadthjunct"][self.spritepos[1]][self.spritepos[0]])
                    
                    self.mazeview.includebot("+",self.spritepos,[0,0])
                    print(self.mazeview.rendermaze())
                    self.movebydir()
                    
                    
                    #print(self.mazeview.rendermaze())
                    #print(breadthbots[self.id]["breadthjunct"][self.spritepos[1]][self.spritepos[0]])
                    #print(self.spritepos)
                    if input("next") == "":
                        pass

            
            

       
    
    def insert(self,string,index,replacement):
        return string[:index] + replacement + string[index+1:]
    
    
    def tick(self):
        pastpos = self.spritepos.copy()
        self.movebydir()
        breadthbots[self.id]["breadthjunct"][self.spritepos[1]] = self.insert(breadthbots[self.id]["breadthjunct"][self.spritepos[1]],self.spritepos[0],str((self.direction+2)%4))
        self.mazeview.includebot("#",self.spritepos,pastpos)
        #print("hi")
        #print(self.spritepos)
        poss = []
        self.getwallsspecial()
        #print(self.wallsspecial)
        
        killed = False
        
        if sum(self.wallsspecial) < 2:
            #print("junct")
            for i in range(len(self.wallsspecial)):
                if self.wallsspecial[i] == 0 and (self.direction+2)%4 != i:
                    poss.append(i)
                #print(self.wallsspecial[i] == 0)
                #print((self.direction+2)%4 != i)
            #print(poss)
            for i in range(len(poss)):
                if i != 0:
                    breadthbots[self.id]["bots"].append(breadthsolver(self.spritepos.copy(),self.speed,self.mazeview,poss[i],self.decoder,self.id))

                    #self.insert(self.junct[self.spritepos[1]],self.spritepos[0],"0")
                else:
                    self.direction = poss[i]
        else:
            if sum(self.wallsspecial) == 3:
                breadthbots[self.id]["bots"][self.botid] = ""
                killed = True
            else:
                for i in range(len(self.wallsspecial)):
                    if self.wallsspecial[i]==0 and i != (self.direction+2)%4:
                        self.direction = i
                        break

        
                    
                    
            
            #breadthbots[self.id]["breadthjunct"][self.spritepos[1]] = self.insert(breadthbots[self.id]["breadthjunct"][self.spritepos[1]],self.spritepos[0],str((self.direction+2)%4))
            
            

class lefthandrobot(mazesolver):
    def __init__(self,spritepos,speed,maze,direction,decoder):
        super().__init__(spritepos,speed,maze,direction,decoder)
    def tick(self):
        self.getwalls()
        #print(self.walls)
        #print(self.spritepos)
        #print(self.direction)
        pastpos = self.spritepos.copy()
        for i in range(-1,3):
            if self.walls[(self.direction+i)%4] == 0:

                #print(f'i={i}')
                self.direction= (self.direction+i)%4
                break
        self.movebydir()
        ###print(self.spritepos)
        ##print(self.direction)
        self.mazeview.includebot("*",self.spritepos,pastpos)
        if self.spritepos == self.mazeview.endpoint():
            #print("finished!")
            pass

class tremaux(mazesolver):
    def __init__(self,spritepos,speed,maze,direction,decoder,):
        super().__init__(spritepos,speed,maze,direction,decoder)
        self.junct = []
        self.decodedir = [[0,-1],[1,0],[0,1],[-1,0]]
        
        for i in range(len(self.mazeview.returnmaze())):
            self.junct.append("")
            for j in range(len(self.mazeview.returnmaze()[i])):
                self.junct[i] = (str(self.junct[i]) + "0")
        #print(len(self.junct))
        #print(len(self.junct[0]))
        self.wallsdig = [0,0,0,0,0,0,0,0]

    def addjunct(self):
        for i in range(len(self.junct)):
            for j in range(len(self.junct[i])):
                if int(self.junct[i][j]) > 0:
                    self.mazeview.includebot(f"{self.junct[i][j]}",[j,i],[0,0])

    def getwallsspecial(self):
        z = self.mazeview.returnmaze()
        check = [[0,-1],[1,0],[0,1],[-1,0]]
        self.wallsspecial = [0,0,0,0]
        for i in range(len(check)):
            if z[self.spritepos[1]+check[i][1]][self.spritepos[0]+check[i][0]]== self.decoder[0]:#and not((self.spritepos[1] == 0 and i == 0) or (self.spritepos[1] == len(z) and i == 2)):
                self.wallsspecial[i] = 0
            elif (self.spritepos[1] == 0 and i ==0) or (self.spritepos == len(z) and i ==2):
                self.wallsspecial[i] = 0
            else:
                self.wallsspecial[i] = 1


    def insert(self,string,index,replacement):
        return string[:index] + replacement + string[index+1:]
    def format(self,format):
        q = ""
        for i in format:
            q = q + i + "\n"
        return q

    def getwallsdiagonally(self):
        z = self.mazeview.returnmaze()
        check = [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]

        for i in range(len(check)):
            if not( self.spritepos[1] == 0 and i>1 and i != 7) or not( self.spritepos[1] == len(z) and 2 < i < 6):
                if z[self.spritepos[1]+check[i][1]][self.spritepos[0]+check[i][0]] == self.decoder[0]:
                    self.wallsdig[i] = 0
                else:
                    self.wallsdig[i] = 1
            else:
                self.wallsdig[i] = 1
        #print(self.wallsdig)
        #for i in range(len(self.walls)):
            ##if self.wallsdig[i]-1 == 1 and i%2 == 1 and self.walls[i]+1 == 1:
                #self.wallsdig[i] == 1
    def pickrandom(self,list):
        #print(len(list))
        if len(list) == 1:
            return(list[0])
        else:
            return list[r(0,len(list))]
    
        
    def tick2(self):
        pastpos = self.spritepos.copy()
        #print(self.spritepos)         
        self.getwallsdiagonally()
        self.getwallsspecial()
        self.getwalls()
        #print(self.walls)
        x= 0
        z = []
        y = 0
        m = 0
        #print(self.wallsdig)
        done = False
        m = False
        poss = []
        for i in self.wallsdig:
            x += i
        
        if x != 7 and (x <6)and  4> sum(self.wallsspecial) > 1  : #and self.walls[(self.direction+2)%4] != 0:
            #print("halfway!")
            
            self.junct[self.spritepos[1]]= self.insert(self.junct[self.spritepos[1]],self.spritepos[0],str(int(self.junct[self.spritepos[1]][self.spritepos[0]])+1))
            #print("yay")
        for i in range(len(self.wallsdig)):
            if self.wallsdig[i] == 0:
                m = i
                break
        for i in range(len(self.walls)):
            if self.walls[i] == 0:
                y = i
                break
        if ((x == 6 and m%2 == 0 and self.wallsdig[(m+4)%8] == 0) or (self.walls[(y+2)%4] == 0 and sum(self.walls) == 2)):
            #print("a")
            #print((self.walls[y]+2)%4)
            #print(sum(self.walls) == 2)
            pass
        
        elif self.spritepos[1] == 0:
            self.direction = 2
            #print("b")
        
        elif x == 7:
            self.direction = (self.direction+2)%4

        else:
            for i in range(len(self.walls)):
                z.append(int(self.junct[self.decodedir[i][1] + self.spritepos[1]][self.decodedir[i][0]+ self.spritepos[0]]))
            for i in range(len(z)):
                if z[i] > 0:
                    y +=1
                    
            if sum(z) < 2 and y == 1:
                for i in range(len(z)):
                    if z[i] == 0 and self.walls[i]==0:
                        poss.append(i)
                    if len(poss) != 0:
                        self.direction = self.pickrandom(poss)
                        done = True
                        #print("c")
                        
            #print("check")
            y = 0
            if not done:
                for i in range(1,len(z)):
                    if  z[((self.direction+2)%4+i)%4] > 0:
                        y += 1
                if y ==3 and z[(self.direction+2)%4] < 2:
                    self.direction = (self.direction +2)%4
                    done = True
                    #print("d")
            if not done:
                y = 3
                for i in range(len(z)):
                    if z[i] < y and self.walls[i] == 0:
                        y = z[i]
                        m = i
                for i in range(len(z)):
                    if z[i] == z[m] and self.walls[i] == 0:
                        poss.append(i)

                #print(poss)
                self.direction = self.pickrandom(poss)
                #print("e")
        self.addjunct()
        self.movebydir()
        self.mazeview.includebot("@",self.spritepos,pastpos)
        #print(self.spritepos)
        #print(self.direction)
        #print(z)
        #print(x)
        #print(self.format(self.junct))
        
class mazeviewer:
    def __init__(self,maze,decoder):
        z = []
        x = "Hi!"
        with open (maze) as f:
            while not x == "":
                x = f.readline()
                z.append(x.replace("\n",""))
        z.pop()
        self.maze = z.copy()
        self.renderable = z.copy()
        self.decoder = decoder
        
    
        
        
    def startpoint(self):
        for i in range(len(self.maze[0])):
            if (self.maze[0])[i] == self.decoder[0]:
                return [i,0]
    def endpoint(self):
        #print(self.maze[-1])
        for i in range(len(self.maze[-1])):
            if (self.maze[-1])[i] == self.decoder[0]:
                return [len(self.maze),i]
    def returnmaze(self):
        return self.maze
    def includebot(self,character,pos,pastpos):
        self.renderable[pastpos[1]] = self.renderable[pastpos[1]][:pastpos[0]] + " " + self.renderable[pastpos[1]][pastpos[0]+1:]
        ###print("hi")
        ##print(pos)
        #print(pastpos)
        #print(self.maze[pastpos[1]][pastpos[0]])
        self.renderable[pos[1]] = self.renderable[pos[1]][:pos[0]] + character + self.renderable[pos[1]][pos[0]+1:]
        
    def rendermaze(self):
        x = ""
        for i in self.renderable:
            x = x+i+"\n"
        return x
    def returndecoder(self):
        return self.decoder
breadthbots = []   
mazeview = mazeviewer(maze,(" ","█"))
lefty = lefthandrobot(mazeview.startpoint(),1,mazeview,2,mazeview.returndecoder())
trem = tremaux(mazeview.startpoint(),1,mazeview,2,mazeview.returndecoder())
setupbreadth(mazeview.startpoint(),1,mazeview,2,mazeview.returndecoder())
while True:
    if input("tick?") == "":
        #trem.tick2()
        #lefty.tick()
        os.system('clear')
        tick(0)
        print(mazeview.rendermaze())
    

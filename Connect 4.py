class player():#class that creates a player object that hold's player's name and symbol
    def __init__(self,name,number):
        self.name=name
        self.num=number

class board():
    def __init__(self,col,rows):#creates a board according to number of columns and rows specified
        self.col=col
        self.row=rows
        self.board=[]
        for r in range(self.row):
            blankrow=[]
            for c in range(self.col):
                blankrow.append(' ')
            self.board.append(blankrow)
            
    def displayboard(self):#displays the board after formatting it
        for r in range(self.row):
            for c in range(self.col):
                    print("|"+self.board[r][c],end='')
            print('|')                
                
        
    def columnFull(self,col):#checks if a given column is full by iterating through it
        full=True
        for i in range(self.row):
            if self.board[i][col]==' ':
                full=False
        return full
    
    def boardfull(self):#checks if there are any spaces left on the board by iterating through every column
        full=True
        for i in range(self.col):
            check=self.columnFull(i)
            if check==False:
                full=False
        return full
    
    def getwidth(self):#returns the number of columns in board
        return self.col
    
    def addtoken(self,col,sym):#adds a given symbol to a given column on the board after checking the column is empty
        check=self.columnFull(col)
        if check:
            print("Sorry, this column is full!")
        else:
            notplaced=True
            i=self.row-1
            while notplaced:              
                if self.board[i][col]==' ':
                    self.board[i][col]=str(sym)
                    notplaced=False
                i=i-1
                
    def checkWinner(self):#checks if someone has won in any direction
        vwin,player=self.checkVertical()
        hwin,player=self.checkHorizontal()
        ldwin,player=self.checkLeftDiag()
        rdwin,player=self.checkRightDiag()
        if hwin or vwin or ldwin or rdwin:
            return True,player#returns the player that has one
        else:
            return False,0
        
    def checkVertical(self):#checks if someone has won in the vertical direction
        win=False
        player=0
        for y in range(self.col):
            for x in range(self.row-3):
                if self.board[x][y] == self.board[x+1][y] and self.board[x+1][y] == self.board[x+2][y]  and self.board[x+2][y]==self.board[x+3][y] and self.board[x+1][y]!=' ':
                    win=True
                    player=self.board[x][y]
        return win,player

    def checkRightDiag(self):#checks if someone has won diagonally right
        player=0
        win=False
        for x in range(self.col - 3):
            for y in range(self.row - 3):
                if self.board[x][y] == self.board[x+1][y+1] and self.board[x+1][y+1] == self.board[x+2][y+2]  and self.board[x+2][y+2]==self.board[x+3][y+3] and self.board[x+2][y+2]!=' ':
                    win = True
                    player=self.board[x][y]
        return win,player
    
    def checkLeftDiag(self):#checks if someone has won diagonally left
        player=0
        win=False
        for x in range(self.col - 3):
            for y in range(3, self.row):
                if self.board[x][y] == self.board[x+1][y-1] and self.board[x+1][y-1] == self.board[x+2][y-2]  and self.board[x+2][y-2]==self.board[x+3][y-3] and self.board[x+2][y-2]!=' ':
                    win = True
                    player=self.board[x][y]
        return win,player
    
    def checkHorizontal(self):#checks if someone has won horizontally
        player=0
        win=False
        for x in range(self.row):
            for y in range(self.col-3):
                if self.board[x][y] == self.board[x][y+1] and self.board[x][y+1] == self.board[x][y+2]  and self.board[x][y+2]==self.board[x][y+3] and self.board[x][y+1]!=' ':
                    win=True
                    player=self.board[x][y]
        return win,player
    
    
name=input("Player 1 Name:")
num=input("Player 1 Number:")
same=True
while same:
    name2=input("Player 2 Name:")
    num2=input("Player 2 Number:")#checks both users choose diff names and symbols
    if name2!=name and num2!=num:
        same=False
player1=player(name,num)
player2=player(name2,num2)#instantiates 2 player objects
valid=False
while not valid:
    try:
        col=int(input("How many columns?"))#lets user choose dimensions
        row=int(input("How many rows?"))
        valid=True
    except:
        print("Invalid entry.")
b=board(col,row)#instantiates board object according to dimensions
choice=None
won=False
b.displayboard()#displays board
valid=False
while choice!="Q" and not(won):
        try:
            choice=(int(input("Player 1 enter column for your move:")))-1#lets each player make their move one by one
            b.addtoken(choice,(player1.num))
            b.displayboard()    
            won,player=b.checkWinner()#checks winner after each move
            if won:
                print("Player 1 wins!!!")
            else:
                choice=(int(input("Player 2 enter column for your move:")))-1
                b.addtoken(choice,(player2.num))#adds token to player specified column
                b.displayboard()
                won,player=b.checkWinner()
                if won:
                    print("Player 2 wins!!!")
                    
        except:
            print("Invalid input!")
   

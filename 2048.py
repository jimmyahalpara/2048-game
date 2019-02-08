import simplegui2pygame as simplegui
#import simplegui
import random
message=''
class Game:
    def __init__(self):
        global message
        self.main=[[' ' for a in range(5)] for a in range(5)]
        self.insert_into_random()
        self.insert_into_random()
        self.full_condition=False
        message=''
    def insert_into_random(self):
        global message
        a=[]
        for i in range(5):
            for j in range(5):
                if self.main[i][j]==' ':
                    a.append([i,j])
        if a==[]:
            self.full_condition=True
            message='GAME OVER TRY AGAIN'
        else:
            k=random.choice(a)
            self.main[k[0]][k[1]]='2'
    def shrink(self,lis):
        l=[]
        for a in lis:
            if a != ' ':
                l.append(a)
        while len(l)<len(lis):
            l.append(' ')
        return l
    def check(self,lis):
        l=lis[:]
        con=False
        for i in range(len(l)):
            if l[i]==' ':
                continue
            else:
                for j in range(i+1,len(l)):
                    if (l[i]==l[j]):
                        con=True
                    elif l[j]==' ':
                        continue
                    else:
                        break             
        return con
    def add(self,lis):
        l=lis[:]
        l=self.shrink(l)
        for i in range(len(l)-1):
            if (l[i]==l[i+1]) and l[i] != ' ':
                l[i+1]=' '
                n=int(l[i])
                n*=2
                l[i]=str(n)
                l=self.shrink(l)
        return l
    def print_game(self,canvas):
        if not self.full_condition:
            canvas.draw_text(self.main[0][0],[60,140],50,'brown')
            canvas.draw_text(self.main[0][1],[160,140],50,'brown')
            canvas.draw_text(self.main[0][2],[260,140],50,'brown')
            canvas.draw_text(self.main[0][3],[360,140],50,'brown')
            canvas.draw_text(self.main[0][4],[460,140],50,'brown')
            canvas.draw_text(self.main[1][0],[60,240],50,'brown')
            canvas.draw_text(self.main[1][1],[160,240],50,'brown')
            canvas.draw_text(self.main[1][2],[260,240],50,'brown')
            canvas.draw_text(self.main[1][3],[360,240],50,'brown')
            canvas.draw_text(self.main[1][4],[460,240],50,'brown')
            canvas.draw_text(self.main[2][0],[60,340],50,'brown')
            canvas.draw_text(self.main[2][1],[160,340],50,'brown')
            canvas.draw_text(self.main[2][2],[260,340],50,'brown')
            canvas.draw_text(self.main[2][3],[360,340],50,'brown')
            canvas.draw_text(self.main[2][4],[460,340],50,'brown')
            canvas.draw_text(self.main[3][0],[60,440],50,'brown')
            canvas.draw_text(self.main[3][1],[160,440],50,'brown')
            canvas.draw_text(self.main[3][2],[260,440],50,'brown')
            canvas.draw_text(self.main[3][3],[360,440],50,'brown')
            canvas.draw_text(self.main[3][4],[460,440],50,'brown')
            canvas.draw_text(self.main[4][0],[60,540],50,'brown')
            canvas.draw_text(self.main[4][1],[160,540],50,'brown')
            canvas.draw_text(self.main[4][2],[260,540],50,'brown')
            canvas.draw_text(self.main[4][3],[360,540],50,'brown')
            canvas.draw_text(self.main[4][4],[460,540],50,'brown')

    def main_process(self,side):
        if side=='up':
            for i in range(5):
                l=[]
                for j in range(5):
                    l.append(self.main[j][i])
                l=self.add(l)
                for j in range(5):
                    self.main[j][i]=l[j]
        elif side=='down':
            for i in range(5):
                l=[]
                for j in range(4,-1,-1):
                    l.append(self.main[j][i])
                l=self.add(l)
                k=0
                for j in range(4,-1,-1):
                    self.main[j][i]=l[k]
                    k+=1
        elif side=='left':
            for i in range(5):
                l=[]
                for j in range(5):
                    l.append(self.main[i][j])
                l=self.add(l)
                for j in range(5):
                    self.main[i][j]=l[j]
        elif side=='right':
            for i in range(5):
                l=[]
                for j in range(4,-1,-1):
                    l.append(self.main[i][j])
                l=self.add(l)
                k=0
                for j in range(4,-1,-1):
                    self.main[i][j]=l[k]
                    k+=1
        self.insert_into_random()
        self.check_win()
    def check_win(self):
        global message
        for i in range(5):
            for j in range(5):
                if self.main[i][j]=='2048':
                    self.full_condition=True
                    message='YOU WON'
    def reset_game(self):
        self.__init__()
main_game=Game()
def draw(canvas):
    global message
    canvas.draw_line([50,50],[50,550],5,'black')
    canvas.draw_line([150,50],[150,550],5,'black')
    canvas.draw_line([250,50],[250,550],5,'black')
    canvas.draw_line([350,50],[350,550],5,'black')
    canvas.draw_line([450,50],[450,550],5,'black')
    canvas.draw_line([550,50],[550,550],5,'black')
    canvas.draw_line([50,50],[550,50],5,'black')
    canvas.draw_line([50,150],[550,150],5,'black')
    canvas.draw_line([50,250],[550,250],5,'black')
    canvas.draw_line([50,350],[550,350],5,'black')
    canvas.draw_line([50,450],[550,450],5,'black')
    canvas.draw_line([50,550],[550,550],5,'black')
    main_game.print_game(canvas)
    canvas.draw_text(message,[20,30],30,'black')
    
def kd(k):
    global main_game
    if not main_game.full_condition:
        if simplegui.KEY_MAP['w']==k:
            main_game.main_process('up')
        if simplegui.KEY_MAP['s']==k:
            main_game.main_process('down')
        if simplegui.KEY_MAP['a']==k:
            main_game.main_process('left')
        if simplegui.KEY_MAP['d']==k:
            main_game.main_process('right')
frame=simplegui.create_frame('2048',600,600)
frame.set_canvas_background('yellow')
frame.add_button('reset',main_game.reset_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kd)
frame.start()
                
                
    

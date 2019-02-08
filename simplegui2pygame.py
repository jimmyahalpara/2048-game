'''module by jimmy kumar ahalpara which can be used to play simplegui(codeskulptre) code in python using pygame
just replace import simplegui statement with import simplegui2pygame as simplegui. mostly all methods will do similer workd as codeskulptre
Updated on 7/1/2019
some colors added as needed'''


import pygame,math,time,sys,threading
import tkinter as tk
from pygame.locals import *


pygame.init()
pygame.mixer.init()
'''dictionary which converts alphabetic color and return rgb value as in a tuple'''
color={'aqua':(116,248,248),'black':(0,0,0),'Black':(0,0,0),'blue':(0,0,255),'Blue':(0,0,255),'fuchsia':(254,16,200),'grey':(130,130,130),'green':(0,255,0),'line':(106,255,6),'maroon':(198,0,0),
       'navy':(0,0,130),'olive':(46,119,2),'orange':(247,131,2),'purple':(174,0,249),'red':(255,0,0),'silver':(150,150,150),'teal':(22,173,90),'white':(255,255,255),
       'yellow':(249,255,0),'brown':(150,0,0),'Pink':(155,38,188),'violet':(163,73,164)}

'''same as simplegui.KEY_MAP in codeskulptre'''
KEY_MAP = {'a': 65, 'A': 65, 'b': 66, 'B': 66, 'c': 67, 'C': 67, 'd': 68, 'D': 68, 'e': 69, 'E': 69, 'f': 70, 'F': 70, 'g': 71, 'G': 71, 'h': 72, 'H': 72, 'i': 73,
        'I': 73, 'j': 74, 'J': 74, 'k': 75, 'K': 75, 'l': 76, 'L': 76, 'm': 77, 'M': 77, 'n': 78, 'N': 78, 'o': 79, 'O': 79, 'p': 80, 'P': 80, 'q': 81, 'Q': 81,
        'r': 82, 'R': 82, 's': 83, 'S': 83, 't': 84, 'T': 84, 'u': 85, 'U': 85, 'v': 86, 'V': 86, 'w': 87, 'W': 87, 'x': 88, 'X': 88, 'y': 89, 'Y': 89, 'z': 90,
        'Z': 90, '0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55, '8': 56, '9': 57, 'space': 32, 'left': 37, 'up': 38, 'right': 39, 'down': 40}

'''will map pygame event.key to its text value'''
KEY_MAP2={32: 'space', 276: 'left', 273: 'up', 275: 'right', 274: 'down', 48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9',
          97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q',
          114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z'}

class create_frame:
    '''creates mainframe object'''
    def __init__(self,caption,width,height,flags=0,col=32):
        self.width=width
        self.height=height
        self.caption=caption
        self.color=color
        self.flags=flags
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.draw_handler=None
        self.keyup_handler=None
        self.keydown_handler=None
        self.mouseclick_handler=None
        self.mousedrag_handler=None
        self.fill_color=(0,0,0)
        self.tk_frame=tk.Tk()
        self.tk_frame.protocol('WM_DELETE_WINDOW',self.destroy_program)
        self.tk_placing=10
        self.tk_input_list = []
    def destroy_program(self):
        '''used when you click tk frame close button'''
        pygame.quit()
        self.tk_frame.destroy()
        
    def set_canvas_background(self,col):
        '''will set background color'''
        self.fill_color=color[col]
        
    def set_draw_handler(self,meth):
        '''will set draw handler'''
        self.draw_handler=meth
        
    def set_keyup_handler(self,meth):
        '''will set keydown handler'''
        self.keyup_handler=meth
        
    def set_keydown_handler(self,meth):
        '''will set keydown handler'''
        self.keydown_handler=meth
        
    def set_mouseclick_handler(self,meth):
        '''will set mouse click handler'''
        self.mouseclick_handler=meth
        
    def set_mousedrag_handler(self,meth):
        '''will set mouse drag handler'''
        self.mousedrag_handler=meth
        
    def __return_draw_handler(self,con):
        if con:
            if self.draw_handler==None:
                return False
            else:
                return True
        else:
            return self.draw_handler
        
    def __return_keyup_handler(self,con):
        if con:
            if self.keyup_handler==None:
                return False
            else:
                return True
        else:
            return self.keyup_handler
        
    def __return_keydown_handler(self,con):
        if con:
            if self.keydown_handler==None:
                return False
            else:
                return True
        else:
            return self.keydown_handler
        
    def __return_mouseclick_handler(self,con):
        if con:
            if self.mouseclick_handler==None:
                return False
            else:
                return True
        else:
            return self.mouseclick_handler
        
    def __return_mousedrag_handler(self,con):
        if con:
            if self.mousedrag_handler==None:
                return False
            else:
                return True
        else:
            return self.mousedrag_handler
        
    def draw_line(self,point1,point2,width,col):
        pygame.draw.line(self.screen,color[col],to_int(point1),to_int(point2),width)
        
    def draw_polygon(self,lis,width,col,col2=None):
        if col2==None:
            pygame.draw.polygon(self.screen,color[col],to_int(lis,False),width)
        else:
            pygame.draw.polygon(self.screen,color[col],to_int(lis,False),0)
            
    def draw_text(self,text,position,size,col,back='black',font='arial'):
        pygame.font.init()
        if back=='black' and self.fill_color!=(0,0,0):
            back=self.fill_color
        else:
            back=color[back]
        fon=pygame.font.SysFont(font,int(size))
        suf=fon.render(text,True,color[col])
        self.screen.blit(suf,to_int((position[0],int(position[1]-size))))
        
    def draw_circle(self,position,radius,width,col,fillcol=None):
        if width>radius:
            width=radius
        if fillcol!=None:
            pygame.draw.circle(self.screen,color[col],to_int(position),int(radius),int(width))
            pygame.draw.circle(self.screen,color[fillcol],to_int(position),int(radius-width),0)
        else:
            pygame.draw.circle(self.screen,color[col],to_int(position),int(radius),int(width))
            
    def draw_point(self,position,col):
        pygame.draw.rect(self.screen,color[col],to_int([position[0],position[1],1,1]))
        
    def draw_polyline(self,lis,width,col):
        pygame.draw.lines(self.screen,color[col],False,to_int(lis,False),width)
        
    def draw_image(self,image,image_centre,image_draw_cordinates,draw_position,draw_size_cordinates,angle=0):
        sur = pygame.Surface((int(image_draw_cordinates[0]),int(image_draw_cordinates[1])),pygame.SRCALPHA,32)
        sur=sur.convert_alpha()
        img = image.return_pygame_image_object()
        sur.blit(img,(0,0),(int(image_centre[0]-(image_draw_cordinates[0]/2)),int(image_centre[1]-(image_draw_cordinates[1]/2)),int(image_draw_cordinates[0]),int(image_draw_cordinates[1])))
        sur2 = pygame.transform.scale(sur,to_int(draw_size_cordinates))
        sur3 = pygame.transform.rotate(sur2,int(math.degrees(-angle)))
        self.screen.blit(sur3,(int(draw_position[0]-(sur3.get_width()/2)),int(draw_position[1]-(sur3.get_height()/2))))
        
    def add_button(self,st,method):
        but = tk.Button(self.tk_frame,text=st,command=method)
        but.place(x=0,y=self.tk_placing)
        self.tk_placing+=30
        
    def add_input(self,text,method,size):
        l=tk.StringVar()
        tk.Label(self.tk_frame,text=text).place(x=0,y=self.tk_placing)
        tk.Entry(self.tk_frame,textvariable=l,width=size).place(x=int(len(text)*6.5),y=self.tk_placing)
        tk.Button(self.tk_frame,text = 'Enter',command=lambda:method(l.get())).place(x=int(size*6.5)+(len(text)*6.5),y=self.tk_placing)
        self.tk_input_list.append(l)
        self.tk_placing+=30
    def add_label(self,txt,width=0):
        ob = tk.Label(self.tk_frame,text=txt)
        ob.place(x=0,y=self.tk_placing)
        l=create_Label(ob,)
        self.tk_placing+=30
        return l
    def start(self):
        threading.Thread(target=self.starttk,args=()).start()
        self.tk_frame.mainloop()
    def starttk(self):
        while True:
            self.screen.fill(self.fill_color)
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    self.destroy_program()
                if event.type==KEYDOWN:
                    if self.__return_keydown_handler(True):
                        if event.unicode in KEY_MAP:
                            self.__return_keydown_handler(False)(KEY_MAP[event.unicode])
                        else:
                            if event.key in KEY_MAP2:
                                self.__return_keydown_handler(False)(KEY_MAP[KEY_MAP2[event.key]])
                            else:
                                self.__return_keydown_handler(False)(event.key)
                if event.type==KEYUP:
                    if self.__return_keyup_handler(True):
                        if event.key in KEY_MAP2:
                            self.__return_keyup_handler(False)(KEY_MAP[KEY_MAP2[event.key]])
                        else:
                            self.__return_keyup_handler(False)(event.key)
                if event.type==MOUSEBUTTONDOWN and event.button==1:
                    if self.__return_mouseclick_handler(True):
                        self.__return_mouseclick_handler(False)(event.pos)
                if event.type==MOUSEMOTION and event.buttons==(1,0,0):
                    if self.__return_mousedrag_handler(True):
                        self.__return_mousedrag_handler(False)(event.pos)
            if self.__return_draw_handler(True):
                self.__return_draw_handler(False)(self)
            pygame.display.update()
            
class create_Label:
    def __init__(self,obj):
        
        self.ob=obj
    def get_text(self):
        return self.ob['text']
    def set_text(self,txt):
        self.ob.configure(text=txt)


class image:
    def __init__(self,obj):
        self.image_obj=obj
        self.width=obj.get_width()
        self.height=obj.get_height()
    def return_pygame_image_object(self):
        return self.image_obj
    def get_height(self):
        return self.height
    def get_width(self):
        return self.width

    
class create_timer:
    thread_handler=[]
    def __init__(self,time,method):
        self.time=float(time)
        self.method=method
        self.playcon=False
        threading.Thread(target=self.main_loop,args=()).start()
    def start(self):
        self.playcon=True
    def stop(self):
        self.playcon=False
    def main_loop(self):
        while True:
            time.sleep(self.time/1000)
            if self.playcon:
                self.method()

                
class Sound:
    def __init__(self,path):
        self.path=path
        if path[-3:]==('wav' or 'ogg'):
            self.type = 1
            self.sound_object = pygame.mixer.Sound(self.path)
        else:
            self.type=2
    def play(self):
        if self.type==1:
            for a in range(6):
                if not pygame.mixer.Channel(a).get_busy():
                    pygame.mixer.Channel(a).play(self.sound_object)
        else:
            pygame.mixer.music.load(self.path)
            pygame.mixer.music.play()
    def rewind(self):
        if self.type==1:
            self.sound_object.stop()
        else:
            pygame.mixer.music.stop()
    def pause(self):
        pygame.mixer.pause()
    def set_volume(self,vol):
        if self.type==1:
            self.object.set_volume(vol)

            
def load_sound(path):
    obj = Sound(path)
    return obj


def load_image(path,con=1):
    if con==1:
        return image(pygame.image.load(path))
    elif con==2:
        return image(pygame.image.load(path).convert())
    elif con==3:
        return image(pygame.image.load(path).convert_alpha())

    
def to_int(l,con=True):
    if con:
        return [int(x) for x in l]
    else:
        for a in range(len(l)):
            l[a]=to_int(l[a])
        return l

    

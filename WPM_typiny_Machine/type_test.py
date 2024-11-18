import random
import curses
from curses import wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Typing GAME!!!")
    stdscr.addstr("\nPress Any key to Continue")
    stdscr.refresh()
    stdscr.getkey()
 
def load_input_text():
    with open('file.txt','r') as f :
        lines=f.readlines()
        return random.choice(lines).strip()

def display_text(stdscr,current_text,target_text,wpm=0):
    stdscr.addstr(target_text)
    stdscr.addstr(1,0,f"WPM:{wpm}")
    
    for i , char in enumerate(current_text):
        correct_character=target_text[i]
        color=curses.color_pair(1)
        if correct_character!=char : 
            color=curses.color_pair(2)
        stdscr.addstr(0,i,char,color)
       
def wpm_test(stdscr):
    target_text=load_input_text()
    target_text_update=target_text.split()
    current_text=[]
    wpm=0
    start_time=time.time()
    stdscr.nodelay(True)
    
    while True :
        time_spent=max(time.time()-start_time,1)
        wpm=round((len(current_text)/(time_spent/60))/5)
        stdscr.clear()
        display_text(stdscr,current_text,target_text,wpm)
        stdscr.refresh()
        
        if "".join(current_text)=="".join(target_text_update) :
            stdscr.nodelay(False)
            break
        
        try:
            key=stdscr.getkey()
        except:
            continue
        
        if ord(key) == 27:
            break
        
        if key in ("KEY_BACKSPACE","\b","\x7f"):
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text)<=len(target_text):
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
    
    start_screen(stdscr)
    
    wpm_test(stdscr)
    
    while True :
        wpm_test(stdscr)
        stdscr.addstr(2,0,"Welcome back You completed the text, Please Press any key to continue...")
        key=stdscr.getkey()
        
        if ord(key)==27:
            break
        
wrapper(main)
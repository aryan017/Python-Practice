from playsound import playsound
import time

def alarm(seconds):
    
    time_left=0
    
    while time_left<seconds:
        time.sleep(1)
        time_left+=1
        
        current_time=seconds-time_left
        current_time_inMinutes=current_time//60
        current_time_inSeconds=current_time%60
        
        print(f"{current_time_inMinutes:02d}:{current_time_inSeconds:02d}")
        
    playsound("newjeans_attention.mp3")

seconds=int(input("After how many seconds you want the alarm off?"))
alarm(seconds)
import pexpect
import time

child = None

def launch(file_path, subtitles_path):
    cmd = "omxplayer {}".format(file_path)
    
    if subtitles_path:
        cmd += "--subtitles {}".format(subtitles_path)
        
    global child
    
    child = pexpect.spawn(cmd)
    
    time.sleep(5)
    
    child.sendline("q")
import os

VIDEO_EXTENSIONS = ["mkv", "mp4", "flv"]
SUBTITLES_EXTENSIONS = ["srt"]

class Directory:
    def __init__(self, path):
        os.chdir(path)
        
        l_dir = os.listdir()
        
        self.l_elements = []
        self.path = os.getcwd()
        
        for name in l_dir:
            self.l_elements.append(DirectoryElement(name, path))
        
class DirectoryElement:
    def __init__(self, name, path):
        self.is_folder = True
        self.can_be_played = False # True if the element is a video
        self.element_path = path + "/" + name
        self.name = name
        
        try:
            os.chdir(name)
        
        except: # In case the element is a file
            self.is_folder = False
            
            if name.split(".")[-1] in VIDEO_EXTENSIONS:
                self.can_be_played = True
            
        else: # In case it is a folder
            os.chdir("..")
            
class Display:
    def __init__(self, path):
        split_path = path.split("/")
        self.folder = "/".join(split_path[:-1])
        self.filename = split_path[-1]
        self.path = path
        
    def get_available_subtitles(self):
        
        os.chdir(self.folder)
        
        l_subtitles = []
        
        for elt in os.listdir():
            if elt.split(".")[-1] in SUBTITLES_EXTENSIONS:
                l_subtitles.append(self.folder + "/" + elt)
                
        return l_subtitles
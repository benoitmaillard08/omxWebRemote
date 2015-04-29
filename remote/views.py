from django.shortcuts import render
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
import os
import remote.omx_api as api
import remote.explorer as exp

# Create your views here.
def player(request):
    
    file_path = request.GET["file"]
    subtitles_path = request.GET.get("subtitles", "")
    
    print(file_path)
    print(subtitles_path)
    
    api.launch(file_path, subtitles_path)
    
    return render(request, "remote/main.html", {"file" : file_path})
    
def ajax_remote(request):
    
    key = request.GET["key"]
    
    api.key_remote(key)
    
    print("KEY PRESS : {}".format(key))
    
    return HttpResponse("00")
    
def explorer(request, path):
    
    print(path)
    directory = exp.Directory(path)
    
    return render(request, "remote/explorer.html", {"directory" : directory})
    
def display(request, path):
    
    display = exp.Display(path)
    
    return render(request, "remote/display.html", {"display" : display})
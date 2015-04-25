from django.shortcuts import render
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
import os
import remote.omx_api as api

# Create your views here.
def player(request):
    
    file_path = request.GET["file"]
    subtitles_path = request.GET.get("subtitles", "")
    
    api.launch(file_path, subtitles_path)
    
    return render(request, "remote/main.html", {"file" : file_path})
    
def ajax_remote(request):
    
    key = request.GET["key"]
    
    api.key_remote(key)
    
    print("KEY PRESS : {}".format(key))
    
    return HttpResponse("00")
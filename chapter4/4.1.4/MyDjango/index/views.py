from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.http import StreamingHttpResponse
from django.http import FileResponse

def index(request):
    return render(request, 'index.html')

def download1(request):
    file_path = 'D:\cat.jpg'
    try:
        r = HttpResponse(open(file_path, 'rb'))
        r['content_type'] = 'application/octet-stream'
        r['Content-Disposition'] = 'attachment; filename=cat.jpg'
        return r
    except Exception:
        raise Http404('Download error')

def download2(request):
    file_path = 'D:\duck.jpg'
    try:
        r = StreamingHttpResponse(open(file_path, 'rb'))
        r['content_type'] = 'application/octet-stream'
        r['Content-Disposition'] = 'attachment; filename=duck.jpg'
        return r
    except Exception:
        raise Http404('Download error')

def download3(request):
    file_path = 'D:\dog.jpg'
    try:
        f = open(file_path, 'rb')
        r = FileResponse(f, as_attachment=True, filename='dog.jpg')
        return r
    except Exception:
        raise Http404('Download error')
from django.shortcuts import render
# 用于创建或进入聊天室
def newChat(request):
    return render(request, 'chat.html', locals())

# 创建聊天室
def room(request, room_name):
    return render(request, 'room.html', locals())
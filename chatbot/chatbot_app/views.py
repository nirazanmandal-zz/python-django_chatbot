from django.shortcuts import render, redirect
from .forms import ChatForm
from .chatbot import chat
from account_app.views import check_validation
from account_app.models import UserAccount


def chat_page(request):
    gif = True
    user = check_validation(request)
    if user:
        if request.method == 'POST':
            form = ChatForm(request.POST)
            if form.is_valid():
                form.save()
            inp = request.POST.get('message')
            reply = chat(inp)
            bot = 'Bot:'
            context = {
                'botreply': reply,
                'userreply': inp,
                'bot': bot,
                'gif': gif,
                'msg_send': user,
            }
            return render(request, 'chatbot_app/chat.html', context)
        else:
            return render(request, 'chatbot_app/chat.html', {'gif': gif, 'user': user})

    else:
        return redirect('account:login')


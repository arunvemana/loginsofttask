from django.shortcuts import render
# Create your views here.

def loginView(request):
    return  render(request,'loginapp/index.html')

def userView(request):
    content = request.user.socialaccount_set.filter(provider='facebook')[0].extra_data
    return render(request,'loginapp/userdetails.html',{'content':content})



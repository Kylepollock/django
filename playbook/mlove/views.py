from django.shortcuts import render




def index(request):
  

    context = {

        
    }
    return render(request, 'index.html', context)




def contact(request):
    context = {}


    return render(request, 'contact.html', context)


def give(request):
    context = {}

    return render(request, 'give.html', context)





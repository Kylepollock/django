from django.shortcuts import render, redirect




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


def send_email(request):

    if request.method == 'POST':

        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]


    return redirect("send-email.html")
# Do something with these three variables... return redirect("/") # Return a redirect!



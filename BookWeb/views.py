# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import logging

def test(request):
    #hi = Course.objects.all()
    html = "<html><body>UNDERGROUND RIVERS</body></html>"
    return HttpResponse(html)

def acctinit(request):
    return render(request, "html/acctinit.html", {})

def acctinit_submit(request):
    #template = loader.get_template("html/acctinit_submit.html")
    #return HttpResponse(template.render({request}))
    u1 = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["p1"])
    #u1 = User.objects.create_user('user', 'yilo', 'pw')
    u1.save()

    #return render(request, "html/acctinit_submit.html", {'firstname':request.POST["firstname"]})
    return acct_login(request)
def acct_login(request):
    user = authenticate(username='mama', password='mama')
    status = 'bitch'
    if user is not None:
      # the password verified for the user
      if user.is_active:
          print("User is valid, active and authenticated")
          status = 'valid!' 
      else:
          print("The password is valid, but the account has been disabled!")
          status = 'disabled!'
    else:
      # the authentication system was unable to verify the username and password
      status = 'POOOP'
  
    return render(request, "html/acctinit_submit.html", {'firstname':status})
     

from django.db.models.query_utils import Q
from django.forms.widgets import CheckboxInput
from django.shortcuts import redirect, render
from django.http import HttpResponse
from email_verification.forms import EmailForm
from email_verification.models import Email
from django.db.models import F, Q

# Create your views here.


def index(request):

    context = {}
    if request.method == "POST":
        data = request.POST["email"]
        # print(data)
        email = Email()
        try:
            email = Email.objects.get(email=data)
            print(type(email))
            print(email)
        except:
            e = Email(email=data)
            e.save()
            context["emailExistStatus"] = "Email not exist"
            return render(request, 'index.html', context)
        finally:
            count = email.count
            print(count)
            # count['count'] = count['count']+1
            # email.update(count=count['count'])
            Email.objects.filter(email=data).update(count=F('count') + 1)
            if count < 7:
                context["emailExistStatus"] = "Email not exist"
                return render(request, 'index.html', context)
            else:
                print(count)
                context["existed"] = "Email Already Exisit"
                # print(email)
                return render(request, 'index.html', context)

    if request.method == "GET":
        return render(request, 'index.html')


def SearchEmail(request):
    if(request.method == "POST"):
        data = request.POST["email"]
        print(data)
        email = ""
        try:
            email = Email.objects.get(email=data)
        except:
            pass
        finally:
            if email:
                print(email)
        return HttpResponse(data)
    else:
        return render(request, 'index.html')

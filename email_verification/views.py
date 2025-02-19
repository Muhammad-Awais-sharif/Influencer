from django.shortcuts import render
from email_verification.models import Email
from django.db.models import F
import csv
from django.http import HttpResponse


def index(request):

    context = {}
    if request.method == "POST":
        data = request.POST["email"]
        email = Email()
        try:
            email = Email.objects.get(email=data)
        except:
            e = Email(email=data)
            e.save()
            context["emailExistStatus"] = "Email not exist"
            return render(request, 'index.html', context)
        finally:
            count = email.count
            if count < 6:
                Email.objects.filter(email=email).update(count=F('count') + 1)
                context["emailExistStatus"] = "Email not exist"
                return render(request, 'index.html', context)
            else:
                context["existed"] = "Email Already Exisit"
                return render(request, 'index.html', context)

    if request.method == "GET":
        return render(request, 'index.html')


def get_all_emails(request):
    emails = Email.objects.all()
    context = {"emails": emails}
    return render(request, 'get_all_emails.html', context)


def export_into_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="emails.csv"'
    writer = csv.writer(response)
    writer.writerow(["id", 'Email', 'Count'])
    for email in Email.objects.all():
        writer.writerow([email.id, email.email, email.count])
    return response

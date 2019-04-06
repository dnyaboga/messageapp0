from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import BreastScreening, BreastResult, CervicalScreening, CervicalResult, NotifyBreast, NotifyCervical, \
    Person, Contact, EncounterType, Patient
from twilio.rest import Client


def index(request):
    return render(request, 'msgapp/index.html')


def person(request):
    if request.method == 'POST':
        person_id=request.POST.get('person_id')
        persons = Person.objects.all()
        context = {
            "persons": persons
        }

        p = Person(person_id=person_id)
        p.save()
        return render(request, 'msgapp/person.html', context)
    else:
        return render(request, 'msgapp/person.html')


def patient(request):
    if request.method == 'POST':

        person_id=request.POST.get('person_id')
        persons = Person.objects.all()
        context = {
            "persons": persons
        }

        p = Patient(person_id=person_id)
        p.save()
        return render(request, 'msgapp/patient.html', context)
    else:
        return render(request, 'msgapp/patient.html')


def encounter(request):
    if request.method == 'POST':
        persons = Person.objects.all()
        encounter_type=request.POST.get('encounter_type')
        context={
            'persons':persons
        }

        e = EncounterType(encounter_type=encounter_type)
        e.save()
        return render(request, 'msgapp/encounter.html',context)
    else:
        return render(request, 'msgapp/encounter.html')


def contact(request):
    if request.method == 'POST':
        person = Person.objects.all()
        phone_number=request.POST.get('phone_number')

        pn = Contact(person=person, phone_number=phone_number)
        pn.save()
        return render(request, 'msgapp/contact.html')
    else:
        return render(request, 'msgapp/contact.html')


def breastscreening(request):
    if request.method == 'POST':
        person=request.POST.get('person')
        encounter_type=request.POST.get('encounter_type')
        encounter_datetime = request.POST.get('encounter_datetime')
        location = request.POST.get('location')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        type_of_abnormality = request.POST.get('type_of_abnormality')
        age = request.POST.get('age')

        cs = BreastScreening(person=person, encounter_type=encounter_type, encounter_datetime=encounter_datetime, location=location, fname=fname, lname=lname,
                               gender=gender, type_of_abnormality=type_of_abnormality, age=age)
        cs.save()
        return render(request, 'msgapp/breast_screening.html')
    else:
        return render(request, 'msgapp/breast_screening.html')


def breastresult(request):
    if request.method == 'POST':
        person_id=request.POST.get('person_id')
        result_date = request.POST.get('result_date')
        results = request.POST.get('results')

        br = BreastResult(person_id=person_id, result_date=result_date, results=results)
        br.save()
        return render(request, 'msgapp/breast_result.html')
    else:
        return render(request, 'msgapp/breast_result.html')


def cervicalscreening(request):
    if request.method == 'POST':
        person = request.POST.get('person')
        encounter_type = request.POST.get('encounter_type')
        encounter_datetime = request.POST.get('encounter_datetime')
        location = request.POST.get('location')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        type_of_abnormality = request.POST.get('type_of_abnormality')
        age = request.POST.get('age')

        cs = CervicalScreening(person=person,encounter_type=encounter_type, encounter_datetime=encounter_datetime, location=location, fname=fname, lname=lname,
                               gender=gender, contact=contact, type_of_abnormality=type_of_abnormality, age=age)
        cs.save()
        return render(request, 'msgapp/cervical_screening.html')
    else:
        return render(request, 'msgapp/cervical_screening.html')


def cervicalresult(request):
    if request.method == 'POST':
        person_id = request.POST.get('person_id')
        result_date = request.POST.get('result_date')
        results = request.POST.get('results')

        cr = CervicalResult(person_id=person_id, result_date=result_date, results=results)
        cr.save()

        return render(request, 'msgapp/cervical_result.html')
    else:
        return render(request, 'msgapp/cervical_result.html')


def notifybreast(request):
    if request.method == 'POST':
        person_id = request.POST.get('person_id')
        notification_date = request.POST.get('notification_date')

        #account_sid = 'AC2bdd21ecf88ccccbea109556a4b755d3'
        #auth_token = '4e80265c137741a5ec3ede91863d5162'

        #client = Client(account_sid, auth_token)
        notifybreasts = BreastScreening.objects.all()
        #number_to_text = '+254714711312'
        #twilio_number = '+12015716985'
        #message_body = notifybreasts
        #message = client.messages.create(
              #to=number_to_text,
              #from_=twilio_number,
              #body=message_body
          #)

        context = {
            "notifybreasts": notifybreasts,
             #"client": client,
             #"number_to_text": number_to_text,
             #"twilio_number": twilio_number,
             #"message_body": message_body,
             #"message": message

        }

        n = NotifyBreast(person_id=person_id, notification_date=notification_date)
        n.save()
        return render(request, 'msgapp/notifybreast.html', context)
    else:
        return render(request, 'msgapp/notifybreast.html')


def notifycervical(request):
    if request.method == 'POST':
        person_id = request.POST.get('person_id')
        notification_date = request.POST.get('notification_date')

        #account_sid = 'AC2bdd21ecf88ccccbea109556a4b755d3'
        #auth_token = '4e80265c137741a5ec3ede91863d5162'

        #client = Client(account_sid, auth_token)
        notifycervical = CervicalScreening.objects.all()
        #number_to_text = '+254714711312'
        #twilio_number = '+12015716985'
        #message_body = notifycervical
        #message = client.messages.create(
              #to=number_to_text,
              #from_=twilio_number,
              #body=message_body
          #)

        context = {
            "notifycervical": notifycervical,
             #"client": client,
             #"number_to_text": number_to_text,
             #"twilio_number": twilio_number,
             #"message_body": message_body,
             #"message": message

        }

        n = NotifyCervical(person_id=person_id, notification_date=notification_date)
        n.save()
        return render(request, 'msgapp/notifycervical.html', context)
    else:
        return render(request, 'msgapp/notifycervical.html')








from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import BreastScreening, BreastResult, CervicalScreening, CervicalResult, Notify, Person
from twilio.rest import Client


def index(request):
    return render(request, 'msgapp/index.html')


def person(request):
    if request.method == 'POST':
        person_id=request.POST.get('person_id')
        encounter_type=request.POST.get('encounter_type')
        p = Person(person_id=person_id,encounter_type=encounter_type)
        p.save()
        return render(request, 'msgapp/person.html')
    else:
        return render(request, 'msgapp/person.html')


def contact(request):
    if request.method == 'POST':
        person_id=request.POST.get('person')
        phone_number=request.POST.get('phone_number')
        pn = Person(person_id=person_id, phone_number=phone_number)
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
        gender = request.POST.get('gender')
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


def notify(request):
    if request.method == 'POST':
        person_id = request.POST.get('person_id')
        notification_date = request.POST.get('notification_date')
        phone_number = request.POST.get('phone_number')

        n = Notify(person_id=person_id, notification_date=notification_date, phone_number=phone_number)
        n.save()
        return render(request, 'msgapp/notify.html')
    else:
        return render(request, 'msgapp/notify.html')


def messages(request):
    account_sid = 'AC2bdd21ecf88ccccbea109556a4b755d3'
    auth_token = '4e80265c137741a5ec3ede91863d5162'

    client = Client(account_sid, auth_token)
    messages = CervicalScreening.objects.all()
    number_to_text = '+254714711312'
    twilio_number = '+12015716985'
    message_body = messages
    message = client.messages.create(
        to=number_to_text,
        from_=twilio_number,
        body=message_body
    )

    context = {
        "messages": messages,
        "client": client,
        "number_to_text": number_to_text,
        "twilio_number": twilio_number,
        "message_body": message_body,
        "message": message

    }
    return render(request, 'msgapp/message.html', context)


def message1(request, message1_id):
    account_sid = 'AC2bdd21ecf88ccccbea109556a4b755d3'
    auth_token = '4e80265c137741a5ec3ede91863d5162'

    client = Client(account_sid, auth_token)
    message1 = BreastScreening.objects.get(pk=message1_id)
    number_to_text = '+254714711312'
    twilio_number = '+12015716985'
    message_body = message1
    message = client.messages.create(
        to=number_to_text,
        from_=twilio_number,
        body=message_body
    )


    context={
        "message1":message1,
        "client":client,
        "number_to_text":number_to_text,
        "twilio_number":twilio_number,
        "message_body":message_body,
        "message":message

    }
    return render(request,'msgapp/message1.html',context)





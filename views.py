from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import BreastScreening, BreastResult, CervicalScreening, CervicalResult, Notify, Person


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
        encounter_datetime = request.POST.get('encounter_datetime')
        location = request.POST.get('location')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        type_of_abnormality = request.POST.get('type_of_abnormality')
        age = request.POST.get('age')

        cs = BreastScreening(person=person, encounter_datetime=encounter_datetime, location=location, fname=fname, lname=lname,
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
        encounter_datetime = request.POST.get('encounter_datetime')
        location = request.POST.get('location')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        type_of_abnormality = request.POST.get('type_of_abnormality')
        age = request.POST.get('age')

        cs = CervicalScreening(encounter_datetime=encounter_datetime, location=location, fname=fname, lname=lname,
                               gender=gender, contact=contact, type_of_abnormality=type_of_abnormality, age=age)
        cs.save()
        return render(request, 'msgapp/cervical_screening.html')
    else:
        return render(request, 'msgapp/cervical_screening.html')


def cervicalresult(request):
    if request.method == 'POST':
        result_date = request.POST.get('result_date')
        results = request.POST.get('results')

        cr = CervicalResult(result_date=result_date, results=results)
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


def message(request):
    context={
        "messages": BreastScreening.objects.all()
    }
    return render(request, 'msgapp/message.html',context)








from django.db import models


class Person(models.Model):
    person_id=models.PositiveIntegerField(blank=True,null=True)


    class Meta:
        verbose_name_plural='Person'

    def __str__(self):
        return f"{self.person_id}"


class Patient(models.Model):
    person=models.ForeignKey(Person, null=True, related_name="patient_id", on_delete=models.SET_DEFAULT,default=1)

    class Meta:
        verbose_name_plural='Patient'

    def __str__(self):
        return f"{self.person}"


class EncounterType(models.Model):
    persons=models.ForeignKey(Person, null=True, related_name="person", on_delete=models.SET_DEFAULT,default=1)
    encounter_type = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural='EncounterType'

    def __str__(self):
        return f"{self.encounter_type}"


class Contact(models.Model):
    person = models.ForeignKey(Person, verbose_name="person_id", default=1, on_delete=models.SET_DEFAULT, null=True)
    phone_number=models.IntegerField(blank=True,null=True)

    class Meta:
        verbose_name_plural='Contact'

    def __str__(self):
        return f"{self.phone_number}"


class BreastScreening(models.Model):
    person=models.ForeignKey(Person, verbose_name="person_id", default=1, on_delete= models.SET_DEFAULT)
    encounter_type=models.ForeignKey(EncounterType, verbose_name="encounter_type", default=1, on_delete=models.SET_DEFAULT, null=True)
    encounter_datetime=models.DateField(blank=True,null=True)
    location=models.CharField(max_length=100)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    type_of_abnormality=models.CharField(max_length=200,blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)


    class Meta:
        verbose_name_plural='BreastScreening'

    def __str__(self):
        return f"Hi {self.lname}, \n" \
            f"the {self.encounter_type} test which you took on {self.encounter_datetime} at {self.location}\n" \
            f"Hospital is out. Please find time and visit our oncology clinic at {self.location }\n" \
            f"hospital from tomorrow to collect your results. For queries, please call +254788888888"


class BreastResult(models.Model):
    Person=models.ForeignKey(BreastScreening, verbose_name="Person_id", default=1, on_delete= models.SET_DEFAULT)
    result_date=models.DateField(blank=True,null=True)
    results=models.CharField(max_length=100,blank=True,null=True)


    class Meta:
        verbose_name_plural='BreastResult'

    def __str__(self):
        return str(self.results)


class CervicalScreening(models.Model):
    person = models.ForeignKey(Person, verbose_name="person_id", default=1, on_delete=models.SET_DEFAULT)
    encounter_type = models.CharField(max_length=100)
    encounter_datetime=models.DateField(blank=True,null=True)
    location=models.CharField(max_length=100)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    type_of_abnormality=models.CharField(max_length=200,blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)

    class Meta:
        verbose_name_plural='CervicalScreening'

    def __str__(self):
        return f"Hi {self.lname}, \n" \
            f"the {self.encounter_type} test which you took on {self.encounter_datetime} at {self.location}\n" \
            f"Hospital is out. Please find time and visit our oncology clinic at {self.location}\n" \
            f"hospital from tomorrow to collect your results. For queries, please call +254788888888"

class CervicalResult(models.Model):
    Person = models.ForeignKey(CervicalScreening, verbose_name="Person_id", default=1, on_delete=models.SET_DEFAULT)
    result_date = models.DateField(blank=True, null=True)
    results = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural='CervicalResult'

    def __str__(self):
        return str(self.result_date)


class NotifyBreast(models.Model):
    person = models.ForeignKey(Person, verbose_name="person_id", default=1, on_delete=models.SET_DEFAULT)
    notification_date = models.DateField(blank=True, null=True)
    contact = models.ForeignKey(Contact, verbose_name="phone_number", default=1, on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural='NotifyBreast'

    def __str__(self):
        return f"{self.person}  {self.contact}"


class NotifyCervical(models.Model):
    person = models.ForeignKey(Person, verbose_name="person_id", default=1, on_delete=models.SET_DEFAULT)
    notification_date = models.DateField(blank=True, null=True)
    contact = models.ForeignKey(Contact, verbose_name="phone_number", default=1, on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural='NotifyCervical'

    def __str__(self):
        return f"{self.person}  {self.contact}"







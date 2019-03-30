from django.db import models


class Person(models.Model):
    person_id=models.PositiveIntegerField(blank=True,null=True)
    encounter_type=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Person'

    def __str__(self):
        return f"{self.person_id}  {self.encounter_type}"


class Contact(models.Model):
    person = models.ForeignKey(Person, verbose_name="person_id", default=1, on_delete=models.SET_DEFAULT, null=True)
    phone_number=models.PositiveIntegerField(blank=True,null=True)

    class Meta:
        verbose_name_plural='Contact'

    def __str__(self):
        return f"{self.phone_number}"


class BreastScreening(models.Model):
    person=models.ForeignKey(Person, verbose_name="person_id", default=1, on_delete= models.SET_DEFAULT)
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
        return str(self.person)


class BreastResult(models.Model):
    Person=models.ForeignKey(BreastScreening, verbose_name="Person_id", default=1, on_delete= models.SET_DEFAULT)
    result_date=models.DateField(blank=True,null=True)
    results=models.CharField(max_length=100,blank=True,null=True)


    class Meta:
        verbose_name_plural='BreastResult'

    def __str__(self):
        return str(self.Person)


class CervicalScreening(models.Model):
    person = models.ForeignKey(Person, verbose_name="person_id", default=1, on_delete=models.SET_DEFAULT)
    encounter_datetime=models.DateField(blank=True,null=True)
    location=models.CharField(max_length=100)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    type_of_abnormality=models.CharField(max_length=200,blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)

    class Meta:
        verbose_name_plural='CervicalScreening'

    def __str__(self):
        return self.lname


class CervicalResult(models.Model):
    breast_screening = models.ForeignKey(CervicalScreening, verbose_name="Patient_id", default=1,
                                         on_delete=models.SET_DEFAULT)
    result_date=models.DateField(blank=True,null=True)
    results=models.CharField(max_length=100,blank=True,null=True)

    class Meta:
        verbose_name_plural='CervicalResult'

    def __str__(self):
        return str(self.result_date)


class Notify(models.Model):
    person = models.ForeignKey(Person, verbose_name="person_id", default=1, on_delete=models.SET_DEFAULT)
    notification_date = models.DateField(blank=True, null=True)
    contact = models.ForeignKey(Contact, verbose_name="phone number", default=1, on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural='Notify'

    def __str__(self):
        return f"{self.person}  {self.contact}"







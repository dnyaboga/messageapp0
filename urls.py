from django.urls import path
from . import views

app_name = 'msgapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('breastscreening', views.breastscreening, name='breastscreening'),
    path('breastresult', views.breastresult, name='breastresult'),
    path('cervicalscreening', views.cervicalscreening, name='cervicalscreening'),
    path('cervicalresult', views.cervicalresult, name='cervicalresult'),
    path('notifybreast', views.notifybreast, name='notifybreast'),
    path('notifycervical', views.notifycervical, name='notifycervical'),
    path('person', views.person, name='person'),
    path('patient', views.patient, name='patient'),
    path('encounter', views.encounter, name='encounter'),
    path('contact', views.contact, name='contact'),
    #path('messages', views.messages, name='messages'),
    #path('<int:message1>', views.message1, name='message1'),


]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('breastscreening', views.breastscreening, name='breastscreening'),
    path('breastresult', views.breastresult, name='breastresult'),
    path('cervicalscreening', views.cervicalscreening, name='cervicalscreening'),
    path('cervicalresult', views.cervicalresult, name='cervicalresult'),
    path('notify', views.notify, name='notify'),
    path('person', views.person, name='person'),
    path('contact', views.contact, name='contact'),
    path('messages', views.messages, name='messages'),
    path('<int:message1_id>', views.message1, name='message1'),


]
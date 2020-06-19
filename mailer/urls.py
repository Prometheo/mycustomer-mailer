from django.urls import path
from .views import MailListView

app_name = 'mailer'

urlpatterns = [
    path('', MailListView.as_view(), name="mail-list"),
]
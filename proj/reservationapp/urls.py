from django.urls import path

from proj.reservationapp.views import ParseTextResponseView


app_name = "reservationapp"
urlpatterns = [
    path('parse-text/', ParseTextResponseView.as_view()),
]

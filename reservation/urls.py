from django.urls import path
from . import views

urlpatterns = [
    # region Reservation
    path("reservation/", views.ReservationLC.as_view()),
    path("reservation/<int:pk>", views.ReservationRUD.as_view()),
    path("history/", views.ReservationHist.as_view()),
    # endregion
]
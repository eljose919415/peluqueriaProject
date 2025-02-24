from django.urls import path
from . import views

urlpatterns = [
    # region User
    path("register/", views.Register.as_view()),
    path("users/", views.CustomUserL.as_view()),
    path("users/<int:pk>", views.CustomUserRUD.as_view()),
    path("images/", views.ImagesManageLC.as_view()),
    path("images/<int:pk>", views.ImagesMangeRUD.as_view()),
    # endregion
]
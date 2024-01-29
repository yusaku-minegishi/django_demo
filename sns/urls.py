from django.urls import path

from . import views

app_name = "sns"

urlpatterns = [
    path("top/", views.top_view, name="top"),
    path("", views.list_view, name="list"),
    path("user/<str:user>/", views.user_list_view, name="userlist"),
    path("detail/<int:pk>/", views.detail_view, name="detail"),
    path("create/", views.create_view, name="create"),
    path("update/<int:pk>/", views.update_view, name="update"),
    path("delete/<int:pk>/", views.delete_view, name="delete"),
]

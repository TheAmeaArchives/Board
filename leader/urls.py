from django.urls import path
from . import views


urlpatterns = [
    path("Home", views.curation, name="curation"),
    path("remove/<int:pk>", views.remove_curation, name = "remove_curation"),
    path("edit/<int:pk>", views.edit_curation, name = 'edit_curation'),
    path("LeaderBoard/", views.leader_board, name='leader'),
    path("curation/<int:pk>", views.detail, name = "curation_detail"),
    path('accepted/', views.accepted, name = 'accepted'),
    path("accept/<int:pk>", views.accept, name = "accept")
]
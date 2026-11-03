from django.urls import path
from atelier import views

urlpatterns = [
    path("", views.home, name="home"),
    path("collections/", views.collections, name="collections"),
    path("our-story/", views.story, name="story"),
    path("lookbook/", views.lookbook, name="lookbook"),
    path("bespoke/", views.bespoke, name="bespoke"),
    path("contact/", views.contact, name="contact"),
]

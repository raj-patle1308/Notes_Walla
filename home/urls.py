from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("contact", views.contact, name='contact'),
    path('notes_walla/', views.notes_walla, name='notes_walla'),
    path('notes_page/', views.notes_page, name='notes_page'),
]
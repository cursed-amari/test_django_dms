from django.conf.urls.static import static
from django.urls import path, include


from .views import *

urlpatterns = [
    path('', AdventurePage.as_view(), name="adventure_page"),
    path('/create-adventure', AdventureCreate.as_view(), name="create-adventure"),
    path('/change-adventure/<slug:slug>', UserProfileView.as_view(), name="change-adventure"),
    path('/<slug:slug>', adventure_post, name="adventure_post"),
]


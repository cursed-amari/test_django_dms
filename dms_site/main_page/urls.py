from django.conf.urls.static import static
from django.urls import path, include

from dms_site import settings
from .views import *

# app_name = 'main_page'

urlpatterns = [
    path('', MainPage.as_view(), name="main_page"),
    path('registration', Registration.as_view(), name="register_user"),
    path('logout', logout_user, name="logout"),
    path('account/<username>', user_account, name="user_account"),
    path('change-password', UserPasswordChangeView.as_view(), name="password"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

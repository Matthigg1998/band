from django.urls import path, include
from . import views
from django.contrib import admin

app_name = 'band'

urlpatterns = [
    path('', views.login_view, name='login'),  # Redirect to your custom login page at root URL
    path('home/', views.home, name='home'),
    path('band/<int:band_id>/', views.band_info, name='band_info'),
    path('songs/', views.song_list, name='song_list'),
    path('registration/', views.registration_view, name='registration'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

from django.urls import path
from . import views  # Import your views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.custom_login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('register', views.register, name='register'),
    path('create', views.create, name='create'),
    path('profile', views.profile, name='profile'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
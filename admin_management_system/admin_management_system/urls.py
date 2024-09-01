from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views,Hod_Views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE,name='base'),

    #LOGIN PATH
    path('', views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='doLogout'),

    #HOD PATH
    path('Hod/Home',Hod_Views.HOME,name='hod_home'),
    path('Hod/Staff/Add',Hod_Views.ADD_STAFF,name='add_staff'),
    path('Hod/Staff/View',Hod_Views.VIEW_STAFF,name='view_staff'),
    path('Hod/Staff/Edit/<str:id>', Hod_Views.EDIT_STAFF,name='edit_staff'),
    path('Hod/Staff/Update',Hod_Views.UPDATE_STAFF,name='update_staff'),
    path('Hod/Staff/Delete/<str:admin>', Hod_Views.DELETE_STAFF,name='delete_staff'),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

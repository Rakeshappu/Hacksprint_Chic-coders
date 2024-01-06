"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from farmer.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('about/',about_view,name='about'),
    path('contact/',contact_view,name='contact'),
    path('faq/',faq_view,name='faq'),
    path('project/',project_view,name='project'),
    path('service/',service_view,name='service'),
    path('feature/',feature_view,name='feature'),
    path('team/',team_view,name='team'),
    path('testimonial/',testimonial_view,name='testimonial'),
    path('error/',error_view,name='error'),
    path('yp/',yp_view,name='yp'), 
    path('rm/',rm_view,name='rm'), 
    path('login/',login_view,name='login'),
    path('register/',register_view,name='register')
]

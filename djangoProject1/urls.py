"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from day_one import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/<int:number>', views.show_number),
    path('hello/<str:name>', views.hello),
    path('random/', views.random_num),
    path('random/<int:max_number>', views.pick_number),
    path('random/<int:min_number>/<int:max_number>', views.pick_number2),
    #re_path('^random/(?P<max_number>)(\d)+/$', views.pick_number),
]

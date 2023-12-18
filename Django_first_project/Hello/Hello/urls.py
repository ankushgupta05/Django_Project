"""
URL configuration for Hello project.

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
from django.urls import path, include

admin.site.site_header = "Ankush's Potfolio admin"
admin.site.site_title = "Ankush Gupta admin Potfolio "
admin.site.index_title = "Wellcome to ankush's Potfolio  "



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]


# Django version 4.2.5, using settings 'Hello.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.



# Username (leave blank to use 'ankushgupta'): ankushgupta0510
# Email address: ankushgupta0510@gmail.com
# password : A.G.2004

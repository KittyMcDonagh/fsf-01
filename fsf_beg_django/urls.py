"""fsf_beg_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from todo.views import get_todo_list, create_an_item, edit_an_item

# The url links to the function in views.py that needs to be run
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_todo_list),
    url(r'^add$', create_an_item),
    
# This url is a bit different. 
# ?P indicates that this is an expression
# <id> tells what the expression is
# \ what to expect comes after this
# d+ 'd' means a digit, '+' means more that one digit
    url(r'^edit/(?P<id>\d+)$', edit_an_item),
]

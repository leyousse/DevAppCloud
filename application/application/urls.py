"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from health_data import views


urlpatterns = [
    path('admin/', admin.site.urls),
	path('homepage/', views.home, name='home'),
	path('adminview/', views.adminview, name='adminview'),
	path('analyste/', views.analyste, name = 'analyste'),
	path('standard/', views.standard, name='standard'),
	path('standard/R1/', views.R1, name='R1'),
	path('standard/R2/', views.R2, name='R2'),
	path('standard/R3/', views.R3, name='R3'),
	path('standard/R4/', views.R4, name='R4'),
	path('analyste/R5/', views.R5, name='R5'),
	path('analyste/R5/R5_1/', views.R5_1, name='R5_1'),
	path('analyste/R5/R5_2/', views.R5_2, name='R5_2'),
	path('analyste/R5/R5_3/', views.R5_3, name='R5_3'),
	path('analyste/R6/', views.R6, name='R6'),
	path('analyste/R6/R6_1/', views.R6_1, name='R6_1'),
	path('analyste/R6/R6_2/', views.R6_2, name='R6_2'),
	path('analyste/R6/R6_3/', views.R6_3, name='R6_3'),
	path('analyste/R7/', views.R7, name='R7'),
	path('analyste/R7/R7_1/', views.R7_1, name='R7_1'),
	path('analyste/R7/R7_2/', views.R7_2, name='R7_2'),
	path('analyste/R7/R7_3/', views.R7_3, name='R7_3'),
	path('analyste/R8/', views.R8, name='R8'),
	path('analyste/R8/R8_1/', views.R8_1, name='R8_1'),
	path('analyste/R8/R8_2/', views.R8_2, name='R8_2'),
	path('analyste/R8/R8_3/', views.R8_3, name='R8_3'),
	path('adminview/statistiques/', views.statistiques, name='statistiques'),
	path('adminview/etat', views.etat, name='etat'),
	path('adminview/repartition', views.repartition, name='repartition'),
	path('adminview/indexes', views.indexes, name='indexes')
]

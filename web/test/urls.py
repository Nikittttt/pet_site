"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('get_prefecture', views.get_prefecture),
    path('add_prefecture', views.add_prefecture),
    path('update_prefecture/<int:pk>', views.update_prefecture),
    #path('delete_prefecture/<int:pk>', views.delete_prefecture),
    path('get_operating_organizations', views.get_operating_organizations),
    path('add_operating_organizations', views.add_operating_organizations),
    path('update_operating_organizations/<int:pk>', views.update_operating_organizations),
    #path('delete_operating_organizations/<int:pk>', views.delete_operating_organizations),
    path('get_shelter', views.get_shelter),
    path('add_shelter', views.add_shelter),
    path('update_shelter/<int:pk>', views.update_shelter),
    #path('delete_shelter/<int:pk>', views.delete_shelter),
    path('get_reason_retirement', views.get_reason_retirement),
    path('add_reason_retirement', views.add_reason_retirement),
    path('update_reason_retirement/<int:pk>', views.update_reason_retirement),
    #path('delete_reason_retirement/<int:pk>', views.delete_reason_retirement),
    path('get_reason_death', views.get_reason_death),
    path('add_reason_death', views.add_reason_death),
    path('update_reason_death/<int:pk>', views.update_reason_death),
    #path('delete_reason_death/<int:pk>', views.delete_reason_death),
    path('get_reason_euthanasia', views.get_reason_euthanasia),
    path('add_reason_euthanasia', views.add_reason_euthanasia),
    path('update_reason_euthanasia/<int:pk>', views.update_reason_euthanasia),
    #path('delete_reason_euthanasia/<int:pk>', views.delete_reason_euthanasia),
    path('get_district', views.get_district),
    path('add_district', views.add_district),
    path('update_district/<int:pk>', views.update_district),
    #path('delete_district/<int:pk>', views.delete_district),
    path('get_size', views.get_size),
    path('add_size', views.add_size),
    path('update_size/<int:pk>', views.update_size),
    #path('delete_size/<int:pk>', views.delete_size),
    path('get_tail', views.get_tail),
    path('add_tail', views.add_tail),
    path('update_tail/<int:pk>', views.update_tail),
    #path('delete_tail/<int:pk>', views.delete_tail),
    path('get_ears', views.get_ears),
    path('add_ears', views.add_ears),
    path('update_ears/<int:pk>', views.update_ears),
    #path('delete_ears/<int:pk>', views.delete_ears),
    path('get_wool', views.get_wool),
    path('add_wool', views.add_wool),
    path('update_wool/<int:pk>', views.update_wool),
    #path('delete_wool/<int:pk>', views.delete_wool),
    path('get_color', views.get_color),
    path('add_color', views.add_color),
    path('update_color/<int:pk>', views.update_color),
    #path('delete_color/<int:pk>', views.delete_color),
    path('get_breed', views.get_breed),
    path('add_breed', views.add_breed),
    path('update_breed/<int:pk>', views.update_breed),
    #path('delete_breed/<int:pk>', views.delete_breed),
    path('get_sex', views.get_sex),
    path('add_sex', views.add_sex),
    path('update_sex/<int:pk>', views.update_sex),
    #path('delete_sex/<int:pk>', views.delete_sex),
    path('get_kind', views.get_kind),
    path('add_kind', views.add_kind),
    path('update_kind/<int:pk>', views.update_kind),
    #path('delete_kind/<int:pk>', views.delete_kind),
    path('get_pet', views.get_pet),
    path('add_pet', views.add_pet),
    path('update_pet/<int:pk>', views.update_pet),
    #path('delete_pet/<int:pk>', views.delete_pet),
    path('get_processing_parasites', views.get_processing_parasites),
    path('add_processing_parasites', views.add_processing_parasites),
    path('update_processing_parasites/<int:pk>', views.update_processing_parasites),
    #path('delete_processing_parasites/<int:pk>', views.delete_processing_parasites),
    path('get_vaccination_information', views.get_vaccination_information),
    path('add_vaccination_information', views.add_vaccination_information),
    path('update_vaccination_information/<int:pk>', views.update_vaccination_information),
    #path('delete_vaccination_information/<int:pk>', views.delete_vaccination_information),
    path('get_health_information', views.get_health_information),
    path('add_health_information', views.add_health_information),
    path('update_health_information/<int:pk>', views.update_health_information),
    #path('delete_health_information/<int:pk>', views.delete_health_information),
]

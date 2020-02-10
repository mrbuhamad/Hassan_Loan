"""hassan_loan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Loans import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # -------- partisipent section------------#
    path('participants/', views.participants_list, name='participants-list'),
    path('participants/create', views.participants_create, name='participants-creat'),
    # -------- partisipent section------------#

    # -------- loan section-------------------#
    path('participants/<int:participants_id>/', views.loan_list, name='loan-detail'),
    path('loan/<int:participants_id>/create', views.loan_create, name='loan-create'),
    # -------- loan section-------------------#

    # -------- pyment section-----------------#
    path('pyments/<int:Loan_id>/', views.pyment_list, name='pyment-list'),
    path('pyments/<int:Loan_id>/create', views.pyment_create, name='pyments-create'),
    path('pyments/<pyment_id>/delete/', views.pyment_delete, name='pyments-delete'),
    # -------- pyment section-----------------#

    # -------- hold section-----------------#
    path('hold/<int:participants_id>/', views.int_hold_amount_list, name='hold-list'),
    path('hold/<int:participants_id>/create', views.hold_create, name='hold-create'),
    path('hold/<hold_id>/delete/', views.hold_delete, name='hold-delete'),
    # -------- hold section-----------------#
]

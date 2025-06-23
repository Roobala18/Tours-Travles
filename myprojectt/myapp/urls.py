from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # home page route
    path('all-cars/', views.all_cars, name='all_cars'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'), 
    path('domestic/', views.domestic, name='domestic'),
    path('destinations/', views.all_destinations, name='all_destinations'),
    path('destination/<slug:destination_slug>/', views.destination_detail, name='destination_detail'),
    path('generate-pdf/', views.generate_package_pdf, name='generate_package_pdf'),
    path('generate-pdf/<int:package_id>/', views.generate_package_pdf, name='generate_package_pdf'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add-package/', views.add_package, name='add_package'),

    path('international/', views.home, name='international'),
    path('destinations/international/', views.all_international, name='all_international'),
    path('destination/international/<slug:destination_slug>/', views.destination_detail_inter, name='destination_detail_inter'),


    path('kerala/', views.kerala, name='kerala'),
    path('destinations/kerala/', views.all_kerala, name='all_kerala'),
    path('destination/kerala/<slug:destination_slug>/', views.destination_kerala, name='destination_kerala'),

    path('karnataka/', views.karnataka, name='karnataka'),
    path('destinations/karnataka', views.all_karnataka, name='all_karnataka'),
    path('karnataka/destination/<slug:destination_slug>/', views.destination_karnataka, name='destination_karnataka'),

    path('andra', views.andra, name='andra'),
    path('destinations/andra', views.all_andra, name='all_andra'),
    path('destination/andra/<slug:destination_slug>/', views.destination_andhra, name='destination_andhra'),

     
]

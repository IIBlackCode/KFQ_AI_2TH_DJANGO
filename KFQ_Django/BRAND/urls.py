from django.urls import path
from BRAND import views
from .VIEW.theme import Theme

urlpatterns = [
    path('test/', views.index),
    path('index/', views.Brand.index, name='1_index.html'),
    path('about/', views.Brand.aboutus, name='2_about.html'),
    path('features/', views.Brand.features, name='3_features.html'),
    path('hosting/', views.Brand.hosting, name='4_hosting.html'),
    path('domain/', views.Brand.domain, name='5_domain.html'),
    path('pricing/', views.Brand.pricing, name='6_pricing.html'),
    path('contact/', views.Brand.contact, name='7_contact.html'),
#***********************************************************************#
    # Original Theme
    path('theme/index/', Theme.theme_index, name='1_index.html'),
    path('theme/about/', Theme.theme_aboutus, name='2_about.html'),
    path('theme/features/', Theme.theme_features, name='3_features.html'),
    path('theme/hosting/', Theme.theme_hosting, name='4_hosting.html'),
    path('theme/domain/', Theme.theme_domain, name='5_domain.html'),
    path('theme/pricing/', Theme.theme_pricing, name='6_pricing.html'),
    path('theme/contact/', Theme.theme_contact, name='7_contact.html'),
#***********************************************************************#
]
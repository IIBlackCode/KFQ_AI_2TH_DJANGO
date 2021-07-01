from django.urls import path
from CRM import views
from .VIEW.theme import Theme
from django.contrib.auth import views as auth_views

app_name='CRM'
urlpatterns = [
    path('test/', views.index),
    path('index/',                          views.Crm.index,        name='index'),
    path('profile/',                        views.Crm.profile,      name='profile'),
    path('settings/',                       views.Crm.settings,     name='settings'),
    path('status/',                         views.Crm.status,       name='status'),
    path('statistics/',                     views.Crm.statistics,   name='statics'),
    path('seatingChart/',                   views.Crm.seatingChart, name='seatingChart'),

    path('login/',                          auth_views.LoginView.as_view(template_name='crm/account/login.html'), name='login'),

    path('UI_Element/page=<page>/',           views.Crm.ui_Element, name='UI_Element'),
    path('icons/',                           views.Crm.icons,      name='icons'),
    path('forms/page=<page>/',                views.Crm.forms,      name='Forms'),
    path('tables/',                           views.Crm.tables,     name='tables'),
    path('charts/',                           views.Crm.chart,      name='charts'),
    path('maps/',                             views.Crm.maps,       name='maps'),

#***********************************************************************#
    # Original Theme
    path('theme/index/',                    Theme.theme_index,      name='01_index.html'),
    path('theme/profile/',                  Theme.theme_profile,    name='02_profile.html'),
    path('theme/settings/',                 Theme.theme_settings,   name='03_settings.html'),
    path('theme/invoice/',                  Theme.theme_invoice,    name='04_invoice.html'),
    path('theme/blank/',                    Theme.theme_blank,      name='05_blank.html'),
    path('theme/UI_Element/page=<page>/',    Theme.theme_UI_Element, name='06_UI_Element.html'),
    path('theme/icons/',                    Theme.theme_icons,      name='07_icons.html'),
    path('theme/forms/page=<page>/',         Theme.theme_Forms,      name='08_Forms.html'),
    path('theme/tables/',                    Theme.theme_tables,     name='09_tables.html'),
    path('theme/charts/',                    Theme.theme_chart,      name='10_charts.html'),
    path('theme/maps/',                      Theme.theme_maps,       name='11_maps.html'),
    # path('theme//', views.index, name=''),
#***********************************************************************#
]
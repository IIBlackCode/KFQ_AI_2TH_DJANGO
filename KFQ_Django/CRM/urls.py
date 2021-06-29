from django.urls import path
from CRM import views
from .VIEW.theme import Theme

urlpatterns = [
    path('test/', views.index),
    path('index/',                          views.Crm.index,        name='01_index.html'),
    path('profile/',                        views.Crm.profile,      name='02_profile.html'),
    path('settings/',                       views.Crm.settings,     name='02_settings.html'),
    path('status/',                         views.Crm.status,       name='03_status.html'),
    path('statistics/',                     views.Crm.statistics,   name='04_statistics.html'),

    path('UI_Element/page=<page>/',           views.Crm.ui_Element, name='06_UI_Element.html'),
    path('icons/',                           views.Crm.icons,      name='07_icons.html'),
    path('forms/page=<page>/',                views.Crm.forms,      name='08_Forms.html'),
    path('tables/',                           views.Crm.tables,     name='09_tables.html'),
    path('charts/',                           views.Crm.chart,      name='10_charts.html'),
    path('maps/',                             views.Crm.maps,       name='11_maps.html'),

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
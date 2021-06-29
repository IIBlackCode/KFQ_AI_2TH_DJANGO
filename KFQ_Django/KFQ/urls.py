from django.urls import path

from KFQ import views

urlpatterns = [
    path('', views.no, name='contents.html'),
    path('index/', views.index, name='index.html'),
    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show),
    path('template/', views.template),
    path('index/', views.index),
#=====================================================================================#
    path('2021-06-22/01/', views.Date2021_06_22.no_01, name='01_basic.html'),
    path('2021-06-22/02/', views.Date2021_06_22.no_02, name='02_operator.html'),
    path('2021-06-22/03/', views.Date2021_06_22.no_03, name='03_ajax.html'),
    path('2021-06-22/04/', views.Date2021_06_22.no_04, name='04.html'),
    path('2021-06-22/05/', views.Date2021_06_22.no_05, name='05.html'),
    path('2021-06-22/06/', views.Date2021_06_22.no_06, name='06.html'),
    path('2021-06-22/07/', views.Date2021_06_22.no_07, name='07.html'),
    # path('2021-06-22/01/', views.Date2021_06_22.no_01),

    path('2021-06-23/01/', views.Date2021_06_23.no_01, name='01.html'),
    path('2021-06-23/02/', views.Date2021_06_23.no_02, name='02.html'),
    path('2021-06-23/03/', views.Date2021_06_23.no_03, name='03.html'),
    path('2021-06-23/04/', views.Date2021_06_23.no_04, name='04.html'),
    path('2021-06-23/05/', views.Date2021_06_23.no_05, name='05.html'),
    path('2021-06-23/06/', views.Date2021_06_23.no_06, name='06.html'),
    path('2021-06-23/07/', views.Date2021_06_23.no_07, name='07.html'),
    path('2021-06-23/08/', views.Date2021_06_23.no_08, name='08.html'),
    path('2021-06-23/09/', views.Date2021_06_23.no_09, name='09.html'),
    path('2021-06-23/10/', views.Date2021_06_23.no_10, name='10.html'),
    path('2021-06-23/11/', views.Date2021_06_23.no_11, name='11.html'),
    path('2021-06-23/12/', views.Date2021_06_23.no_12, name='12.html'),
    path('2021-06-23/13/', views.Date2021_06_23.no_13, name='13.html'),
    path('2021-06-23/14/', views.Date2021_06_23.no_13, name='14.html'),
    path('2021-06-23/15/', views.Date2021_06_23.no_13, name='15.html'),
    path('2021-06-23/16/', views.Date2021_06_23.no_13, name='16.html'),
    path('2021-06-23/17/', views.Date2021_06_23.no_13, name='17.html'),
    path('2021-06-23/18/', views.Date2021_06_23.no_13, name='18.html'),


    path('2021-06-24/01/', views.Date2021_06_24.no_01, name='01.html'),
    path('2021-06-24/02/', views.Date2021_06_24.no_02, name='02.html'),
    path('2021-06-24/03/', views.Date2021_06_24.no_03, name='03.html'),
    path('2021-06-24/04/', views.Date2021_06_24.no_04, name='04.html'),
    path('2021-06-24/05/', views.Date2021_06_24.no_05, name='05.html'),
   

    path('JavaScript/Dom/01/', views.Dom.dom_01, name='dom_01.html'),
    path('JavaScript/Dom/02/', views.Dom.dom_02, name='dom_02.html'),
    path('JavaScript/Dom/03/', views.Dom.dom_03, name='dom_03.html'),
    path('JavaScript/Dom/04/', views.Dom.dom_04, name='dom_04.html'),
    path('JavaScript/Dom/05/', views.Dom.dom_05, name='dom_05.html'),
    path('JavaScript/Dom/06/', views.Dom.dom_06, name='dom_06.html'),
    path('JavaScript/Dom/07/', views.Dom.dom_07, name='dom_07.html'),
    path('JavaScript/Dom/08/', views.Dom.dom_08, name='dom_08.html'),
    path('JavaScript/Dom/09/', views.Dom.dom_09, name='dom_09.html'),
    path('JavaScript/Dom/10/', views.Dom.dom_10, name='dom_10.html'),
    path('JavaScript/Dom/11/', views.Dom.dom_11, name='dom_11.html'),

    # path('JavaScript/Dom/01/', views.Dom, name='dom_01.html'),
]
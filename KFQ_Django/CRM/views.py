from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("CRM PAGE.")
#***********************************************************************#
class Crm :
    def index(request):
        print("PAGE : index")
        page ='Dashboard'
        context = {
            'page' : page
        }
        return render(request, './crm/01_index.html', context)
    def profile(request):
        print("PAGE : profile")
        page ='Profile'
        context = {
            'page' : page
        }
        return render(request, './crm/02_profile.html', context)
    def settings(request):
        print("PAGE : settings")
        page ='Settings'
        context = {
            'page' : page
        }
        return render(request, './crm/02_settings.html', context)
    def status(request):
        print("PAGE : status")
        page ='status'
        context = {
            'page' : page
        }
        return render(request, './crm/03_status.html', context)
    def statistics(request):
        print("PAGE : statistics")
        page ='statistics'
        context = {
            'page' : page
        }
        return render(request, './crm/04_statistics.html', context)


    def ui_Element(request, page):
        print("PAGE : ",page)

        context = {
            'page' : page
        }
        if page == "01-alerts.html":
            return render(request, './crm/Element/UI_Element/ui-alerts.html', context)
        elif page == "02-buttons.html":
            return render(request, './crm/Element/UI_Element/ui-buttons.html', context)
        elif page == "03-cards.html":
            return render(request, './crm/Element/UI_Element/ui-cards.html', context)
        elif page == "04-general.html":
            return render(request, './crm/Element/UI_Element/ui-general.html', context)
        elif page == "05-grid.html":
            return render(request, './crm/Element/UI_Element/ui-grid.html', context)
        elif page == "06-modals.html":
            return render(request, './crm/Element/UI_Element/ui-modals.html', context)
        elif page == "07-typography.html":
            return render(request, './crm/Element/UI_Element/ui-typography.html', context)

        # return render(request, './crm/Element/06_UI_Element.html', context)

    def icons(request):
        print("PAGE : theme_icons")
        page ='Icons'
        context = {
            'page' : page
        }
        return render(request, './crm/Element/07_icons.html', context)

    def forms(request, page):
        print("PAGE : theme_Forms",page)

        context = {
            'page' : page
        }
        if page == "01-layouts.html":
            return render(request, './crm/Element/Forms/'+page, context)
        elif page == "02-basic-inputs.html":
            return render(request, './crm/Element/Forms/'+page, context)

    def tables(request):
        print("PAGE : theme_tables")
        page ='Tables'
        context = {
            'page' : page
        }
        return render(request, './crm/Element/09_tables.html', context)

    def chart(request):
        print("PAGE : theme_Charts")
        page ='Charts'
        context = {
            'page' : page
        }
        return render(request, './crm/Element/10_charts.html', context)

    def maps(request):
        print("PAGE : theme_maps")
        page ='Maps'
        context = {
            'page' : page
        }
        return render(request, './crm/Element/11_maps.html', context)
#***********************************************************************#


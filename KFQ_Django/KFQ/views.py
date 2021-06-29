from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Curriculum

# Create your views here.
def index(request):
    return render(request, './2021-06-25/index.html')

# Create your views here.
def main(request):
    return JsonResponse({'name': 'park','age': 37})

def insert(request):
    # 1-linus입력
    Curriculum.objects.create(name='linux')
    # 2- python입력
    c = Curriculum(name='python')
    c.save()
    # 3-html/css/js입력
    Curriculum(name='python').save()
    #4-django입력
    Curriculum(name='django').save()
    return HttpResponse('데이터 입력 완료')

def show(request):
    # curriculum = Curriculum.objects.all()
    # result = ''
    # for c in curriculum:
    #     result += c.name + '<br>'
    # return HttpResponse(result)
    
    # firstapp/templates/firstapp/show.html을 보여주자
    # return render(request, 'firstapp/show.html',{})

    curriculum = Curriculum.objects.all()
    return render(
        request, 'firstapp/show.html',
        {'data': curriculum}
    )

def template(request):
    curri = Curriculum.objects.all()
    data = {
        'curri': curri,
        'str': 'text', 'num': 10,
        'list': [1, 2, 3],
        'dict': {'a': 'aaa', 'b': 'bbb'}
    }
    return render(
        request, 'firstapp/template.html', data)


#===============================================================#
def no(request):
        page ='2021-06-22'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './contents.html', context)

class Date2021_06_22 :
    def no_01(request):
        page ='2021-06-22'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-22/01_basic.html', context)

    def no_02(request):
        page ='2021-06-22'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-22/02_operator.html', context)

    def no_03(request):
        page ='2021-06-22'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-22/03_ajax.html', context)


    def no_04(request):
        page ='2021-06-22'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-22/04.html', context) 

    def no_05(request):
        page ='2021-06-22'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-22/05.html', context) 
    
    def no_06(request):
        page ='2021-06-22'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-22/06.html', context) 
    
    def no_07(request):
        page ='2021-06-22'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-22/07.html', context) 

    def no_08(request):
        page ='2021-06-22'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-22/08.html', context) 

class Date2021_06_23 :
    def no_01(request):
        page ='2021-06-23'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-23/01.html', context) 

    def no_02(request):
        page ='2021-06-23'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-23/02.html', context) 

    def no_03(request):
        page ='2021-06-23'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-23/03.html', context) 

    def no_04(request):
        page ='2021-06-23'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-23/04.html', context) 

    def no_05(request):
        page ='2021-06-23'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-23/05.html', context) 

    def no_06(request):
        page ='2021-06-23'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-23/06.html', context) 

    def no_07(request):
        page ='2021-06-23'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-23/07.html', context) 

    def no_08(request):
        page ='2021-06-23'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-23/08.html', context) 

    def no_09(request):
        page ='2021-06-23'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-23/09.html', context)

    def no_10(request):
        page ='2021-06-23'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-23/10.html', context) 

    def no_11(request):
        page ='2021-06-23'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-23/11.html', context) 

    def no_12(request):
        page ='2021-06-23'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-23/12.html', context) 


    def no_13(request):
        page ='2021-06-23'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-23/13.html', context) 


class Date2021_06_24 :
    def no_01(request):
        page ='2021-06-24'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-24/01.html', context) 

    def no_02(request):
        page ='2021-06-24'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-24/02.html', context) 

    def no_03(request):
        page ='2021-06-24'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-24/03.html', context) 

    def no_04(request):
        page ='2021-06-24'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-24/04.html', context) 
    
    def no_05(request):
        page ='2021-06-24'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './2021-06-24/05.html', context) 

class Dom :
    def dom_01(request):
        page ='2021-06-24'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './DOM/dom_01.html', context)
    def dom_02(request):
        page ='2021-06-24'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './DOM/dom_02.html', context)  
    def dom_03(request):
        page ='2021-06-24'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './DOM/dom_03.html', context)
    def dom_04(request):
        page ='2021-06-24'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './DOM/dom_04.html', context) 
    def dom_05(request):
        page ='2021-06-24'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './DOM/dom_05.html', context)

    def dom_06(request):
        page ='2021-06-24'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './DOM/dom_06.html', context)

    def dom_07(request):
        page ='2021-06-24'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './DOM/dom_07.html', context)

    def dom_08(request):
        page ='2021-06-24'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './DOM/dom_08.html', context)

    def dom_09(request):
        page ='2021-06-24'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './DOM/dom_09.html', context)

    def dom_10(request):
        page ='2021-06-24'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './DOM/dom_10.html', context)

    def dom_11(request):
        page ='2021-06-24'
        print("Date :",page)
        context = {
            'page' : page
        }
        return render(request, './DOM/dom_11.html', context)
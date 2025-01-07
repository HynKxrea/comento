#from django.http import HttpResponse
from django.shortcuts import render
from .models import MainContent

def index(request):
    #return HttpResponse("Hello World")

    content_list = MainContent.objects.order_by('-pub_date')
    #질문 목록을 pub_date의 - 역순으로 정렬
    context = {'content_list': content_list}
    return render(request, 'product/content_list.html', context)
    #content_list의 데이터를 위 파일에 적용 후 html 리턴
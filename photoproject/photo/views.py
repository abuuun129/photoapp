from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    '''トップページのビュー
    '''
    #inedx.htmlのレンダリングをする
    template_name  = 'index.html'


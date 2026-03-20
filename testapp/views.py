from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
def emp_data_view(request):
    emp_data = {
        'eno':100,
        'ename':"nani",
        'esal' :1200
    }
    res = 'Employee id {} emp name {} emp esal {}'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'])
    return HttpResponse(res)
import json
def emp_data_jsonview(request):
    emp_data = {
        'eno':100,
        'ename':"nani",
        'esal' :1200
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')

# directly coverting into json ny JsonResponse
from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data = {
        'eno':100,
        'ename':"nani",
        'esal' :1200
    }
    return JsonResponse(emp_data)

class JsonCBV(View):
    def get(self,request,*args, **kwargs ):
        # emp_data = {
        # 'eno':100,
        # 'ename':"nani",
        # 'esal' :1200
        # }
        # return JsonResponse(emp_data)
        json_data = json.dumps({'msg':'This is the get method'})
        return HttpResponse(json_data,content_type='application/json')
    
    def post(self,request,*args, **kwargs ):
        json_data = json.dumps({'msg':'This is the post method'})
        return HttpResponse(json_data,content_type='application/json')
    def put(self,request,*args, **kwargs ):
        json_data = json.dumps({'msg':'This is the put method'})
        return HttpResponse(json_data,content_type='application/json')
    def delete(self,request,*args, **kwargs ):
        json_data = json.dumps({'msg':'This is the delete method'})
        return HttpResponse(json_data,content_type='application/json')

from . mixins import HttpResponseMixin

class JsonCBVMix(HttpResponseMixin,View):
    def get(self,request,*args, **kwargs ):
        
        json_data = json.dumps({'msg':'This is the mixin get method'})
        return self.render_to_http_response(json_data)
    
    def post(self,request,*args, **kwargs ):
        json_data = json.dumps({'msg':'This is the post method'})
        return 
    def put(self,request,*args, **kwargs ):
        json_data = json.dumps({'msg':'This is the put method'})
        return HttpResponse(json_data,content_type='application/json')
    def delete(self,request,*args, **kwargs ):
        json_data = json.dumps({'msg':'This is the delete method'})
        return HttpResponse(json_data,content_type='application/json')
   
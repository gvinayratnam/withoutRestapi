from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .mixins import Serializer,HttpResponseStatus
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
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


# imptanant

from .models import Employee
# import json
from django.core.serializers import serialize
from .utils import isjson_data
@method_decorator(csrf_exempt,name='dispatch')
class ApiCurd(Serializer,HttpResponseStatus,View):
    def get_object_id(self,id): # we write this methods on the utils.py also
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist: #here we are calling the doesnotexit on employee...employee is child model.model from there the exception is comming
            emp = None
        return emp
    
    def get(self,request,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'resource does not exist'})
            # return HttpResponse(json_data,content_type='application/json',status = 404)
            return self.return_with_status(json_data,status=404)
        else:
            json_data = self.serializer('json',[emp,])

        # print(emp)
        # emp_data = {
        #     'eno' : emp.eno,
        #     'ename' : emp.ename
        # }
        # res = json.dumps(emp_data)
        # res = serialize('json',[emp,],fields = ('eno','ename'))
        # gets extra info also


        # return HttpResponse(res)
        # return HttpResponse(json_data,content_type='application/json',status = 200)
        return self.return_with_status(json_data)
    def put(self,request,id):
        emp = self.get_object_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'resource does not exist not possible to update'})
            return self.return_with_status(json_data,status=404)
        data_received = request.body
        valid_data = isjson_data(data_received)
        if not valid_data:
            json_data = json.dumps({'msg':'send valid data'})
            return self.return_with_status(json_data,status = 400)
        provided_data = json.loads(data_received) # if record exit and valid data then it comes to this line here converted to the json to dict
        original_data = {
            'eno' : emp.eno,
            'ename' : emp.ename,
            'esal': emp.esal,
            'eadd': emp.eadd
        } # this is original data 
        original_data.update(provided_data)
        form = EmployeeForm(original_data,instance=emp) #if instance is not given it will create new object and we have to tell for which object we are updating the object we have tell....if want to upadate we have to tell which object is going to update-->instance=emp
        if form.is_valid():
            form.save(commit=True)
            # if created we need to send sucesss msg
            json_msg = json.dumps({'msg':"resource created sucessfully"})
            return self.return_with_status(json_msg)
        #if validations are failed
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.return_with_status(json_data,status=400)




from .utils import isjson_data
from .forms import EmployeeForm
@method_decorator(csrf_exempt,name='dispatch')
class GetAll(Serializer,HttpResponseStatus,HttpResponseMixin,View):
    def get(self,requests):
        q = Employee.objects.all()
        # ser = serialize('json',q)
        # p_data = json.loads(ser)
        # finatl = []
        # for obj in p_data:
        #     emp_data = obj['fields']
        #     finatl.append(emp_data)
        # jsoon_data = json.dumps(finatl)
        # instead of these lets use mixin
        json_data = self.serializer(q)
        return HttpResponse(json_data,content_type = 'application/json')
    def post(self,request,*args, **kwargs):

        # json_data = json.dumps({'msg':'this is post method'})
        # return self.render_to_http_response(json_data)
        data_received = self.request.body
        print(data_received)
        valid_data = isjson_data(data_received)
        if not valid_data:
            json_data = json.dumps({'msg':'send valid data'})
            return self.return_with_status(json_data,status = 400)
        emp_data = json.loads(data_received)
        form = EmployeeForm(emp_data) # creating employye form object
        if form.is_valid():
            form.save(commit=True)
            # if created we need to send sucesss msg
            json_msg = json.dumps({'msg':"resource created sucessfully"})
            return self.return_with_status(json_msg)
        #if validations are failed
        if form.errors:  # here foms is object of employeeform it inherits modelFrom the errors are comming from that class
            json_data = json.dumps(form.errors)
            return self.return_with_status(json_data,status=400)

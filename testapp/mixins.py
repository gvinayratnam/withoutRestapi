from django.http import HttpResponse
from django.core.serializers import serialize
import json
class HttpResponseMixin:
    def render_to_http_response(self,json_data):
        return HttpResponse(json_data,content_type='application/json')
    
class Serializer:
    def serializer(self,data):
        ser = serialize('json',data)
        p_data = json.loads(ser)
        finatl = []
        for obj in p_data:
            emp_data = obj['fields']
            finatl.append(emp_data)
        jsoon_data = json.dumps(finatl)
        return jsoon_data
    
class HttpResponseStatus:
    def return_with_status(self,json_data,status=200):
        return HttpResponse(json_data,content_type = 'application/json',status=status)
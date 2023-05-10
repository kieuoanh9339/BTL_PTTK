# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from shoe_model.models import Shoe
from django.core.serializers.json import DjangoJSONEncoder
@csrf_exempt
def get_shoe_data(request):
    data = []
    resp = {}
    # This will fetch the data from the database.
    prodata = Shoe.objects.all()
    for tbl_value in prodata.values():
        data.append(tbl_value)
    # If data is available then it returns the data.
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp, cls=DjangoJSONEncoder), content_type = 'application/json')
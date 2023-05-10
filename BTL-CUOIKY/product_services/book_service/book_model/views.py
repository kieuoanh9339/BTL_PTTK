# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import json
from django.views.decorators.csrf import csrf_exempt
from book_model.models import Book
from django.core.serializers.json import DjangoJSONEncoder

# hàm kiểm tra xem đối tượng có phải là 1 instance của lớp 'book' hay ko
# Nếu đúng sẽ trả về 1 dictionary của thuộc tính 'book'
#nếu sai sẽ gọi phương thức default của DjangoJSONEncoder để xư lý
class BookEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            return {
                'title': obj.title,
                'author': obj.author,
                'publication_year': obj.publication_year,
                'description': obj.description,
                'price': obj.price,
                'inventory': obj.inventory,
                'image': obj.image.url if obj.image else None,
                'slug': obj.slug,
            }
        return super().default(obj)

@csrf_exempt
def get_book_data(request):
    data = []
    resp = {}
    # This will fetch the data from the database.
    prodata = Book.objects.all()
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


def get_book_detail(request, slug=None):
    book = get_object_or_404(Book, slug=slug)
    resp = {}
    resp['status'] = 'Success'
    resp['status_code'] = '200'
    resp['data'] = [book]
    return HttpResponse(json.dumps(resp, cls=BookEncoder), content_type='application/json')

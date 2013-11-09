from django.shortcuts import render
from django.http import HttpResponse
import httplib2
import json

# Create your views here.

def index(request):

	h=httplib2.Http('.cache')
	resp,content=h.request('https://www.bitstamp.net/api/ticker/')
	str_content=content.decode('utf-8')
	info=json.loads(str_content)
	context={'info':info}
	return render(request,'getBitInfo/index.html',context)


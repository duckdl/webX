from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
	responseContext = {}
	return render_to_response('website/index.html',
			responseContext,
			context_instance=RequestContext(request)	
			)

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

# Create your views here.

def index(request):
	return render_to_response('home.html', {}, context_instance=RequestContext(request))

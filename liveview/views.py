from django.shortcuts import render
from liveview.models import LiveCode
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import html.parser

def home(request):
	return render(request, 'index.html', {})

def oracle(request):
	if request.user.is_authenticated() and request.user.is_staff:
		return render(request, 'liveinput.html', {})
	else:
		raise Http404

def liveview(request):
	return render(request, 'liveview.html', {})

def raw_view(request, type):
	lc = LiveCode.objects.get()
	if type=='js':
		return HttpResponse(lc.raw_js)
	elif type=='css':
		return HttpResponse(lc.raw_css)
	elif type=='html':
		return HttpResponse(lc.raw_html)
	else:
		raise Http404

@csrf_exempt
def post_view(request, type):
	if request.user.is_authenticated() and request.user.is_staff and request.is_ajax():
		h = html.parser.HTMLParser()
		lc = LiveCode.objects.get()
		if type=='js':
			lc.raw_js = h.unescape(request.POST['raw'])
		elif type=='css':
			lc.raw_css = h.unescape(request.POST['raw'])
		elif type=='html':
			lc.raw_html = h.unescape(request.POST['raw'])
		else:
			raise Http404
		lc.save()
		return HttpResponse("success")
	else:
		raise Http404

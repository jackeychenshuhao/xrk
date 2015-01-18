# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from jackey.models import *
from django.template import Template,Context
from django.template.loader import get_template

def index(request):
	
	return render_to_response('index.html')

def xrk_errlogin(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/xrk_login')
	else:
		return  render_to_response('index.html',{'login_err': "Error Username or Password!"})

def xrk_login(request):
	
	return render_to_response('xrk_login.html', {'user': request.user})

def logout(request):
	user = request.user
	auth.logout(request)
	
	return HttpResponse("<h4>  %s logout success! </h4>" % user)

def config_center(request):
	ip_list = IP.objects.all()

        return render_to_response('config_center.html', {'user': request.user,'ip_list': ip_list})

def admin_center(request):

        return render_to_response('admin_center.html', {'user': request.user})

def moniter_center(request):

        return render_to_response('moniter_center.html', {'user': request.user})

def rsync_center(request):

        return render_to_response('rsync_center.html', {'user': request.user})

def getmemory(request):
	m = os.popen("free -m |grep '^Mem'|awk '{print $2, $3 - $6 - $7 }' ").read()
	b = m.split()
	total_mem = b[0]
	used_mem = b[1]
	print 'total_mem',total_mem, 'used', used_mem
	return HttpResponse('{"total_mem":%s,"used_mem": %s}' %(total_mem,used_mem))

def command_center(request):
    return render_to_response('command_center.html', {'user': request.user})
from django.shortcuts import render
import requests
from subprocess import run,PIPE
import sys
import hashlib


def button(request):
    return render(request,'home.html')



def external(request):
    inp = request.POST.get('param')
    hash1 = hashlib.md5(inp.encode('utf-8')).hexdigest()
    hash2 = hashlib.sha1(inp.encode('utf-8')).hexdigest()
    hash3 = hashlib.sha256(inp.encode('utf-8')).hexdigest()
    hash4 = hashlib.sha512(inp.encode('utf-8')).hexdigest()
    return render(request,'home.html',{'data1':hash1, 'data2':hash2, 'data3':hash3, 'data4':hash4, 'data':inp})




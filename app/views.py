"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime

import os

def tic(request):
    mySetting = os.getenv("HJK_SETTING")
    resp = "Hello from <b>tic</b> " + str(datetime.now()) + "(utc " + str(datetime.utcnow()) + ")<br>HJK_SETTING: "

    if mySetting == None:
        resp += "(not found)"
    else:
        resp += mySetting

    resp += "<br>PYTHONPATH: "

    pyhtonPath = os.getenv("PYTHONPATH")
    if pyhtonPath == None:
        resp += "(not found)"
    else:
        resp += pyhtonPath


    return HttpResponse(resp)

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

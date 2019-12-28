# Soumyadev Sanyal made this file.

from django.http import HttpResponse

def index(request):
    return HttpResponse("""
    <h1>Home Page</h1>
    <a href="http://127.0.0.1:8000/removepunc">Remove Punctuation</a><br>
    <a href="http://127.0.0.1:8000/removespace">Remove Space</a><br>
    <a href="http://127.0.0.1:8000/charcount">Count Character</a><br>

    """)
def removepunc(request):
    return HttpResponse("""
    Punctuation removed<br>
    <a href="http://127.0.0.1:8000/">Home</a>
    """)

def removespace(request):
    return HttpResponse("""
    Space removed<br>
    <a href="http://127.0.0.1:8000/">Home</a>
    """)

def charcount(request):
    return HttpResponse("""
    Character counted<br>
    <a href="http://127.0.0.1:8000/">Home</a>
    """)
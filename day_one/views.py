import random

from django.shortcuts import render
from django.http import HttpResponse

def show_number(request, number):
    answer = f"""
             <html>
                <body>
                    <p>The answer is {number}!</p>
                </body>
             </html>
             """

    return HttpResponse(answer)

def hello(request, name):
    welcome = f"""
             <html>
                <body>
                    <p>Hello {name}!</p>
                </body>
             </html>
             """

    return HttpResponse(welcome)

def random_num(request):
    number = random.randint(1, 100)
    httml_number = f"""
             <html>
                <body>
                    <p> {number} </p>
                </body>
             </html>
             """

    return HttpResponse(httml_number)

def pick_number(request, max_number):
    picked_number = random.randint(0, max_number)
    result = f"User picked: {max_number}. Random number: {picked_number}"
    return HttpResponse(result)

def pick_number2(request, min_number, max_number):
    picked_number = random.randint(min_number, max_number)
    result = f"User picked min value: {min_number} and max value: {max_number}. Random number: {picked_number}"
    return HttpResponse(result)
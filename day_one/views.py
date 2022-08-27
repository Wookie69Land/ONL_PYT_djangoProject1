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

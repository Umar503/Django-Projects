from django.http import HttpResponse
from django.shortcuts import render

def calculater(request):
    result = ''
    try:
        if request.method == "POST":
            num1 = eval(request.POST.get('number1'))
            num2 = eval(request.POST.get('number2'))
            op = request.POST.get('operation')
            
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "/":
                result = num1 / num2
            elif op == "*":
                result = num1 / num2
    except:
       result = "Invalid input."

    print(result)
    return render(request, 'form.html', {'result': result})

from django.shortcuts import render
from . models import Destination
from . models import Teams



# Create your views here.
# def home(request):
#      name="india"
#     return render(request, "home.html",{'obj':name})

# def arithmetics(request):
#     number1=request.GET['num1']
#     number2=request.GET['num2']
#     res1 = int(number1) + int(number2)
#     res2 = int(number1) - int(number2)
#     res3 = int(number1) * int(number2)
#     res4 = int(number1)/int(number2)
#     return render(request,"result.html",{'result1':res1,
#                                          'result2':res2,
#                                          'result3':res3,
#                                          'result4':res4})

def home(request):
    obj=Destination.objects.all()
    obj2=Teams.objects.all()

    return render(request, "index.html",{'result':obj,
                                         'result2':obj2})





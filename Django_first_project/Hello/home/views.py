from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # contect ={
        # 'variable1':" Ankush Is smart Boy  ",
        # 'variable2':" and His Best Friend Is very Preety Girl ",
    # }
    return render(request,'index.html')
    # return render(request,'index.html', contect)
    # return HttpResponse("this is home page")


def about(request):
    return render(request,'about.html')
    # return HttpResponse("this is about page")
    
def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is services page")
    
def project(request):
    return render(request,'project.html')
    # return HttpResponse("this is project page")

def contect(request):
    return render(request,'contect.html')
    # return HttpResponse("this is contect page")

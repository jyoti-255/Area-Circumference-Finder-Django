from django.shortcuts import render

def home(request):
    if request.POST.get("radius"):
        radius=float(request.POST.get("radius"))
        area=3.14*radius**2
        area=round(area,2)
        circum=2*3.14*radius
        circum=round(circum,2)
        msg="area="+str(area)+"circum="+str(circum)
        return render(request,"home.html",{"msg":msg})
    else:
        return render(request,"home.html")
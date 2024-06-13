from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from service.models import Service1

def home(request):
    try:
        serviceData=Service1.objects.all()
        
        data={
            'servicedata':serviceData,
            
        }
        

        
    except: 
        pass
    
    return render(request,"index.html",data)



def answer(request):
        serviceData=Service1.objects.all()
        score=0
       
        
        if request.method == "POST":
            score = 0
            count=0
            li=[]
            wrong=0
            for key, value in request.POST.items():
               
                
               
                if key != 'csrfmiddlewaretoken':
                    qkey = key
                    count+=1

    
                    # qvalue = int(value)
                    service1 = Service1.objects.get(id=qkey)
                    # print(service1)
                    if value == service1.answer:
                        score += 1
                    else:
                        wrong+=1
                        li.append(service1)
                data={
                     'score':score,
                     'count':count,
                     'li':li,
                     'wrong':wrong
                }     
            
            return render(request,'ans.html', data)
                
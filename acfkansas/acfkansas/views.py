from django.shortcuts import render
#from django.http import HttpResponse




def home(request):
    
    context = {
               
        }
    
    return render(request, 'core/index.html', context)
    

def about(request, about_type):
    
    context = {
               
        'about_type': about_type,
        }
    
    return render(request, 'core/about.html', context)

def ministry(request, ministry_type):
    
    context = {
               
        'ministry_type': ministry_type,
        }
    
    return render(request, 'core/ministry.html', context)

def contact(request):
    
    context = {

        }
    
    return render(request, 'core/contact.html', context)

def resources(request, resources_type):
    
    context = {
               
        'resources_type': resources_type,
        }
    
    return render(request, 'core/resources.html', context)
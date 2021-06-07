from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import Account,ServiceName,ServiceCats
from django.contrib.auth.models import User

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'
    context['total_customers'] =Account.objects.filter(category="Customer").count()
    context['total_workers'] =Account.objects.filter(category="Worker").count()
    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def workers(request):
    
    context = {}
    context['segment'] = 'workers'
    context['workers'] =Account.objects.filter(category="Worker")
    html_template = loader.get_template( 'workers.html' )
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def home_customer(request):
    
    context = {}
    context['segment'] = 'Home'

    html_template = loader.get_template( 'index_cus.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def home_worker(request):
    
    context = {}
    context['segment'] = 'Home'

    html_template = loader.get_template( 'index_worker.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def services(request):
    
    context = {}
    context['segment'] = 'services'
    servicelist = list()
    totalservcats = ServiceCats.objects.all() 
    totalserv = ServiceName.objects.all() 
    for i in totalservcats:
        print(i)
        totalserv = ServiceName.objects.filter(name=i).count()
        print (totalserv)
        d= {"name":i.name,"count":totalserv}
        servicelist.append(d)



    context['services']=servicelist
    print(servicelist)

    html_template = loader.get_template( 'services.html' )
    return HttpResponse(html_template.render(context, request))

def register_user(request):
    
    context = {}
    context['segment'] = 'Register User'
    try:
        if request.method == 'POST':
            print("entered", request.POST)

            checkuser = User.objects.all()
            print(type(checkuser))
            if request.POST.get('password') == request.POST.get('password_confirm'):
                newuser = User.objects.create_user(request.POST.get('email'), request.POST.get('email'), request.POST.get('password'))
                newuser.first_name = request.POST.get('first_name')
                newuser.save()
                user = Account()
                print("Acc created , user model")
                print(request.POST.get('category'))
                user.category = request.POST.get('category')
                
                user.first_name = request.POST.get('first_name')
                user.last_name = request.POST.get('last_name')
                user.email = request.POST.get('email')
                user.address = request.POST.get('address')
                user.phone = request.POST.get('phone')
                user.city = request.POST.get('city')
                user.state = request.POST.get('state')
                user.country = request.POST.get('country')
                user.zipcode = request.POST.get('zipcode')
                print(user.category)
                print(user.first_name)
                print(user.email)
                print(user.last_name)
                print(user.address)
                print(user.phone)
                print(user.city)
                print(user.state)
                print(user.country)
                print(user.zipcode)
                print('++++++++++++++++++++++++++++++++++++++++++++++++')
                print(user,'++++++++++++++++++++++++++++++++++++++++++++++++')
                user.save()
                print("entered",user)
                
                print("entered new user " )
                return redirect('login')
            else:
                print("exit no match" )


        else:
            print("else+++++++++++++ " )
            # messages.success(request,'Registration Failed.Please try again later.')
            html_template = loader.get_template( 'register.html')
            return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except Exception as e:

        print("+++++++++++++",e)
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
        
def register_auth(request):
    context = {}
    context['segment'] = 'Register'

    html_template = loader.get_template( 'register.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

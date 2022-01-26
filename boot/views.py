from turtle import color, fillcolor, width
from django.shortcuts import render, redirect
from django.contrib import messages

# plots
from bokeh.plotting import figure
from bokeh.embed import components

# Create your views here.
def index(request):
    return render(request, 'boot/index.html')

# sign up
def signup(request):
    return render(request, 'boot/pages/register.html')

# loading
def loading(request):
    messages.info(request, 'MR. Dodi KABEYA')
    return render(request, 'boot/pages/loading.html')

# forgot password
def forgotPassword(request):
    return render(request, 'boot/pages/forgot.html')

# forgot password
def setPassword(request):
    return render(request, 'boot/pages/setPassword.html')

# base dashboard
def boot(request):
    return render(request, 'boot/dashboard/base/base.html')

# home dashboard
def home(request):
    y = [2, 4, 1, 7, 3, 4, 8]
    x = list(range(8))
    p = figure(tools = ['hover','pan'], tooltips = 'Day @x')
    # p.width = 455 * 2
    p.toolbar.autohide = True
    p.toolbar.logo = None
    p.height = 200
    p.grid.visible = False
    p.background_fill_color = '#3C4043'
    p.sizing_mode="stretch_width"
    col = [ i / 5 for i in y ]
    
    male = [10, 7 , 5, 6, 12]
    f = [ 2, 3, 5, 7, 9]
    m = figure(tools = ['hover','pan'], tooltips = 'Day @male')
    m.circle(f , male, color='#5cb85c', radius = [ i / 100 * 2 for i in male ])
    m.background_fill_color = '#3C4043'
    m.sizing_mode="stretch_width"
    m.grid.visible = False
    m.height = 180
    m.toolbar.autohide = True
    m.toolbar.logo = None
    
    p.vbar( x = x, top= y, bottom = 0, fill_color = '#4372DF', width= .3, fill_alpha = col
           )
    
    script, div = components(p)
    scripts, gender = components(m)
    return render(request, 'boot/dashboard/home.html', {
        'div' : div, 'script' : script,'scripts' : scripts, 'gender' : gender
    })
# team dashboard
def team(request):
    return render(request, 'boot/dashboard/team.html')

# chat dashboard
def chat(request):
    return render(request, 'boot/dashboard/chat.html')
# analyse dashboard
def analyse(request):
    return render(request, 'boot/dashboard/analyse.html')
# settings dashboard
def settings(request):
    return render(request, 'boot/dashboard/settings.html')


# profile dashboard
def profile(request):
    return render(request, 'boot/dashboard/profile.html')

# edit dashboard
def edit(request):
    return render(request, 'boot/dashboard/edit.html')

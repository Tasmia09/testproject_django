from django.shortcuts import render

# Create your views here.


def contact(request):
    #context = {'name': 'test', 'number': '123'}
    context = {}
    if request.method=='POST':

        print('Request Submitted')
        username = request.POST.get('username')
        number = request.POST.get('contactNo')

        #import pdb; pdb.set_trace()
        context={
            'name': username,
            'number': number
        }


    return render(request,'contact.html', context=context)


def home(request):
    return render(request, 'home.html')
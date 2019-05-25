from django.shortcuts import render
# from . import forms # . implies current directory(here its formapp)

from formapp.forms import FormName
# Create your views here.


def index(request):
    return render(request,'formapp/index.html')
                        #passing the page we wanna show

def form_view(request):
    form = FormName() #making instance(names) of class FormName

    if request.method == "POST":
        form = FormName(request.POST)

        if form.is_valid():
                # doing smtg after grabbing the data
                # print('VALIDATION SUCCESSFUL!')
                # print("Name: "+ form.cleaned_data['name'])
                # print("Email: "+ form.cleaned_data['email'])
                # print("Text: "+ form.cleaned_data['text'])
                # by this the submitted data will be printed in the console**

                form.save(commit=True)  #to save the form in db
                return index(request)

        else:
            print('invalid!')

    return render(request,'formapp/form_page.html',{'form':form})  #key-->form




# request.methon =="post" => someone hitting submit ie posst request

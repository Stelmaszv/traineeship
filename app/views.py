from django.shortcuts import render
from django.views.generic import TemplateView
from app.counter import KilometresPerHourCounter, FootPerHourCounter
from .forms import Calculate

class AbstractView(TemplateView):

    template_name = "main.html"           #set_templete
    context = {"form": Calculate()}       #data for templete
    Counter=None                          #instance of counter

    def get_data(self,request):
        self.Counter() #get_counter
        form = Calculate(request.POST or None)
        if form.is_valid():
            counter=self.Counter().count(form.cleaned_data.get('value'))
            self.context = {"Counter": counter, "form": Calculate()}
            return render(request, self.template_name, self.context)
        return render(request, self.template_name, self.context)

    def add_post(self,request):
        return self.get_data(request)

    def post(self, request, *args, **kwargs):
        return self.add_post(request) #action in post

    def add_get(self, request, *args, **kwargs):
        return self.get_data(request)

    def get(self, request, *args, **kwargs):
        return self.add_get(request) #action in get

class KilometresPerHourViev(AbstractView):
    template_name = "KilometresPerHour.html"    #set_templete
    Counter=KilometresPerHourCounter            #instance of counter

class FootPerHourViev(AbstractView):
    template_name = "FootPerHour.html"          #set_templete
    Counter=FootPerHourCounter                  #instance of counter


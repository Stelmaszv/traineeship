from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import Calculate


class AbstractView(TemplateView):

    template_name = "main.html" #set_templete
    context = {}                #data for templete
    stan=False

    def get_data(self,request):
        self.context = {"stan": self.stan, "form": Calculate()}
        return render(request, self.template_name, self.context)

    def add_post(self,request):
        return self.get_data()

    def post(self, request, *args, **kwargs):
        return self.add_post(request)

    def add_get(self, request, *args, **kwargs):
        return self.get_data()

    def get(self, request, *args, **kwargs):
        return self.add_get(request) #action in get

class KilometresPerHourViev(AbstractView):
    template_name = "KilometresPerHour.html" #set_templete


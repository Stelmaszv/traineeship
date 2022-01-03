from django.shortcuts import render
from django.views.generic import TemplateView

class AbstractView(TemplateView):

    template_name = "main.html"
    context = {}
    def add_get(self, request, *args, **kwargs):
        self.request = request
        return render(request, self.template_name, self.context)

    def get(self, request, *args, **kwargs):
        return self.add_get(request)

class KilometresPerHourViev(TemplateView):
    template_name = "KilometresPerHour.html"


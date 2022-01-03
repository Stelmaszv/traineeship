from django.views.generic import TemplateView

class AbstractView(TemplateView):
    template_name = "main.html"

class KilometresPerHourViev(TemplateView):
    template_name = "KilometresPerHour.html"

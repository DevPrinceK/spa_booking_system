from django.shortcuts import render
from django.views import View


class BaseView(View):
    template = "main/base.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})

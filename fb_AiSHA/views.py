# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic

class AiSHAView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World !")

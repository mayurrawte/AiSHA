# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic

class AiSHAView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == '45757815635947892':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse("Error, invalid token")

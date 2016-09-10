import json
import requests
import os
import datetime

from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from clarifai.client import ClarifaiApi
from chatbot.settings import BASE_DIR
# Create your views here.

class VisionSearch(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(FacebookBotView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
		clarifai_api = ClarifaiApi() # assumes environment variables are set.
    	my_image = request.FILES['src_img']
    	time_now = str(datetime.datetime.now())
    	st_time_list = [i for i in time_now if i.isalnum()]
    	file_str = ''.join(st_time_list)
		file_name = '/' + file_str + '.jpeg'
		file_path = BASE_DIR + file_name
		fp = open(file_path, 'w')
		fp.write(my_image)
		result = clarifai_api.tag_images(open(file_path, 'rb'))
		image_data = result.values()[3][0]
		all_tags = image_data['result']['tag']['classes']
		#handle case in case of an invalid format
		# file_data = get_S3_file('V1_Migrations/'+org_id+'/'+org_id + '.json')
	
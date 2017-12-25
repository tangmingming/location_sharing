from datetime import datetime
import time
import threading
import json
import copy
import time
from django.shortcuts import render

from django.views.generic.base import View
from django.http.response import HttpResponse, HttpResponseNotAllowed,HttpResponseBadRequest

# Create your views here.

locations = {}
matux = threading.Lock()

class Location(View):
    def post(self, request):
      print(request.body)
      try:
        data = request.body.decode("utf-8")
        datas = data.split(",")
        latitude = float(datas[0])
        longitude = float(datas[1])
        username = str(datas[2])
        if not username or username == "null":
          raise Exception("username error")
      except Exception as exc:
        return HttpResponseBadRequest("data error")
      current_time_stamp = int(time.time())
      if matux.acquire(2):
        locations[username] = {
          "latitude": latitude,
          "longitude": longitude,
          "time_stamp": current_time_stamp
        }
        matux.release()
      else:
        return HttpResponseBadRequest("server error")

      return HttpResponse(locations[username])

    def get(self, request):
      response_data = {
        "locations": []
      }
      response_data
      for username, datas in locations.items():
        spacing = int(time.time()) - datas["time_stamp"]
        if spacing <= 60*10:
          datas_1 = copy.copy(datas)
          datas_1["spacing"] = spacing
          datas_1["username"] = username
          response_data["locations"].append(datas_1)

      return HttpResponse(json.dumps(response_data))

class Test(View):
  def get(self, request):
    time.sleep(5000)
    return HttpResponse("ok")

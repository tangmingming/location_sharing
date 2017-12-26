from datetime import datetime, timedelta
import time
import threading
import json
import copy
import time

from django.core.serializers import serialize
from django.views.generic.base import View
from django.http.response import HttpResponse, HttpResponseNotAllowed,HttpResponseBadRequest, JsonResponse

from . import models
# Create your views here.

locations = {}
matux = threading.Lock()

class Location(View):
    def post(self, request):
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

      try:
        location = models.Location.objects.get(username=username)
      except Exception:
        location = models.Location()
        location.username = username

      location.latitude = latitude
      location.longitude = longitude
      location.save()
      return HttpResponse("ok")

    def get(self, request):

      locations = models.Location.objects.filter(update_time__gte=datetime.now()-timedelta(minutes=10))
      time_now = datetime.now()
      for location in locations:
        update_time = location.update_time
        location.spacing = (time_now-location.update_time.replace(tzinfo=None)).seconds
      data = serialize("json", locations)
      data = json.loads(data)
      buf = []
      for d in data:
        buf.append(d["fields"])
      data = { "locations": buf }
      return HttpResponse(json.dumps(data))

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
    return HttpResponse(json.dumps(locations))

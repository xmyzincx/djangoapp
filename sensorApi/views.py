from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt #, ensure_csrf_cookie
from django.http import Http404, HttpResponse, JsonResponse
from models import ElsysSensorData
import json

# These are the fields to be stored in the database
LOGFIELDS = [
    'deviceID',
    'deviceName',
    'payload',
    'rssi',
    'timestamp',
    'nodeTimestamp',
    'temperature',
    'humidity',
    'light',
    'pir',
    'battery',
]

# This is the decorator to exempt cross-site request forgery.
@csrf_exempt
def sensor_data(request):
    if request.method == 'POST':
        rcvd_json_data = json.loads(request.body)
        # print rcvd_json_data
        field_values = {x: rcvd_json_data.get(x, '') for x in LOGFIELDS}
        # print field_values
        tldat = ElsysSensorData(**field_values)
        try:
            tldat.save()
        except Exception as e:  # pylint: disable=broad-except
            print '%s (%s)' % (e.message, type(e))
            return JsonResponse({'mesg': 'Values not saved'})
        return JsonResponse({'mesg': 'Success'})
    else:  # Other requests
        return HttpResponse("You're at empatica sensor data API. Invalid request.")

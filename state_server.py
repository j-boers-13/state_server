from django.http import HttpResponse
from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt
from shapely.geometry import Point, Polygon
import json

SECRET_KEY = "4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh"
ROOT_URLCONF = __name__
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': False,
            'level': 'CRITICAL',
        },
    },
}

STATES_GEOMETRY = []

states_file = open("states.json", "r")
state_lines = states_file.readlines()

for state_line in state_lines:
    state_dict = json.loads(state_line)
    STATES_GEOMETRY.append(state_dict)

# Method that returns all matching states
def find_states(longitude, latitude):
    point = Point(longitude, latitude)
    matches = []

    for state in STATES_GEOMETRY:
        polygon = Polygon(state["border"])

        if polygon.contains(point):
            matches.append(state['state'])

    return matches

# Index route that only takes POST request
@csrf_exempt
def index(request):
    if request.method == "POST":
        longitude = request.POST['longitude']
        latitude = request.POST['latitude']

        matches = find_states(longitude, latitude)

        return HttpResponse(f"{json.dumps(matches)}\n", content_type="text/plain")
    else:
        return HttpResponse("This endpoint only accepts POST requests.", content_type="text/plain")


urlpatterns = [
    re_path(r"^$", index, name="index"),
]

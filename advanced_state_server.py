from django.http import HttpResponse
from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt
import geopandas
from shapely.geometry import Point
import json

SECRET_KEY = "nl$7nsm@_7=2bs=^37j)n%+yb+patcb8!5zjk+%p$mqb^=)k&r"
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

SHAPEFILE = 'shapefile/cb_2018_us_state_20m.shp'
GEOMETRY_DATAFRAME = geopandas.read_file(SHAPEFILE)

def find_state(longitude, latitude):
    point = Point(longitude, latitude) # Construct a point with given long and lat

    for index, row in GEOMETRY_DATAFRAME.iterrows():
        if row['geometry'].contains(point): # Check if the geometry contains the point
            return(row['NAME'])

@csrf_exempt
def index(request):
    if request.method == "POST":
        longitude = request.POST['longitude']
        latitude = request.POST['latitude']

        match = find_state(longitude, latitude)

        if match == None:
            return HttpResponse("[]\n", content_type="text/plain")
        else:
            return HttpResponse(f"[{json.dumps(match)}]\n", content_type="text/plain")

    else:
        return HttpResponse("This endpoint only accepts POST requests.", content_type="text/plain")


urlpatterns = [
    re_path(r"^$", index, name="index"),
]

import requests
from django.conf import settings
from django.shortcuts import render

BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"

def index(request):
    lat = lng = None
    address = ""

    if request.method == "POST":
        address = request.POST.get("address")

        response = requests.get(BASE_URL, params={
            "address": address,
            "key": settings.GOOGLE_API_KEY
        })

        data = response.json()
        if data.get("status") == "OK":
            loc = data["results"][0]["geometry"]["location"]
            lat = loc["lat"]
            lng = loc["lng"]

    return render(request, "maps/index.html", {
        "lat": lat,
        "lng": lng,
        "address": address,
        "GOOGLE_API_KEY": settings.GOOGLE_API_KEY
    })

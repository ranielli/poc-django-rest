import googlemaps
from datetime import datetime

def geocode_google_maps(adrress):
   gmaps = googlemaps.Client(key='AIzaSyBU60ndoNlQ-mGWFRk2pdJZoBPTYSMkNbU')
   geocode_result = gmaps.geocode(adrress)
   if len(geocode_result) > 0:
      longitude = geocode_result[0]['geometry']['location']['lng']
      latitude =  geocode_result[0]['geometry']['location']['lat']
   else:
      longitude = 0
      latitude = 0
   return longitude , latitude
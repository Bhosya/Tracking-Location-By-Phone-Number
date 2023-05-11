import phonenumbers
import opencage
import folium

from phonenumbers import geocoder

number = "+6288983048655"

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)


from phonenumbers import carrier

service_pro = phonenumbers.parse(number)
provider = carrier.name_for_number(service_pro, "en")
print(provider)


from opencage.geocoder import OpenCageGeocode

key = '0486b7bb8fb34e10abe9ecd090c39296'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start= 9)
folium.Marker([lat,lng], popup=location).add_to(myMap)

myMap.save("location.html")

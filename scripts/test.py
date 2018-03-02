# testing if pythonista lets me get the latlng


import location
from urllib import request

if location.is_authorized():

    location.start_updates()
    latLng = location.get_location()
    print(latLng)
    location.stop_updates()

else:
    print('location needs to be allowed')

response = request.urlopen('https://cityio.media.mit.edu')

print(response)

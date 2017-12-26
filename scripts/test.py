# testing if pythonista lets me get the latlng


import location

if location.is_authorized():
	
	location.start_updates()
	latLng = location.get_location()
	print(latLng)
	location.stop_updates()
	
else :
	print('location needs to be allowed')

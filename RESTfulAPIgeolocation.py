
>>> def reverse_geocode(lat_in , lng_in):
...   address_ = ''
...   address_ = json.dumps(gmaps.reverse_geocode( (51.4527928, -0.9745882999999)),indent = 2)
...   print (address_)
... 
>>> reverse_geocode


>>> def reverse_geocode(lat_in , lng_in):
...   address_ = json.dumps(gmaps.reverse_geocode( (lat_in, lng_in)),indent = 2)
...   print (address_['formatted_address'])
... 
>>> reverse_geocode(51.4527928,-0.9745882999999)

>>> def reverse_geocode(lat_in , lng_in):
...   address_ = json.dumps(gmaps.reverse_geocode( (lat_in, lng_in)),indent = 2)
...   print (address_)
... 

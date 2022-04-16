import gps
import time
from ISStreamer.Streamer import Streamer
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import sys, traceback
from sys import exit

geolocator = Nominatim()
session = gps.gps("127.0.0.1", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
publish_data = Streamer(bucket_name="GPS", bucket_key="CPLS9K36RHPB", access_key="XDJVOUNQoIqpir8CGpB88QIzAFmnm5wv") 
while True:
	try:
		time.sleep(0.1)
    		raw_data = session.next()
		if raw_data['class'] == 'TPV':
			if hasattr(raw_data,'lat') and hasattr(raw_data,'lon'):
				publish_data.log("Location", "{lat},{lon}".format(lat=raw_data.lat,lon=raw_data.lon))
        		        print "Latitude is = "+str(raw_data.lat)
				print "Longitude is = "+str(raw_data.lon)
				coordinates = str(raw_data.lat) + "," + str(raw_data.lon)
				where_it_is = geolocator.reverse(coordinates,timeout=10)
				publish_data.log("Vehicle is located at",where_it_is.address)
				print(where_it_is.address)
		if raw_data['class'] =='TPV':
			if hasattr(raw_data,'speed'):
				publish_data.log("Speed of the vehicle", raw_data.speed)
				print "Vehicle is moving at = "+str(raw_data.speed)+" KPH"
		if raw_data['class'] =='TPV':
			if hasattr(raw_data,'alt'):
				publish_data.log("Altitude",raw_data.alt)
				print "The altitude is = "+str(raw_data.alt)+" m"
		if raw_data['class'] == 'TPV':
			if hasattr(raw_data,'time'):
				publish_data.log("Time",raw_data.time)
				print "The curent date and time is = "+str(raw_data.time)+"\n"			
		
	except GeocoderTimedOut as e:
		publish_data.log("msg","Geocoder Timeout")
		pass
	except KeyError:
		pass
	except (KeyboardInterrupt, SystemExit):
		publish_data.close()
		print "\nEnding the current process"
		gps.running = False
		exit()
		quit()
	except StopIteration:
		session = None
		print "No incoming data from the GPS module"

		

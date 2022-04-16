import gps
import time
from ubidots import ApiClient
session = gps.gps("127.0.0.1", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
api = ApiClient(token='A1E-vQkVcPQiD9lgmkeeK3iKo9l4TCLvP6')
variable = api.get_variable('5a384d5cc03f97581e5db8cf')
 
while True:
    try:
	time.sleep(0.5)
    	raw_data = session.next()
	if raw_data['class'] == 'TPV':
		if hasattr(raw_data, 'lat')& hasattr(raw_data, 'lon'):
			latitude=raw_data.lat
                       	longitude=raw_data.lon
        		print "\nLatitude is = "+str(latitude)
			print "Latitude is = "+str(longitude)
			response = variable.save_value({'value':10, 'context':{'lat': latitude,'lng': longitude}})
    except KeyError:
		pass
    except KeyboardInterrupt:
		quit()
    except StopIteration:
		session = None
		print "No incoming data from the GPS module"


import random
import time
from ubidots import ApiClient

api = ApiClient(token='A1E-vQkVcPQiD9lgmkeeK3iKo9l4TCLvP6')
variable = api.get_variable('5a3838fdc03f9731ac28a3ce')
while(1):
    x=random.randint(1,100)
    response = variable.save_value({"value":x})
    print "\nThe random number sent to IoT dashboard is "+str(x)
    time.sleep(0.1)

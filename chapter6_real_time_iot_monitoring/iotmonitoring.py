import AS7262_Pi as spec
import time
import http.client 
import urllib.parse

#Reboot the spectrometer, just in case
spec.soft_reset()

#Set the gain of the device between 0 and 3.  Higher gain = higher readings
spec.set_gain(3)

#Set the integration time between 1 and 255.  Higher means longer readings
spec.set_integration_time(50)

#Set the board to continuously measure all colours
spec.set_measurement_mode(2)

key = "PX9QECQRVCLKD042"  # Put your API Key here

#Run this part of the script until stopped with control-C
try:
    #Turn on the main LED
    spec.enable_main_led()
    #Do this until the script is stopped:    
    def thermometer():
        while True:
                results = spec.get_calibrated_values()
                red = float(results[0])
                orange = float(results[1])
                yellow = float(results[2])
                green = float(results[3])
                blue = float(results[4])
                violet = float(results[5])
                #Print the results!
                print("Red    :" + str(results[0]))
                print("Orange :" + str(results[1]))
                print("Yellow :" + str(results[2]))
                print("Green  :" + str(results[3]))
                print("Blue   :" + str(results[4]))
                print("Violet :" + str(results[5]) + "\n")
                time.sleep(0.5)
                params = urllib.parse.urlencode({'field1': red, 'field2': orange, 'field3': yellow, 'field4': green, 'field5': blue, 'field6': violet, 'key':key }) 
                headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
                conn = http.client.HTTPConnection("api.thingspeak.com:80")
                try:
                    conn.request("POST", "/update", params, headers)
                    response = conn.getresponse()
                    print (red, orange, yellow, green, blue, violet)
                    print (response.status, response.reason)
                    data = response.read()
                    conn.close()
                except:
                    print ("connection failed")
                break
    if __name__ == "__main__":
            while True:
                    thermometer()

#When the script is stopped with control-C
except KeyboardInterrupt:
	#Set the board to measure just once (it stops after that)
	spec.set_measurement_mode(3)
	#Turn off the main LED
	spec.disable_main_led()
	#Notify the user
	print("Manually stopped")	
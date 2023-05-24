#Set the integration time between 1 and 255.  Higher means longer readings
spec.set_integration_time(50)

#Set the board to continuously measure all colours
spec.set_measurement_mode(2)

#Run this part of the script until stopped with control-C
try:
	#Turn on the main LED
	spec.enable_main_led()
	#Do this until the script is stopped:
	while True:
		#Store the list of readings in the variable "results"
		results = spec.get_calibrated_values()
		red = float(results[0])
		orange = float(results[1])
		yellow = float(results[2])
		green = float(results[3])
		blue = float(results[4])
		violet = float(results[5])
		file = open("solution.csv","a")
		file.write("{0:0.1f},{1:0.1f},{2:0.1f},{3:0.1f},{4:0.1f},{5:0.1f}".format(red, orange, yellow, green, blue, violet)+"\n")
		file.close()
		#Print the results!
		print("Red    :" + str(results[0]))
		print("Orange :" + str(results[1]))
		print("Yellow :" + str(results[2]))
		print("Green  :" + str(results[3]))
		print("Blue   :" + str(results[4]))
		print("Violet :" + str(results[5]) + "\n")

		time.sleep(0.5)

#When the script is stopped with control-C
except KeyboardInterrupt:
	#Set the board to measure just once (it stops after that)
	spec.set_measurement_mode(3)
	#Turn off the main LED
	spec.disable_main_led()
	#Notify the user
	print("Manually stopped")	
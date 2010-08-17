
# README

This package offers a Python API to the Oak series of sensors made by
[Toradex](http://www.toradex.com/En/Products/USB_Sensors_and_Peripherals).


## Supported Oak devices

The following devices have Python wrappers with the following class
names:

  * Current sensor: `ToradexCurrent`
  * MagR sensor: `ToradexMagR`
  * Motion sensor: `ToradexMotion`
  * Distance sensor: `ToradexDist`
  * Tilt sensor: `ToradexTilt`
  * Light sensor: `ToradexLux`
  * Accelerometer: `ToradexG`
  * Temperature and humidity sensor: `ToradexRH`
  * Pressure sensor: `ToradexP`
  * 8 channel A2D convertor: `Toradex8ChannelA2D`


## Requirements

pytoradex requires python-hid to be installed. You can get the latest
copy here:
[http://libhid.alioth.debian.org/](http://libhid.alioth.debian.org/)
or on Ubuntu you can install the package via the command line:

    $ sudo apt-get install python-hid 


## Installation

To install pytoradex, execute the following on the command line:

    $ pip install pytoradex


### Opening a Toredex / Oak sensor as a non-root user on Linux

Under Linux based operating systems you may find that, as a normal
user, you do not have permissions to open and read from Oak
sensors. This means that all your programs will have to be run as
`sudo` or `root`, which is a security hazard. To fix this, copy the
file `59-toradex.rules` in the folder `/etc/udev/rules.d` and restart
the udev service by typing the following at the command line:

    $ sudo udevadm trigger


## Usage

To use one of the sensors wrapped in pytoradex, first create a Python
object which corresponds to the sensor you have attached to your USB
bus, then open the sensor, then call the relevant `get_` method for
whatever reading you want to take from the sensor. For example, with
an Oak Lux sensor we might want to take an average of one hundred
readings:


    from pytoradex.toradex import ToradexLux
	import time
    
	numreadings = 100
	lux = ToradexLux()
	try:
	    lux.open()

    	    # Turn the LED on to indicate a change of state.
	    lux.led_on()
	    readings = [lux.get_lux() for i in xrange(numreadings)]
	    lux.led_off()
	    lux.close()
            
	    print 'Average light level: {0}'.format(sum(readings)/numreadings)

	except:
	    print 'Cannot open Oak Lux sensor. Please check USB cables.'
    


Every Oak sensor has the following methods which control the red LED
at the end of the PCB:

  * `blink_led`
  * `blink_led_slow`
  * `blink_led_fast`
  * `blink_led_pulse`
  * `led_on`
  * `led_off`

If you are debugging your own code you may find it useful to print out
all the date coming from the sensor to the command line. You can use
our debug utilities to do this:


    from pytoradex.toradex import ToradexG
	
	accel = ToradexG()
	accel.open()
	accel.blink_led()
	while True:
	    print(accel._debug())
	

If you have a bunch of Oak sensors connected to the USB bus, rather
than creating a Python object for each one, you can use the
`ToradexSensorCollection` class to open several devices at once:


    import time
    from pytoradex.toradex import ToradexSensorCollection
	
    collection = ToradexSensorCollection()
    print(collection.open())
    while True:
        collection._debug() # Will print output of each sensor in turn.
        time.sleep(1)


---------------------------------------

© Sarah Mount, University of Wolverhampton, 2010.

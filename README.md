# LaunchAzimuth
Launch azimuth calculator

I initially wrote this code to calculate proper launch azimuths for launching rockets and shuttles in Kerbal Space Program. I quickly adpated it to work for vehicles launched from Earth at latitudes other than the equator. It is easily operated through the command line.

The altitude of the launch site is assumed to be roughly equal to sea level.

Requires: `numpy`

## Inputs

* Inclination
	* (*Optional*)
	* Targeted orbital inclination, relative to equator, measured in degrees
	* example: `--inc=51.6`
* Altitude
	* (*Optional*)
	* Targeted orbital altitude 
	* example: `--alt=300000`
* Latitude
	* (*Optional*)
	* example: `--inc=28.5`

## Outputs

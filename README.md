# LaunchAzimuth
Launch azimuth calculator

I initially wrote this code to calculate proper launch azimuths for launching rockets and shuttles in Kerbal Space Program. I quickly adpated it to work for vehicles launched from Earth at latitudes other than the equator. It is easily operated through the command line.

The altitude of the launch site is assumed to be roughly equal to sea level. Default values are for a launch from Kennedy Space Center to a 300x300 km orbit parellel to the International Space Station (51.6°).

Requires: `python3`, `numpy`

## Inputs

* Inclination
	* (*Optional*)
	* Targeted orbital inclination, relative to equator, measured in degrees
	* default: `--inc=51.6`
* Altitude
	* (*Optional*)
	* Targeted orbital altitude in meters above sea level (must be greater than 0)
	* default: `--alt=300000`
* Latitude
	* (*Optional*)
	* Degrees latitude above or below the equator (must be less than or equal to `inclination`)
	* default: `--inc=28.5`

## Outputs

No returned outputs yet. Outputs are printed when this module is executed from the command line.

## Next steps/refinements
* Add ability to call this from another Python script, without need for command line arguments
* Add toggle for return versus printed output
* List outputs in README file

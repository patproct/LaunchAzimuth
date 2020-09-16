#!/usr/bin/env python3
# Written by Patrick Proctor
# on August 25, 2015
# https://github.com/patproct
# All units are in MKS (meters, kilograms, seconds)
# This requires numpy and argparse

import argparse, sys
import numpy as np

grav_const = 6.67384e-11
# planet mass, equatorial radius, grav const, rotational period, orbital altitide, launch site latitude
kerbin = np.array([5.2916e+22, 6e+5, grav_const, 21600, 85000, 0])
kerbin64 = np.array([2.1675e+24, 3.84e+6, grav_const, 86400, 100000, 0.1])
earth = np.array([5.972e+24, 6.371e+6, grav_const, 86164, 300000, 28.5])

# Change this variable to 'kerbin' if you want to find a launch azimuth
# in Kerbal Space Program. Be sure to mind your cmd line args if you change this.
planet = earth

def trueAlt(alt):
    # returns planetary radius plus altitude ASL
    global planet
    return alt + planet[1]

def orbitalVel(alt):
    # returns the orbital speed of the spacecraft, neglecting the ship's mass
    global planet
    
    mu = planet[0] * planet[2]
    quo = mu / trueAlt(alt)
    vel = np.sqrt(quo)
    
    return vel

def planetRot():
    # returns the rotational speed of the planet at the equator
    global planet
    return (2 * np.pi * planet[1]) / planet[3]

def betaInertial(inc,lat):
    # returns the inertial azimuth
    sine = np.cos(inc) / np.cos(lat)
    beta = np.arcsin(sine)
    return beta

def azimuth(lat,inertial,v_orb,v_rot):
    # returns the inertial launch azimuth for the rocket to target
    vxrot = (v_orb * np.sin(inertial)) - (v_rot * np.cos(lat))
    vyrot = v_orb * np.cos(inertial)
    return np.array([np.arctan(vxrot/vyrot), vxrot, vyrot])

def vBoost(xrot,yrot):
    # returns the effective delta-v needed to be produced
    return np.sqrt((np.power(xrot, 2)) + (np.power(yrot ,2)))

def main():
    global planet
    
    # The command line arguments presume a launch from Kennedy Space Center to the
    # International Space Station and an initial orbital altitude of 300 kilometers.
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("--inc", type=np.float16, default=51.6, help="target orbital inclination")
    parser.add_argument("--alt", type=np.float32, default=planet[4], help="target orbital ASL in meters")
    parser.add_argument("--lat", type=np.float32, default=planet[5], help="latitude of the launch site")
    args = parser.parse_args()
    
    # This constant is used for converting between radians and degrees.
    pi_conv = np.pi / 180
    
    inclination = args.inc * pi_conv
    altitude = args.alt
    latitude = args.lat * pi_conv
    
    # If the targeted altitude is below the altitude of the launch site, kill the script
    if altitude < 0:
        sys.exit("Targeted orbital altitude must be above sea level.")
    
    # If the targeted inclination is less than the latitude of the launch site, kill the script
    if np.absolute(args.inc) < np.absolute(args.lat):
        sys.exit("Launch site latitude cannot be less than the orbital inclination.")
    
    vOrb = orbitalVel(altitude)
    vRot = planetRot()
    beta_inert = betaInertial(inclination, latitude)
    az = azimuth(latitude, beta_inert, vOrb, vRot)
    heading = az[0] / pi_conv
    delta_v = vOrb - vBoost(az[1],az[2])
    
    if heading < 0:
        heading1 = heading + 360
    else:
        heading1 = heading
    
    heading2 = 180 - heading
    
    # Printed outputs -----------------------------------------
    print("Launch azimuth in degrees:")
    print(heading1)
    if heading1 != heading2:
        print(180 - heading)
    
    print("\nOrbital speed in meters per second:")
    print(vOrb)
    
    print("\nDelta-v required, less gravity/drag losses:")
    print(vOrb - delta_v)
    
    print("\nSpeed saved in meters per second:")
    print(delta_v)
    
    # Returned outputs ----------------------------------------
    return_array = np.array([vOrb, vRot, beta_inert, heading, delta_v])
    
if __name__ == "__main__":
    main()

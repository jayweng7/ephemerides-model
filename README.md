# ephemerides-model
Modelling planetary ephemerides - a small project to learn Python.

![Inner planets](https://github.com/jayweng7/ephemerides-model/blob/master/inner_tilt.gif)

(More gifs below)

The project totals less than 100 lines and uses data taken from JPL's HORIZONS web tool to model the solar system.
Included is data on all 8 planets + Pluto for 13 years, which gives each body's position every day until 2030-Jun-19.
Expanding this model to include asteroids, space probes and moons is possible and extremely easy, a process that entails fetching 1 .txt file from HORIZONS and adding 3 lines of code per object.
Included are separate models for the inner planets and another for the gas giants + Pluto for better viewing.
Note that the Sun is not to scale whatsoever. 

## Fetching Data
JPL's HORIZONS web tool provides the ephemeris (a table of the calculated positions of a celestial object at regular intervals throughout a period) of most objects in the solar system and can be accessed [here](https://ssd.jpl.nasa.gov/horizons.cgi)
Using this tool, setting the Sun as the coordinate centre, we select the date range and step (1 day in this case,) and ask for positions only given as x,y,z-vectors.
It returns a .txt file that looks like this:

'''
*******************************************************************************
Revised: Jul 31, 2013                  Earth                                399
 
PHYSICAL PROPERTIES (revised Sep 18, 2013):
 Mean radius, km          = 6371.01+-0.01   Mass, 10^24 kg = 5.97219+-0.0006
 Equ. radius, km          = 6378.14+-0.01   Mass layers:
 Polar axis, km           = 6356.752          Atmos          = 5.1   x 10^18 kg
 Flattening               = 1/298.257         oceans         = 1.4   x 10^21 kg
 Density, gm cm^-3        = 5.515             crust          = 2.6   x 10^22 kg
 J2  (GEM T2, 1990)       = 0.0010826265      mantle         = 4.043 x 10^24 kg
 gp, m s^-2 (polar)       = 9.8321863685      outer core     = 1.835 x 10^24 kg
 ge, m s^-2 (equatorial)  = 9.7803267715      inner core     = 9.675 x 10^22 kg
 go, m s^-2               = 9.82022         Fluid core rad   = 3480 km
 GM, km^3 s^-2            = 398600.440      Inner core rad   = 1215 km
 Mean rot. rate, rad s^-1 = 7.292115*10^-5  Surface Area:
 Sidereal period, hr      = 23.93419          land           = 1.48 x 10^8 km
 Mean solar day, days     = 1.002738          sea            = 3.62 x 10^8 km
 Moment of inertia        = 0.3308          Love no., k2     = 0.299
 Mean Temperature, K      = 270             Atm. pressure    = 1.0 bar
 Solar constant, W/m^2    = 1367.6          Vis. mag. V(1,0) = -3.86
 Volume, 10^10 km^3       = 108.321         Geometric albedo = 0.367 

DYNAMICAL CHARACTERISTICS:
 Obliquity to orbit, deg  = 23.45           Sidereal period  = 1.0000174  yrs
 Orbit velocity, km s^-1  = 29.7859         Sidereal period  = 365.25636  days
 Mean daily motion, n     = 0.9856474 deg/d Escape velocity  = 11.186 km s^-1
 Hill's sphere radius     = 234.9           Magnetic moment  = 0.61 gauss Rp^3
*******************************************************************************
 

 

*******************************************************************************
Ephemeris / WWW_USER Tue Jun 20 14:38:01 2017 Pasadena, USA      / Horizons    
*******************************************************************************
Target body name: Earth (399)                     {source: DE431mx}
Center body name: Sun (10)                        {source: DE431mx}
Center-site name: BODY CENTER
*******************************************************************************
Start time      : A.D. 2017-Jun-19 00:00:00.0000 TDB
Stop  time      : A.D. 2030-Jun-19 00:00:00.0000 TDB
Step-size       : 1440 minutes
*******************************************************************************
Center geodetic : 0.00000000,0.00000000,0.0000000 {E-lon(deg),Lat(deg),Alt(km)}
Center cylindric: 0.00000000,0.00000000,0.0000000 {E-lon(deg),Dxy(km),Dz(km)}
Center radii    : 696000.0 x 696000.0 x 696000.0 k{Equator, meridian, pole}    
Output units    : KM-S                                                         
Output type     : GEOMETRIC cartesian states
Output format   : 1 (position only)
Reference frame : ICRF/J2000.0                                                 
Coordinate systm: Ecliptic and Mean Equinox of Reference Epoch                 
*******************************************************************************
            JDTDB,            Calendar Date (TDB),                      X,                      Y,                      Z,
**************************************************************************************************************************
$$SOE
2457923.500000000, A.D. 2017-Jun-19 00:00:00.0000, -6.155424147343478E+06, -1.518815065626095E+08,  6.643649614661932E+03,
2457924.500000000, A.D. 2017-Jun-20 00:00:00.0000, -3.624395740734054E+06, -1.519748316269549E+08,  6.683147603422403E+03,
2457925.500000000, A.D. 2017-Jun-21 00:00:00.0000, -1.092115911764117E+06, -1.520251612133897E+08,  6.699006726264954E+03,
2457926.500000000, A.D. 2017-Jun-22 00:00:00.0000,  1.440663439928219E+06, -1.520324325371194E+08,  6.688853505283594E+03,
2457927.500000000, A.D. 2017-Jun-23 00:00:00.0000,  3.973173714382737E+06, -1.519966050473781E+08,  6.651979971498251E+03,
2457928.500000000, A.D. 2017-Jun-24 00:00:00.0000,  6.504633573566168E+06, -1.519176665791108E+08,  6.589610909007490E+03,
2457929.500000000, A.D. 2017-Jun-25 00:00:00.0000,  9.034255713492058E+06, -1.517956376388518E+08,  6.504888599492610E+03,
2457930.500000000, A.D. 2017-Jun-26 00:00:00.0000,  1.156125511237482E+07, -1.516305723639450E+08,  6.402534276016057E+03,
2457931.500000000, A.D. 2017-Jun-27 00:00:00.0000,  1.408485669764220E+07, -1.514225558399467E+08,  6.288267580203712E+03,
2457932.500000000, A.D. 2017-Jun-28 00:00:00.0000,  1.660430067983436E+07, -1.511716988086827E+08,  6.168150056436658E+03,
2457933.500000000, A.D. 2017-Jun-29 00:00:00.0000,  1.911884489795243E+07, -1.508781315020306E+08,  6.048015207022429E+03,
2457934.500000000, A.D. 2017-Jun-30 00:00:00.0000,  2.162776463538895E+07, -1.505419981204550E+08,  5.933074881047010E+03,
2457935.500000000, A.D. 2017-Jul-01 00:00:00.0000,  2.413035092210839E+07, -1.501634527357560E+08,  5.827708467923105E+03,
2457936.500000000, A.D. 2017-Jul-02 00:00:00.0000,  2.662590830428547E+07, -1.497426566839898E+08,  5.735390053734183E+03,
2457937.500000000, A.D. 2017-Jul-03 00:00:00.0000,  2.911375272666037E+07, -1.492797771085774E+08,  5.658695582598448E+03,
2457938.500000000, A.D. 2017-Jul-04 00:00:00.0000,  3.159320981220191E+07, -1.487749862063264E+08,  5.599342426709831E+03,
2457939.500000000, A.D. 2017-Jul-05 00:00:00.0000,  3.406361356725481E+07, -1.482284607943399E+08,  5.558231655016541E+03,
...
...
...
2462670.500000000, A.D. 2030-Jun-18 00:00:00.0000, -9.509543710420463E+06, -1.516860088083985E+08,  1.034747482605278E+04,
2462671.500000000, A.D. 2030-Jun-19 00:00:00.0000, -6.982412442849495E+06, -1.518359198665248E+08,  1.027031955035031E+04,
$$EOE
**************************************************************************************************************************
'''



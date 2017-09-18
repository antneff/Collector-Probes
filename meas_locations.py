# Program: meas_locations_v3.py
# Author:  Shawn Zamperini
# Email:   zamp@utk.edu
# Date:    4/30/17
#
# The variables in the program are pulled from the slides
# named Probe_Geo_Figures. That naming convention is followed here.


# Needed for trig functions.
import math

# Define constants used in functions below.
# Most are defined and listed in Shawn's slideset on the CP geometry.
# Probe arm inserted at angle to centerline of port axis.
offset_angle = 13.0  # in degrees
# Radial distance from vessel wall to insertion shaft mid-port
r_offset = 288.1884  # in cm
# Radial distance from probe tip to collection face at the axis of symmtry of each probe type.
alpha_A = 0.521  # in cm
# alpha_B = 0.137  # in cm
# alpha_C = 0.076  # in cm
alpha_B = 0.0323  # in cm
alpha_C = 0.0168  # in cm
# Orthonganal distance from probe axis to collection face of each probe type.
beta_A = 1.450  # in cm
beta_B = 0.508  # in cm
beta_C = 0.254  # in cm
# Radial distance from probe A tip to the tips of the other 2 probes.
lamb = 1.27
# Distance (directly) from probe tip to nearest collector probe face.
delta_A = math.sqrt(alpha_A**2 + beta_A**2)
delta_B = math.sqrt(alpha_B**2 + beta_B**2)
delta_C = math.sqrt(alpha_C**2 + beta_C**2)

# Angle between alpha and beta for each probe.
d = math.degrees(math.atan(beta_A / alpha_A))
q = math.degrees(math.atan(beta_B / alpha_B))
s = math.degrees(math.atan(beta_C / alpha_C))


def calc_R_measAD(r_probe, location):
    """Calculate the radial position of a measurement along the left A probe.
        r_probe and locations are entered in as cm. Location is from the tip of
        the probe. """

    # Angle between r_probe and A probe center axis. 180 degrees since we
    # want the higher value in quadrant II (basic trig stuff).
    c = 180 - math.degrees(math.asin(r_offset * math.sin(math.radians(offset_angle)) / r_probe))
    # Angle between r_probe and delta
    e = c - d

    # Radial position of A-D tip using law of cosines
    r_AD = math.sqrt(delta_A**2 + r_probe**2 - 2 * r_probe * delta_A * math.cos(math.radians(e)))

    # Angle between tip of left A probe and length of A-D probe. Again want
    # the higher value in quadrant II.
    f = 180 - math.degrees(math.asin(r_offset * math.sin(math.radians(offset_angle)) / r_AD))

    # Radial position of measurement location, l, along A-D. l=0 is at
    # the tip of the probe. In cm.
    r_ADmeas = math.sqrt(location**2 + r_AD**2 - 2 * location * r_AD * math.cos(math.radians(f)))

    return r_ADmeas


def calc_R_measAU(r_probe, location):
    """
    Calculate the radial position of a measurement along the right A probe.
    """

    # Angle between r_probe and A probe center axis. 180 degrees since we
    # want the higher value in quadrant II (basic trig stuff).
    c = 180 - math.degrees(math.asin(r_offset * math.sin(math.radians(offset_angle)) / r_probe))

    # Angle between r-probe and delta
    k = 360 - d - c

    # Radial position of the tip of the right A probe.
    r_AU = math.sqrt(delta_A**2 + r_probe**2 - 2 * r_probe * delta_A * math.cos(math.radians(k)))

    # Angle between length of probe and radial position vector of the tip.
    m = 180 - math.degrees(math.asin(r_offset * math.sin(math.radians(offset_angle)) / r_AU))

    r_AUmeas = math.sqrt(location**2 + r_AU**2 - 2 * location * r_AU * math.cos(math.radians(m)))

    return r_AUmeas


def calc_R_measBD(r_probe, location):
    """Calculate the radial position of a measurement along the left B probe."""

    # Angle between r_probe and A probe center axis. 180 degrees since we
    # want the higher value in quadrant II (basic trig stuff).
    c = 180.0 - math.degrees(math.asin(r_offset * math.sin(math.radians(offset_angle)) / r_probe))

    # Follows same logic as A probes. Refer to slides.
    r_Btip = math.sqrt(r_probe**2 + lamb**2 - 2 * r_probe * lamb * math.cos(math.radians(c)))
    f = math.degrees(math.asin(r_probe * math.sin(math.radians(c)) / r_Btip))
    n = 180.0 - f - q
    r_BD = math.sqrt(delta_B**2 + r_Btip**2 - 2 * delta_B * r_Btip * math.cos(math.radians(n)))
    v = 180.0 - math.degrees(math.asin(r_offset * math.sin(math.radians(offset_angle)) / r_BD))

    r_BDmeas = math.sqrt(location**2 + r_BD**2 - 2 * location * r_BD * math.cos(math.radians(v)))

    return r_BDmeas


def calc_R_measBU(r_probe, location):
    """Calculate the radial position of a measurement along the right B probe."""

    # Angle between r_probe and A probe center axis. 180 degrees since we
    # want the higher value in quadrant II (basic trig stuff).
    c = 180.0 - math.degrees(math.asin(r_offset * math.sin(math.radians(offset_angle)) / r_probe))

    r_Btip = math.sqrt(r_probe**2 + lamb**2 - 2 * r_probe * lamb * math.cos(math.radians(c)))
    f = math.degrees(math.asin(r_probe * math.sin(math.radians(c)) / r_Btip))
    n = 180.0 - f - q

    # Refer to slides for picture.
    r_BU = math.sqrt(r_Btip**2 + delta_B**2 - 2 * r_Btip * delta_B *
                     math.cos(math.radians(360 - (n + q + q))))
    p = 180.0 - math.degrees(math.asin(r_offset * math.sin(math.radians(offset_angle)) / r_BU))

    r_BUmeas = math.sqrt(location**2 + r_BU**2 - 2 * location * r_BU * math.cos(math.radians(p)))

    return r_BUmeas


def calc_R_measCD(r_probe, location):
    """Calculate the radial position of a measurement along the left C probe."""

    c = 180.0 - math.degrees(math.asin(r_offset * math.sin(math.radians(offset_angle)) / r_probe))
    r_Ctip = math.sqrt(r_probe**2 + lamb**2 - 2 * r_probe * lamb * math.cos(math.radians(c)))
    f = math.degrees(math.asin(r_probe * math.sin(math.radians(c)) / r_Ctip))
    n = 180.0 - f - s
    r_CD = math.sqrt(delta_C**2 + r_Ctip**2 - 2 * delta_C * r_Ctip * math.cos(math.radians(n)))
    v = 180.0 - math.degrees(math.asin(r_offset * math.sin(math.radians(offset_angle)) / r_CD))

    r_CDmeas = math.sqrt(location**2 + r_CD**2 - 2 * location * r_CD * math.cos(math.radians(v)))

    return r_CDmeas


def calc_R_measCU(r_probe, location):
    """Calculate the radial position of a measurement along the right C probe."""

    c = 180.0 - math.degrees(math.asin(r_offset * math.sin(math.radians(offset_angle)) / r_probe))
    r_Ctip = math.sqrt(r_probe**2 + lamb**2 - 2 * r_probe * lamb * math.cos(math.radians(c)))
    f = math.degrees(math.asin(r_probe * math.sin(math.radians(c)) / r_Ctip))
    n = 180.0 - f - s
    r_CU = math.sqrt(r_Ctip**2 + delta_C**2 - 2 * r_Ctip * delta_C *
                     math.cos(math.radians(360 - (n + s + s))))
    p = 180.0 - math.degrees(math.asin(r_offset * math.sin(math.radians(offset_angle)) / r_CU))

    r_CUmeas = math.sqrt(location**2 + r_CU**2 - 2 * location * r_CU * math.cos(math.radians(p)))

    return r_CUmeas

# ===================================
# Base Units
# ===================================

METER = 1.0
KILOMETER = 1e3
CENTIMETER = 1e-2
MILLIMETER = 1e-3


# ===================================
# Distance Conversions
# ===================================

KM_TO_M  = 1e3
M_TO_KM  = 1e-3

AU_TO_M  = 1.496e11
M_TO_AU  = 1 / AU_TO_M

LY_TO_M  = 9.4607e15
M_TO_LY  = 1 / LY_TO_M

PC_TO_M  = 3.0857e16
M_TO_PC  = 1 / PC_TO_M


# ===================================
# Time Units
# ===================================

SECOND = 1.0
MINUTE = 60.0
HOUR   = 3600.0
DAY    = 86400.0
YEAR   = 365.25 * DAY


# ===================================
# Mass Units
# ===================================

KILOGRAM = 1.0
GRAM     = 1e-3
TON      = 1e3

SOLAR_MASS = 1.98847e30
EARTH_MASS = 5.9722e24
MOON_MASS  = 7.342e22
JUPITER_MASS = 1.898e27


# ===================================
# Quick Conversion Helpers (constants only)
# ===================================

KG_TO_SOLAR   = 1 / SOLAR_MASS
SOLAR_TO_KG   = SOLAR_MASS

KG_TO_EARTH   = 1 / EARTH_MASS
EARTH_TO_KG   = EARTH_MASS

KG_TO_MOON    = 1 / MOON_MASS
MOON_TO_KG    = MOON_MASS

KG_TO_JUPITER = 1 / JUPITER_MASS
JUPITER_TO_KG = JUPITER_MASS

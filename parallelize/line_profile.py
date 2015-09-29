"""Test code for kernprof.py"""

import numpy as np
import dust
import sigma_scat as ss

# Set up the grain size distribution.  Let's assume all the dust grains are silicate.

AMIN, AMAX = 0.005, 0.25 # microns
NA  = 5  # number of points to use to sample distribution
RHO = 3.8 # grain density (g cm^-3)
P   = 3.5 # power law slope

mrn = dust.Dustdist( rad=np.linspace(AMIN,AMAX,NA), rho=RHO, p=P )

# Calculate the scattering and extinction opacity
ENERGY = np.logspace(-1,1,50)
MDUST  = 1.e22 * dust.c.mp() * 0.009  # magic numbers (dust mass per 10^22 H)

kappascat = ss.Kappascat( E=ENERGY, dist=dust.Dustspectrum(rad=mrn), scatm=ss.makeScatmodel('Mie','Silicate') )

kappascat()

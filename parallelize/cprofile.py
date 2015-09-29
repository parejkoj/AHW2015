# ## Slow example
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

import dust
import sigma_scat as ss

# Set up the grain size distribution.  Let's assume all the dust grains are silicate.

AMIN, AMAX = 0.005, 0.25 # microns
NA  = 50  # number of points to use to sample distribution
RHO = 3.8 # grain density (g cm^-3)
P   = 3.5 # power law slope

mrn = dust.Dustdist( rad=np.linspace(AMIN,AMAX,NA), rho=RHO, p=P )

# Calculate the scattering and extinction opacity
ENERGY = np.logspace(-1,1,50)
MDUST  = 1.e22 * dust.c.mp() * 0.009  # magic numbers (dust mass per 10^22 H)
kappascat = ss.Kappascat( E=ENERGY, dist=dust.Dustspectrum(rad=mrn), scatm=ss.makeScatmodel('Mie','Silicate'))

# The Python Profiler helps you identify the bottlenecks in your code. In general, you want to use the C version of it: cProfile. The simplest way to run it is to execute it via: `cProfile.run(command,filename)`, where command is a string containing the command you wish to profile, and filename is the file you want to write the results to.
import cProfile
import pstats

profile_name = 'Kappascat.prof'
cProfile.run("kappascat(with_mp=False)",filename=profile_name)
# cProfile.run("kappascat(with_mp=True)",filename=profile_name)

stats = pstats.Stats(profile_name)
stats.strip_dirs()
stats.sort_stats('cumtime').print_stats(10)


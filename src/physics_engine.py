# Core physics functions
import numpy as np
from astropy import constants as const
from astropy import units as u
from scipy.integrate import quad

class CosmologyEngine:
    def __init__(self, H0=70, Om0=0.3, Ol0=0.7, Or0=0.0):
        """
        Initialize with standard cosmological parameters.
        H0: Hubble constant at z=0 (km/s/Mpc)
        Om0: Matter density parameter
        Ol0: Cosmological constant (Lambda) density parameter
        Or0: Radiation density parameter
        """
        self.H0 = H0
        self.Om0 = Om0
        self.Ol0 = Ol0
        self.Or0 = Or0
        # Curvature density (derived)
        self.Ok0 = 1.0 - (Om0 + Ol0 + Or0)

    def hubble_parameter(self, z):
        """Calculates H(z)"""
        # E(z) = sqrt(Or(1+z)^4 + Om(1+z)^3 + Ok(1+z)^2 + Ol)
        zp1 = 1 + z
        Ez = np.sqrt(self.Or0 * zp1**4 + 
                     self.Om0 * zp1**3 + 
                     self.Ok0 * zp1**2 + 
                     self.Ol0)
        return self.H0 * Ez

    def lookback_time(self, z):
        """Placeholder for integration logic we will add in the notebook"""
        pass

    def luminosity_distance(self, z):
        """
        Calculates the Luminosity Distance d_L in Mpc.
        d_L = (1+z) * d_H * integral(1/E(z') dz') from 0 to z
        (Assuming a flat universe for simplicity)
        """
        dh = 299792.458 / self.H0  # Hubble Distance in Mpc (c/H0)
        
        # Define the integrand 1/E(z)
        integrand = lambda z_prime: 1.0 / (self.hubble_parameter(z_prime) / self.H0)
        
        integral, _ = quad(integrand, 0, z)
        return (1 + z) * dh * integral

    def distance_modulus(self, z):
        """Calculates mu = 5 * log10(dL / 10pc)"""
        dl = self.luminosity_distance(z)
        if dl <= 0: return 0
        return 5 * np.log10(dl * 1e6 / 10)
    
    def redshift_recombination(self):
        """
        A simple approximation for the redshift when photons decoupled from matter.
        Standard Lambda-CDM value is roughly 1090.
        """
        return 1089.0  # Planck 2018 benchmark

    def sound_horizon(self):
        """
        The distance a sound wave could travel in the plasma before recombination.
        This sets the 'first peak' scale in the CMB.
        """
        # Simplified approximation: r_s approx 147 Mpc
        return 147.0
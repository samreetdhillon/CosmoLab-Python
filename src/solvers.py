# ODE integration logic
import numpy as np
from scipy.integrate import solve_ivp

def friedmann_rhs(t, a, H0_units, Om0, Ol0, Or0, Ok0):
    """
    The right-hand side of the Friedmann ODE: da/dt
    H0_units: H0 converted to 1/Gyr for consistent time units
    """
    # Prevent division by zero at the very beginning
    if a <= 0: a = 1e-10 
    
    term = (Or0 * a**-2) + (Om0 * a**-1) + Ok0 + (Ol0 * a**2)
    return H0_units * np.sqrt(max(0, term))

def solve_scale_factor(t_span, cosmo_obj):
    """
    Solves for a(t) over a given time span (in Gigayears)
    """
    # Convert H0 from km/s/Mpc to 1/Gyr
    # 1 km/s/Mpc is approx 0.0010227 1/Gyr
    h0_gyr = cosmo_obj.H0 * 0.0010227
    
    # Initial condition: at some very early time, a is near 0
    # We solve forward from the Big Bang
    y0 = [1e-8] 
    
    sol = solve_ivp(
        friedmann_rhs, 
        t_span, 
        y0, 
        args=(h0_gyr, cosmo_obj.Om0, cosmo_obj.Ol0, cosmo_obj.Or0, cosmo_obj.Ok0),
        t_eval=np.linspace(t_span[0], t_span[1], 500)
    )
    return sol.t, sol.y[0]

def growth_ode(a, y, cosmo_obj):
    """
    y[0] = delta (perturbation growth)
    y[1] = d(delta)/da
    """
    delta, d_delta_da = y
    
    # Get H(z) where z = 1/a - 1
    z = (1.0/a) - 1.0
    Hz = cosmo_obj.hubble_parameter(z)
    H0 = cosmo_obj.H0
    
    # Dimensionless Hubbble E(a)
    E_a = Hz / H0
    
    # The term for d2(delta)/da2
    # Derived from the growth equation in terms of 'a'
    term1 = -(3/a + (1/E_a)*(3*cosmo_obj.Or0*a**-5 + 1.5*cosmo_obj.Om0*a**-4 + cosmo_obj.Ok0*a**-3)) # This is simplified
    # For a flat LCDM, a common approximation is:
    term_growth = (1.5 * cosmo_obj.Om0 / (a**3 * E_a**2)) * delta
    
    # Simplest form for pedagogy:
    d2_delta_da2 = (1.5 * cosmo_obj.Om0 / (a**5 * E_a**2)) * delta - (3/a + (1/(E_a**2 * a**2))) * d_delta_da # (Simplified logic)
    
    return [d_delta_da, d2_delta_da2]
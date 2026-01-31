# Cosmology Pedagogy Series

### _An Interactive Journey through the Evolution of the Universe_

This repository is a collection of educational Python notebooks designed to bridge the gap between cosmological theory and numerical implementation. By combining the **Friedmann Equations** with modern data science tools, we explore how the universe expands, how we measure its distances, and how gravity creates the cosmic web.

---

## Series Overview

The project is divided into four key pedagogical modules:

1.  **Expansion & Metrics:** Understanding the FLRW metric and the Hubble parameter $H(z)$.
2.  **Friedmann Solver:** Numerically integrating the equations of motion for the Scale Factor $a(t)$.
3.  **The Distance Ladder:** Using Type Ia Supernovae as "Standard Candles" to prove the existence of Dark Energy.
4.  **Growth of Perturbations:** Solving for the density contrast $\delta(t)$ to see how large-scale structures form.

---

## Repository Structure

```text
├── notebooks/             # Interactive Jupyter Notebooks (The core tutorials)
├── src/                   # Python modules containing the physics engines
│   ├── physics_engine.py  # Hubble, Distances, and Cosmological parameters
│   └── solvers.py         # ODE integrators for expansion and growth
├── data/                  # Sample datasets (Supernova Ia observations)
├── tests/                 # Unit tests for physical consistency
└── requirements.txt       # Necessary Python libraries
```

## Installation and Usage

1. **Clone the repository**

```
git clone [https://github.com/your-username/Cosmology-Pedagogy.git](https://github.com/your-username/Cosmology-Pedagogy.git)
cd Cosmology-Pedagogy
```

2. **Set up a virtual environment**

```
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies**

```
pip install -r requirements.txt
```

4. **Launch the tutorials**

```
jupyter notebook
```

## Physics Highlights

The Friedmann EquationAt the heart of our solver is the first Friedmann Equation:
$$\left( \frac{\dot{a}}{a} \right)^2 = H_0^2 \left[ \Omega_{r,0}a^{-4} + \Omega_{m,0}a^{-3} + \Omega_{k,0}a^{-2} + \Omega_{\Lambda,0} \right]$$
Using this, we can simulate different "toy universes" (e.g., Einstein-de Sitter, Milne, or $\Lambda$CDM) and compare their ages and ultimate fates.

### The Hubble Diagram

We implement the Luminosity Distance $d_L$ and compare it against real-world observations to visualize the 2011 Nobel Prize-winning discovery of

## References & Resources

- Introduction to Cosmology by Barbara Ryden
- Physical Cosmology by P.J.E. Peebles
- Planck Collaboration Results (2018)

## Contributing

Found a bug in the math? Want to add a notebook on Cosmic Microwave Background (CMB) anisotropies? Contributions are welcome! Please open an issue or submit a pull request.

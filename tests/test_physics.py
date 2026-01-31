import os
import sys
import unittest
# Ensure project root is on sys.path when running this test directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.physics_engine import CosmologyEngine

class TestCosmology(unittest.TestCase):
    def setUp(self):
        # Benchmark: Planck 2018 parameters
        self.cosmo = CosmologyEngine(H0=67.4, Om0=0.315, Ol0=0.685)

    def test_hubble_today(self):
        """H(z=0) must equal H0"""
        self.assertAlmostEqual(self.cosmo.hubble_parameter(0), 67.4, places=2)

    def test_flatness(self):
        """In a flat universe, Ok0 should be 0"""
        self.assertAlmostEqual(self.cosmo.Ok0, 0.0, places=5)

    def test_distance_modulus_near(self):
        """At very low redshift, distance modulus should be small but positive"""
        mu = self.cosmo.distance_modulus(0.01)
        self.assertGreater(mu, 30) # Typical value for z=0.01

if __name__ == '__main__':
    unittest.main()
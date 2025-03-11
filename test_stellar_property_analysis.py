import unittest
import numpy as np
from scipy.constants import h, c, k, sigma as stefan_boltzmann_constant
from stellar_property_analysis import calculate_luminosity, planck_spectrum


class TestStellarPropertyAnalysis(unittest.TestCase):
    def test_calculate_luminosity(self):
        R = np.array([1.0])
        Teff = np.array([1000.0])
        expected_luminosity = 4 * np.pi * R[0] ** 2 * stefan_boltzmann_constant * Teff[0] ** 4
        result = calculate_luminosity(R, Teff)
        self.assertEqual(len(result), 1)
        self.assertTrue(np.isclose(result[0], expected_luminosity, rtol=1e-3))

    def test_planck_spectrum(self):
        wavelength = np.array([1e-6])
        T = 1000.0
        expected_brightness = (2 * h * c ** 2 / (wavelength[0] ** 5)) * (1 / (np.exp(h * c / (wavelength[0] * k * T)) - 1))
        result = planck_spectrum(wavelength, T)
        self.assertEqual(len(result), 1)
        self.assertTrue(np.isclose(result[0], expected_brightness, rtol=1e-3))


if __name__ == "__main__":
    unittest.main()

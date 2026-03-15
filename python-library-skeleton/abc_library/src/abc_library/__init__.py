"""
ABC Library - A sample Python library
"""

__version__ = "1.0.0"
__author__ = "Shadhini Jayatilake"
__email__ = "shadhini.jayatilake@gmail.com"

from .package_a.core import A1, A2
from .package_b.utils import utility_function_a, utility_function_b

__all__ = ['A1', 'A2', 'utility_function_a', 'utility_function_b']

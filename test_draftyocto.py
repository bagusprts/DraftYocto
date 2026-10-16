# test_draftyocto.py
"""
Tests for DraftYocto module.
"""

import unittest
from draftyocto import DraftYocto

class TestDraftYocto(unittest.TestCase):
    """Test cases for DraftYocto class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DraftYocto()
        self.assertIsInstance(instance, DraftYocto)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DraftYocto()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

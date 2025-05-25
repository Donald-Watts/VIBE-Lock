"""
VIBE-Lock - Vast Intelligence-Based Extraction Containment Toolkit
"""

__version__ = "0.0.1a1"
__author__ = "Donald Watts"
__license__ = "MIT"

from .vibe_init import main as init_main
from .vibe_stamp import main as stamp_main
from .vibe_scan import main as scan_main

__all__ = ['init_main', 'stamp_main', 'scan_main'] 
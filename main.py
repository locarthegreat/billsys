#!/usr/bin/env python3
"""
Apartment Billing Management System - Main Entry Point
"""

import sys
from pathlib import Path

# Add the frontend_modules directory to the path
sys.path.insert(0, str(Path(__file__).parent / "frontend_modules"))

# Import directly from frontend_new module file
from frontend_new import ModernLoginUI


def main():
    """Main entry point for the application"""
    # Create and run login window
    login_app = ModernLoginUI()
    login_app.mainloop()


if __name__ == "__main__":
    main()

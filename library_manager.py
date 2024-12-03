import os
import sys

def is_installed(package):
    """Check if a package is installed."""
    try:
        __import__(package)
        return True
    except ImportError:
        return False

def install_package(package_name):
    """Install a package using pip."""
    print(f"{package_name} is not installed. Installing now...")
    os.system(f"{sys.executable} -m pip install {package_name}")

# Required libraries for the project
required_packages = {
    "docx": "python-docx",
    "colorama": "colorama",
    "requests": "requests",
    "bs4": "beautifulsoup4"
}

if __name__ == "__main__":
    checked_packages = set()
    for module_name, pip_name in required_packages.items():
        if module_name not in checked_packages:
            if is_installed(module_name):
                print(f"{module_name} is already installed.")
            else:
                install_package(pip_name)
            checked_packages.add(module_name)

    print("All required libraries have been checked and installed.")

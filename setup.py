from distutils.core import setup
import py2exe

setup(console=['main.py'],
      options={
          "py2exe": {
              "optimize": 2,
              "includes": [],  # List of all the modules you want to import
              "packages": ["collections"]}
      }
      )

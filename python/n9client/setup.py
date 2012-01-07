from distutils.core import setup
import os, sys, glob

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name="n9client",
      scripts=['n9client'],
      version='0.1.0',
      maintainer="Juha Autero",
      maintainer_email="email@example.com",
      description="A PySide example",
      long_description=read('n9client.longdesc'),
      data_files=[('share/applications',['n9client.desktop']),
                  ('share/icons/hicolor/64x64/apps', ['n9client.png']),
                  ('share/n9client/qml', glob.glob('qml/*.qml')), ],)

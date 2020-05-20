#!/usr/bin/env bash

# Compiles the script into an app and changes the icon. use AS SUDO

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

python3 setup.py py2app -A

mv dist/ScaylaCompanion.app/Contents/Resources/PythonApplet2.icns dist/ScaylaCompanion.app/Contents/Resources/PythonApplet.icns
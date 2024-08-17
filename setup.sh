#!/bin/bash

wget https://github.com/hbldh/bleak/archive/refs/tags/v0.22.2.zip && unzip v0.22.2.zip && rm v0.22.2.zip
wget https://github.com/Bluetooth-Devices/dbus-fast/archive/refs/tags/v2.22.1.zip && unzip v2.22.1.zip && rm v2.22.1.zip
cp /storage/.kodi/addons/script.module.typing_extensions/lib/typing_extensions.py ./bleak-0.22.2

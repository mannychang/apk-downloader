#!/bin/sh

find apks/ -name *.apk -exec adb install -r {} \;

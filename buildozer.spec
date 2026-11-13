[app]
title = Math Tools
package.name = mathtools
package.domain = org.mathtools

source.dir = .
source.include_exts = py
source.exclude_dirs = .github, bin, .buildozer, __pycache__

version = 1.0.0
requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

# The app is fully offline: no permissions needed (no INTERNET, no storage).
android.permissions =
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.allow_backup = False

[buildozer]
log_level = 2
warn_on_root = 1

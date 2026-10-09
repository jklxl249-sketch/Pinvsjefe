[app]
title = Pin vs Jefe
package.name = pinvsjefe
package.domain = org.pin
source.dir =.
version = 1.0
requirements = python3,kivy==2.3.0,pillow
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.allow_backup = False

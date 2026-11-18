[app]

title = UZBEK IZOHLI LUGAT

package.name = uzbekizohlilugat
package.domain = org.uzbeklugat

source.dir = .
source.include_exts = py,json,kv,png,jpg

version = 1.0.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.archs = arm64-v8a, armeabi-v7a

android.api = 35
android.minapi = 23

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
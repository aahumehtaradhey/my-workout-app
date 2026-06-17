[app]
title = Fitness Boss
package.name = fitnessboss
package.domain = org.radhe
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy

# Play Store ke liye .aab bundle banna zaroori hai
android.release_artifact = aab

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.api = 33
android.minapi = 21

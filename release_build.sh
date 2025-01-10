#!/bin/bash

# Clean previous builds
./gradlew clean

# Generate release APK
./gradlew assembleRelease

# Verify APK is created
APK_PATH="app/build/outputs/apk/release/app-release.apk"

if [ -f "$APK_PATH" ]; then
    echo "Release APK successfully generated!"
    echo "Location: $APK_PATH"
    
    # Optional: Generate SHA256 checksum
    shasum -a 256 "$APK_PATH" > "$APK_PATH.sha256"
else
    echo "Error: Release APK not generated"
    exit 1
fi

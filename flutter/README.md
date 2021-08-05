## Installation
[I am using macOS Big Sur 11.5]
[Flutter has some pretty good documentation here](https://flutter.dev/docs/get-started/install)
Some errors I encountered during installation that weren't documented on the Flutter Website are:
> `flutter doctor`
> Unable to find bundled Java version

Navigate to the Android Studio location in Applications and add symbolic link to jre
ln -s ../jre jdk

If running `flutter doctor --android-licenses` gives NoClassDefFoundError, install Android SDK Command-line tools in Android Studios (not installed by default)
[Installation steps](https://stackoverflow.com/questions/61993738/flutter-doctor-android-licenses-gives-a-java-error):
1. Tools > SDK Manager
2. Appearance & Behaviour > System Settings > Android SDK
3. SDK Tools
4. Apply `Android SDK Command-line tools` and it will begin download (~1GB)

Then rerun flutter doctor :)

## Running Flutter
`flutter clean; flutter run`
I like how hitting `r` will hard reset while running :)

Run Android:
Set up 


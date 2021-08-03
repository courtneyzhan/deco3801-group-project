package com.example.together_app
import com.tekartik.sqflite.SqflitePlugin
import io.flutter.embedding.android.FlutterActivity

class MainActivity: FlutterActivity() {
        SqflitePlugin.registerWith(registrarFor("com.tekartik.sqflite.SqflitePlugin"))

}

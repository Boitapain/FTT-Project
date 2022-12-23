package com.mtu.ftt_mobile

import android.Manifest
import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat


class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        ActivityCompat.requestPermissions(
            this@MainActivity,
            arrayOf(Manifest.permission.INTERNET),
            0
        )
        mainActivityContext = this
    }

    fun login(v: View?) {
        val intent = Intent(this, LoginActivity::class.java)
        startActivityForResult(intent, 2)
    }

    fun register(v: View?) {
        val intent = Intent(this, RegisterActivity::class.java)
        startActivity(intent)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        val responseText = findViewById<TextView>(R.id.responseText)
        if (requestCode == 2) { // Login
            responseText.text = "Successful Login."
            startActivity(Intent(this, HomeActivity::class.java))
        } else {
            responseText.text = "Invalid or no data entered. Please try again."
        }
    }

    companion object {
        var mainActivityContext: Context? = null
        var postUrl = "http://10.0.2.2:5000"
    }
}
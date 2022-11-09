package com.mtu.ftt_mobile

import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import okhttp3.*
import org.json.JSONException
import org.json.JSONObject
import java.io.IOException


class RegisterActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_register)
    }

    fun register(v: View?) {
        val usernameView = findViewById<EditText>(R.id.username)
        val firstNameView = findViewById<EditText>(R.id.firstName)
        val lastNameView = findViewById<EditText>(R.id.lastName)
        val passwordView = findViewById<EditText>(R.id.password)
        val username = usernameView.text.toString().trim { it <= ' ' }
        val firstName = firstNameView.text.toString().trim { it <= ' ' }
        val lastName = lastNameView.text.toString().trim { it <= ' ' }
        val password = passwordView.text.toString().trim { it <= ' ' }
        if (firstName.length == 0 || lastName.length == 0 || username.length == 0 || password.length == 0) {
            Toast.makeText(
                applicationContext,
                "Something is wrong. Please check your inputs.",
                Toast.LENGTH_LONG
            ).show()
        } else {
            val registrationForm = JSONObject()
            try {
                registrationForm.put("subject", "register")
                registrationForm.put("firstname", firstName)
                registrationForm.put("lastname", lastName)
                registrationForm.put("username", username)
                registrationForm.put("password", password)
            } catch (e: JSONException) {
                e.printStackTrace()
            }
            val body = RequestBody.create(
                MediaType.parse("application/json; charset=utf-8"),
                registrationForm.toString()
            )
            postRequest(MainActivity.postUrl, body)
        }
    }

    fun postRequest(postUrl: String?, postBody: RequestBody?) {
        val client = OkHttpClient()
        val request = Request.Builder()
            .url(postUrl)
            .post(postBody)
            .header("Accept", "application/json")
            .header("Content-Type", "application/json")
            .build()
        client.newCall(request).enqueue(object : Callback {
            override fun onFailure(call: okhttp3.Call, e: IOException) {
                call.cancel()
                Log.d("FAIL", e.message!!)
                runOnUiThread {
                    val responseText = findViewById<TextView>(R.id.responseTextRegister)
                    responseText.text = "Failed to Connect to Server. Please Try Again."
                }
            }

            override fun onResponse(call: okhttp3.Call, response: Response) {
                val responseTextRegister = findViewById<TextView>(R.id.responseTextRegister)
                try {
                    val responseString = response.body()!!.string().trim { it <= ' ' }
                    runOnUiThread {
                        if (responseString == "success") {
                            responseTextRegister.text = "Registration completed successfully."
                            finish()
                        } else if (responseString == "username") {
                            responseTextRegister.text =
                                "Username already exists. Please chose another username."
                        } else {
                            responseTextRegister.text =
                                "Something went wrong. Please try again later."
                        }
                    }
                } catch (e: Exception) {
                    e.printStackTrace()
                }
            }
        })
    }
}
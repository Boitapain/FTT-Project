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


class LoginActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)
    }

    fun submit(v: View?) {
        val usernameView = findViewById<EditText>(R.id.loginUsername)
        val passwordView = findViewById<EditText>(R.id.loginPassword)
        val username = usernameView.text.toString().trim { it <= ' ' }
        val password = passwordView.text.toString().trim { it <= ' ' }
        if (username.isEmpty() || password.isEmpty()) {
            Toast.makeText(
                applicationContext,
                "Something is wrong. Please check your inputs.",
                Toast.LENGTH_LONG
            ).show()
            return
        }
        val loginForm = JSONObject()
        try {
            loginForm.put("subject", "login")
            loginForm.put("email", username)
            loginForm.put("password", password)
        } catch (e: JSONException) {
            e.printStackTrace()
        }
        val body = RequestBody.create(
            MediaType.parse("application/json; charset=utf-8"),
            loginForm.toString()
        )
        postRequest(MainActivity.postUrl, body)
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
            override fun onFailure(call: Call, e: IOException) {
                // Cancel the post on failure.
                call.cancel()
                Log.d("FAIL", e.message!!)

                // In order to access the TextView inside the UI thread, the code is executed inside runOnUiThread()
                runOnUiThread {
                    val responseTextLogin = findViewById<TextView>(R.id.responseTextLogin)
                    responseTextLogin.text = "Failed to Connect to Server. Please Try Again."
                }
            }

            @Throws(IOException::class)
            override fun onResponse(call: Call, response: Response) {
                // In order to access the TextView inside the UI thread, the code is executed inside runOnUiThread()
                runOnUiThread {
                    val responseTextLogin = findViewById<TextView>(R.id.responseTextLogin)
                    try {
                        val loginResponseString = response.body()!!.string().trim { it <= ' ' }
                        Log.d(
                            "LOGIN",
                            "Response from the server : $loginResponseString"
                        )
                        if (loginResponseString == "successful") {
                            Log.d("LOGIN", "Successful Login")
                            finish() //finishing activity and return to the calling activity.
                        } else if (loginResponseString == "failure") {
                            responseTextLogin.text = "Login Failed. Invalid username or password."
                        }
                    } catch (e: Exception) {
                        e.printStackTrace()
                        responseTextLogin.text = "Something went wrong. Please try again later."
                    }
                }
            }
        })
    }
}
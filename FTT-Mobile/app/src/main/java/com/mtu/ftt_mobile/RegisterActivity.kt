package com.mtu.ftt_mobile

import android.content.Intent
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
        val usernameView = findViewById<EditText>(R.id.email)
        val firstNameView = findViewById<EditText>(R.id.firstName)
        val lastNameView = findViewById<EditText>(R.id.lastName)
        val passwordView = findViewById<EditText>(R.id.password)
        val financialView = findViewById<EditText>(R.id.financialInstitution)
        val username = usernameView.text.toString().trim { it <= ' ' }
        val firstName = firstNameView.text.toString().trim { it <= ' ' }
        val lastName = lastNameView.text.toString().trim { it <= ' ' }
        val password = passwordView.text.toString().trim { it <= ' ' }
        val financial = financialView.text.toString().trim { it <= ' ' }
        if (firstName.length == 0 || lastName.length == 0 || username.length == 0 || password.length == 0 || financial.length==0) {
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
                registrationForm.put("email", username)
                registrationForm.put("password", password)
                registrationForm.put("financial_inst", financial)
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
        val intent = android.content.Intent(this, GetBrokerPremium::class.java)
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
                        if (responseString == "successful") {
                            responseTextRegister.text = "Registration completed successfully."
                            startActivity(intent)
                            finish()
                        } else if (responseString == "failure") {
                            responseTextRegister.text =
                                "Something went wrong. Please try again later."
                        } else {
                            responseTextRegister.text =responseString

                        }
                    }
                } catch (e: Exception) {
                    e.printStackTrace()
                }
            }
        })
    }
}
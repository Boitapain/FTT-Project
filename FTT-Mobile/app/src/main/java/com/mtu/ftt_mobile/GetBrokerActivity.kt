package com.mtu.ftt_mobile

import android.graphics.Paint
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView
import okhttp3.*
import org.json.JSONException
import org.json.JSONObject
import java.io.IOException

class GetBrokerActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_get_broker)

        val buttonDismissBrokerPremium = findViewById<Button>(R.id.button_skip_broker_premium)
        buttonDismissBrokerPremium.paintFlags = Paint.UNDERLINE_TEXT_FLAG
    }
    fun getBroker(){
        val registrationForm = JSONObject()
        try {
            registrationForm.put("subject", "")
            registrationForm.put("table", "clients")

        } catch (e: JSONException) {
            e.printStackTrace()
        }
        val body = RequestBody.create(
            MediaType.parse("application/json; charset=utf-8"),
            registrationForm.toString()
        )
        postRequest(MainActivity.postUrl, body)
    }

    fun postRequest(postUrl: String?, postBody: RequestBody?) {
        val intent = android.content.Intent(this, GetBrokerActivity::class.java)
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
package com.mtu.ftt_mobile

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button

class GetBrokerPremium : AppCompatActivity(), View.OnClickListener{

    lateinit var dismiss: Button
    lateinit var getBroker: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_get_broker_premium)
    }

    override fun onClick(p0: View?) {
        if (p0 != null) {
            when(p0.id){
                R.id.dismissBtn -> startActivity(Intent(this, HomeActivity::class.java))
                R.id.getBrokerBtn -> startActivity(Intent(this, HomeActivity::class.java))
            }
        }
    }
}
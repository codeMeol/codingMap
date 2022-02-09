package com.example.practice

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView


import java.lang.Math.abs
import java.util.*

class MainActivity : AppCompatActivity() {
    var k=0
    var p_num=2;
    var point_list= mutableListOf<Float>()

    fun start(){
        setContentView(R.layout.activity_start)
        var btn_minus:Button=findViewById(R.id.btn_minus)
        var btn_plus:Button=findViewById(R.id.btn_plus)
        var btn_start:Button=findViewById(R.id.btn_start)
        var tv_pn: TextView=findViewById(R.id.tv_playernum)

        var i=tv_pn.text;

        btn_minus.setOnClickListener{
            if(p_num==0){
                p_num=1;
            }
            p_num--
            tv_pn.text=p_num.toString()
        }

        btn_plus.setOnClickListener{

            p_num++
            tv_pn.text=p_num.toString()
        }
        btn_start.setOnClickListener{
            main()
        }
    }
    fun main() {
        setContentView(R.layout.activity_main)
        val btn: Button = findViewById(R.id.btn_change)
        val tv: TextView = findViewById(R.id.tv_random)
        var tv_people:TextView= findViewById(R.id.tv_people)
        var timerTask: Timer? = null
        var sec: Int = 0;
        var state = 1

        val tv_timer: TextView = findViewById(R.id.tv_timer)
        val random = Random()

        val num = random.nextInt(1001)
        tv.text = (num.toFloat() / 100).toString()
        tv_people.text="참가자"+(k+1)
        btn.setOnClickListener {
            println(p_num)
            state++
            println(state)
            if (state==2) {
                timerTask = kotlin.concurrent.timer(period = 10) {
                    sec++
                    runOnUiThread {
                        tv_timer.text = (sec.toFloat() / 100).toString()
                        btn.text = "정지"
                    }


                }
          } else if(state==3) {
                btn.text="다음"
                timerTask?.cancel()
                var point = abs(sec - num).toFloat() / 100
                point_list.add(point)
                Toast.makeText(this@MainActivity, point.toString() + "입니다", Toast.LENGTH_SHORT)
                    .show()
                state=0

//            }
            }
            else if(state==1){
                if(k+1<p_num){
                    k++

                    main()
                }else{
                    println(point_list)
                    k=0;
                    point_list.clear()
                    myRecycler()

                }


            }

        }

    }
    fun myRecycler(){

        var dogList = arrayListOf<member>(
            member("안녕1", "안녕2", "안녕3")

        )
            setContentView(R.layout.activity_end)


        var mRecyclerView : RecyclerView=findViewById(R.id.mRecyclerView)
            val mAdapter = MainRvAdapter(this, dogList)
            mRecyclerView.adapter = mAdapter

            val lm = LinearLayoutManager(this)
            mRecyclerView.layoutManager = lm
            mRecyclerView.setHasFixedSize(true)

    }
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
           start()



            }
        }


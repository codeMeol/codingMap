package com.example.practice

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class MainRvAdapter (val context: Context, val dogList:ArrayList<member>)  :
        RecyclerView.Adapter<MainRvAdapter.Holder>(){


            inner class Holder(itemView: View): RecyclerView.ViewHolder(itemView) {
                var tv_player_name = itemView?.findViewById<TextView>(R.id.player_name)
                var tv_point = itemView?.findViewById<TextView>(R.id.tv_point)
                var tv_lanking = itemView?.findViewById<TextView>(R.id.tv_lanking)

                fun bind (member: member, context: Context) {
                    /* dogPhoto의 setImageResource에 들어갈 이미지의 id를 파일명(String)으로 찾고,
                    이미지가 없는 경우 안드로이드 기본 아이콘을 표시한다.*/

                    /* 나머지 TextView와 String 데이터를 연결한다. */
                    tv_player_name?.text = member.tv_userName
                    tv_lanking?.text = member.tv_lank
                    tv_point?.text = member.tv_point

                }
            }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): Holder {
            val view = LayoutInflater.from(context).inflate(R.layout.recyclerview_item,parent,false)
        return Holder(view)
    }

    override fun onBindViewHolder(holder: Holder, position: Int) {
        holder?.bind(dogList[position],context)
    }

    override fun getItemCount(): Int {
        return dogList.size
    }
}


package com.example.androistudiojavapractice;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.webkit.WebChromeClient;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.ArrayAdapter;

import android.widget.Toast;

import com.example.androistudiojavapractice.databinding.ActivityMainBinding;
import com.example.androistudiojavapractice.databinding.WebviewActivityBinding;


import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    private ActivityMainBinding binding;

    String shared="file";
    int i=1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityMainBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());
        binding.btnGosub.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast toast=Toast.makeText(MainActivity.this.getApplicationContext(),"hi",Toast.LENGTH_LONG);
                toast.show();
                Intent intent=new Intent(MainActivity.this,WebsiteActivity.class);
                startActivity(intent);
            }
        });
        SharedPreferences sharedPreferences= getSharedPreferences(shared,0);
        int editNum=sharedPreferences.getInt("listcount",i);
        Toast toast=Toast.makeText(this.getApplicationContext(),""+editNum,Toast.LENGTH_LONG);
        toast.show();
        List<String> data=new ArrayList<>();

        ArrayAdapter<String> adapter= new ArrayAdapter<>(this, android.R.layout.simple_list_item_1,data);
        binding.exlist.setAdapter(adapter);
        if(editNum!=1) {
            for(int count=1;count<=editNum;count++) {
                data.add("리스트 " + count);
                adapter.notifyDataSetChanged();
            }
            i=editNum;

        }
        else if(editNum==1)
        adapter.notifyDataSetChanged();

        binding.btnAddlist.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
            i+=1;
            data.add("리스트 "+i);
                adapter.notifyDataSetChanged();
            }
        });



    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        SharedPreferences sharedPreferences= getSharedPreferences(shared,0);
        SharedPreferences.Editor editor= sharedPreferences.edit();
        editor.putInt("listcount",i);
        editor.commit();


        
    }
}
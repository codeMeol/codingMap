package com.example.androistudiojavapractice;

import android.os.Bundle;
import android.view.KeyEvent;
import android.webkit.WebChromeClient;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import com.example.androistudiojavapractice.databinding.WebviewActivityBinding;

import androidx.appcompat.app.AppCompatActivity;

public class WebsiteActivity extends AppCompatActivity {

    private WebviewActivityBinding webviewActivityBinding;
    private String url="https://www.naver.com";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        webviewActivityBinding = WebviewActivityBinding.inflate(getLayoutInflater());
        setContentView(webviewActivityBinding.getRoot());
        webviewActivityBinding.webView.getSettings().setJavaScriptEnabled(true);
        webviewActivityBinding.webView.loadUrl(url);
        webviewActivityBinding.webView.setWebChromeClient(new WebChromeClient());
        webviewActivityBinding.webView.setWebViewClient(new WebViewClientClass());

    }

    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {

        if ((keyCode)==KeyEvent.KEYCODE_BACK && webviewActivityBinding.webView.canGoBack())
        {
            webviewActivityBinding.webView.goBack();

            return true;

        }
        return super.onKeyDown(keyCode, event);
    }

    private class WebViewClientClass extends WebViewClient {//현재페이지에 url을 불러오는 메소드
        @Override
        public boolean shouldOverrideUrlLoading(WebView view, String url) {
            view.loadUrl(url);
            return true;
        }
    }
}
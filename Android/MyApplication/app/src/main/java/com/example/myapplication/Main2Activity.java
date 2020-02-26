package com.example.myapplication;

import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class Main2Activity extends AppCompatActivity {
    // Alt+Enter : 자동 import
    // Alt+Insert : Generate

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.iot_test_2);

        WebView wv = findViewById(R.id.webview);

        WebSettings webSettings = wv.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webSettings.setSupportZoom(true);

        wv.setWebViewClient(new WebViewClient());

        wv.loadUrl("file:///android_asset/br.html");

        // wv.loadUrl("http://www.naver.com");

    }

}

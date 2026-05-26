from kivy.app import App
from jnius import autoclass

class DEEPAIApp(App):
    def build(self):
        Activity = autoclass('org.kivy.android.PythonActivity').mActivity
        WebView = autoclass('android.webkit.WebView')
        WebViewClient = autoclass('android.webkit.WebViewClient')
        
        webview = WebView(Activity)
        settings = webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setLoadWithOverviewMode(True)
        settings.setUseWideViewPort(True)
        
        webview.setWebViewClient(WebViewClient())
        
        # 🔗 Tumhara live server link jo app kholte hi chalega
        webview.loadUrl('https://unlovely-bankroll-jargon.ngrok-free.dev')
        
        Activity.setContentView(webview)
        return webview

if __name__ == '__main__':
    DEEPAIApp().run()

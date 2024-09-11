import streamlit as st
import pyshorteners

# URL을 줄이는 함수
def shorten_url(long_url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_url)

# Streamlit 앱 구성
st.title("URL Shortener App")

# 사용자 입력을 받음
long_url = st.text_input("Enter the URL you want to shorten:")

# 버튼 클릭 시 URL 단축
if st.button("Shorten URL"):
    if long_url:
        try:
            short_url = shorten_url(long_url)
            st.success(f"Shortened URL: {short_url}")
            st.markdown(f"[Open Shortened URL]({short_url})", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please enter a URL.")

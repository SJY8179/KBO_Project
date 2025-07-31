import streamlit as st

st.title("KBO 인사이트 2")
st.write("왼쪽 사이드바에서 페이지를 선택하세요.")

player = "김태군"
hit = 2
avg = 0.667

st.markdown(f"""
<div style=";padding:1rem;border-radius:1rem;">
    <h4>🏅 선수: <b>{player}</b></h4>
    <p>안타 수: {hit}</p>
    <p>타율: <b style='color:green;'>{avg:.3f}</b></p>
</div>
""", unsafe_allow_html=True)
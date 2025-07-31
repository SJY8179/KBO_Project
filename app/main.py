
import streamlit as st
import pandas as pd

st.title("KBO 인사이트 초기페이지")
st.write("야구 데이터를 시각화해봅시다!")

data = {
    "선수": ["이정후", "나성범", "최형우"],
    "타율": [0.342, 0.315, 0.288]
}
df = pd.DataFrame(data)

st.dataframe(df)

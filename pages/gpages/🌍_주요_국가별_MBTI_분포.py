import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="주요 국가별 MBTI 분포", page_icon="🌍", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #FAFAF7; }
    .pastel-card { background-color: #FFFFFF; border-radius: 16px; padding: 24px; }
</style>
""", unsafe_allow_html=True)

st.title("🌍 2. 주요 국가별 MBTI 분포 비교")

st.markdown('<div class="pastel-card">', unsafe_allow_html=True)
st.write("문화권별 E/I 비율 및 F/T 성향 차이를 비교해보세요.")

country_df = pd.DataFrame({
    '국가': ['대한민국 🇰🇷', '미국 🇺🇸', '일본 🇯🇵', '독일 🇩🇪'],
    '내향형(I) 비율': [51, 47, 58, 52],
    '외향형(E) 비율': [49, 53, 42, 48],
    '감정형(F) 비율': [67, 46, 52, 39],
    '사고형(T) 비율': [33, 54, 48, 61]
})

fig = px.bar(
    country_df, x='국가', y=['내향형(I) 비율', '외향형(E) 비율'],
    title="국가별 내향형(I) vs 외향형(E) 비율 비교",
    barmode='stack',
    color_discrete_sequence=['#A2D2FF', '#FFB7B2']
)
fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="대한민국 MBTI 인구 비율", page_icon="📊", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #FAFAF7; }
    .pastel-card { background-color: #FFFFFF; border-radius: 16px; padding: 24px; }
    .pastel-card-pink { background-color: #FFF5F5; border-left: 5px solid #FFB7B2; padding: 15px; border-radius: 8px; margin-bottom: 10px; }
    .pastel-card-blue { background-color: #F0F7FF; border-left: 5px solid #A2D2FF; padding: 15px; border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

KOREA_MBTI_DATA = pd.DataFrame({
    'MBTI': ['INFP', 'ENFP', 'ISFJ', 'ESFJ', 'ISFP', 'ESFP', 'INTP', 'INFJ', 
             'ENFJ', 'ENTP', 'ESTJ', 'ISTJ', 'INTJ', 'ISTP', 'ESTP', 'ENTJ'],
    'Ratio': [13.39, 12.60, 8.35, 8.20, 6.61, 6.36, 6.28, 6.25, 
              6.09, 5.04, 4.56, 4.28, 3.75, 3.11, 2.94, 2.73]
})

PASTEL_COLORS = [
    "#FFB7B2", "#FFDAC1", "#FFE5B4", "#FFF5BA", "#E2F0CB", 
    "#B5EAD7", "#C7CEEA", "#A2D2FF", "#BDB2FF", "#FFC6FF",
    "#D8BBFF", "#E8AEB7", "#B2F7EF", "#F7D6E0", "#F2C6DE", "#D0F4DE"
]

st.title("📊 1. 대한민국 MBTI 인구 비율 통계")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="pastel-card">', unsafe_allow_html=True)
    fig = px.bar(
        KOREA_MBTI_DATA, x='MBTI', y='Ratio', color='MBTI', text='Ratio',
        color_discrete_sequence=PASTEL_COLORS,
        labels={'Ratio': '비율 (%)'}
    )
    fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', showlegend=False, height=450)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="pastel-card">', unsafe_allow_html=True)
    st.markdown("### 📌 주요 특징")
    st.markdown("""
        <div class="pastel-card-pink">
            <b>🥇 1위: INFP (13.39%)</b><br>
            감수성이 풍부하고 독창적인 성향이 대한민국에서 가장 높게 나타납니다.
        </div>
        <div class="pastel-card-blue">
            <b>🥈 2위: ENFP (12.60%)</b><br>
            상상력이 풍부하고 사교적인 활동가 성향이 상위권입니다.
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
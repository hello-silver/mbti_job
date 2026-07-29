import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="대표 직업군 10선 MBTI 분포", page_icon="💼", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #FAFAF7; }
    .pastel-card { background-color: #FFFFFF; border-radius: 16px; padding: 24px; }
</style>
""", unsafe_allow_html=True)

JOB_MBTI = {
    "💻 IT & SW 개발자": {"ISTJ": 22, "INTP": 18, "INTJ": 15, "ISTP": 14, "기타": 31},
    "🩺 의료 & 보건 전문가": {"ISFJ": 28, "ISTJ": 20, "ENFJ": 14, "INFJ": 12, "기타": 26},
    "👩‍🏫 초·중고 교사": {"ENFJ": 25, "ESFJ": 22, "INFJ": 15, "ISFJ": 14, "기타": 24},
    "📈 경영 기획 & 전략": {"ENTJ": 26, "ESTJ": 22, "INTJ": 18, "ENTP": 14, "기타": 20},
    "🎨 디자이너 & 예술가": {"INFP": 26, "ISFP": 24, "ENFP": 20, "INTP": 12, "기타": 18},
    "📢 마케팅 & 홍보": {"ENFP": 28, "ENTP": 22, "ESFP": 18, "ENFJ": 14, "기타": 18},
    "⚖️ 법률 & 공무원": {"ISTJ": 32, "ESTJ": 25, "INTJ": 14, "ISFJ": 12, "기타": 17},
    "🔬 연구원 & 과학자": {"INTP": 30, "INTJ": 25, "ISTJ": 16, "ISTP": 12, "기타": 17},
    "💰 금융 & 회계 전문가": {"ISTJ": 35, "ESTJ": 22, "INTJ": 15, "ENTJ": 12, "기타": 16},
    "✈️ 서비스 & 항공": {"ESFP": 28, "ESFJ": 25, "ESTP": 20, "ISFP": 14, "기타": 13}
}

PASTEL_COLORS = ["#FFB7B2", "#FFDAC1", "#FFE5B4", "#B5EAD7", "#C7CEEA"]

st.title("💼 3. 대한민국 대표 직업군 10선 MBTI 분포")

st.markdown('<div class="pastel-card">', unsafe_allow_html=True)
selected_job = st.selectbox("👉 직업군 선택:", list(JOB_MBTI.keys()))

job_data = JOB_MBTI[selected_job]
df = pd.DataFrame({'MBTI': list(job_data.keys()), '비율': list(job_data.values())})

fig = px.pie(df, names='MBTI', values='비율', hole=0.4, color_discrete_sequence=PASTEL_COLORS)
fig.update_traces(textinfo='percent+label')
fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')

st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
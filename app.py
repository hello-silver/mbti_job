import streamlit as st

# ==========================================
# 1. 페이지 전체 기본 설정
# ==========================================
st.set_page_config(
    page_title="🌱 청소년 MBTI 진로 탐구 센터",
    page_icon="🌱",
    layout="wide"
)

# ==========================================
# 2. 파스텔 톤 커스텀 CSS
# ==========================================
PASTEL_CSS = """
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    html, body, [class*="css"] {
        font-family: 'Pretendard', sans-serif;
        color: #4A4A4A;
    }
    .stApp { background-color: #FAFAF7; }
    .header-banner {
        background: linear-gradient(135deg, #FFDAC1 0%, #E2F0CB 50%, #B5EAD7 100%);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .pastel-card { background-color: #FFFFFF; border-radius: 16px; padding: 24px; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03); }
    .pastel-card-pink { background-color: #FFF5F5; border-left: 5px solid #FFB7B2; border-radius: 12px; padding: 18px; margin-bottom: 12px; }
    .pastel-card-blue { background-color: #F0F7FF; border-left: 5px solid #A2D2FF; border-radius: 12px; padding: 18px; margin-bottom: 12px; }
    .pastel-card-green { background-color: #F2F9F1; border-left: 5px solid #B5EAD7; border-radius: 12px; padding: 18px; margin-bottom: 12px; }
    .pastel-card-yellow { background-color: #FFFDEE; border-left: 5px solid #FFE5B4; border-radius: 20px; padding: 20px; }
</style>
"""
st.markdown(PASTEL_CSS, unsafe_allow_html=True)

# ==========================================
# 3. MBTI 진로 추천 데이터
# ==========================================
MBTI_CAREER_DATA = {
    "INFP": {
        "title": "열정적인 중재자 🦄",
        "jobs": [
            {"title": "🎨 크리에이티브 콘텐츠 작가 / 웹툰 스토리작가", "desc": "감수성과 상상력을 글로 풀어내어 사람들에게 감동과 힐링을 주는 직업입니다."},
            {"title": "🌱 청소년 심리상담사", "desc": "타인의 아픔에 공감하고 조용히 들어주는 능력을 발휘하여 고민을 나눕니다."},
            {"title": "🌿 친환경 사회적기업 기획자", "desc": "가치관을 살려 더 나은 사회와 환경을 만드는 프로젝트를 기획합니다."}
        ],
        "advice": "내면 세계가 깊고 아름다운 친구군요! 남들과 비교하기보다는 나만의 속도와 가치를 찾아갈 때 가장 빛납니다.",
        "skills": ["창의적 글쓰기", "공감 및 경청 능력", "가치 중심의 기획력"]
    },
    "ENFP": {
        "title": "재기발랄한 활동가 🎈",
        "jobs": [
            {"title": "🚀 미디어 크리에이터 & PD", "desc": "풍부한 아이디어와 열정으로 즐거움을 주는 콘텐츠를 만들고 소통합니다."},
            {"title": "📢 브랜드 마케팅 기획자", "desc": "트렌드를 읽고 창의적인 카피와 이벤트를 기획하여 마케팅을 전개합니다."},
            {"title": "🤝 이벤트 & 페스티벌 디렉터", "desc": "에너지 넘치는 분위기 속에서 새로운 사람들과 협업하고 행사를 만듭니다."}
        ],
        "advice": "아이디어가 넘치는 당신! 호기심이 넓은 만큼, 한 가지 목표를 정해 끝까지 마무리해보는 경험을 쌓아보세요.",
        "skills": ["창의적 아이디어 도출", "트렌드 감각", "뛰어난 친화력"]
    },
    "INFJ": {
        "title": "선의의 옹호자 🔮",
        "jobs": [
            {"title": "📚 인문학 연구원 & 칼럼니스트", "desc": "깊은 통찰력을 바탕으로 본질적인 메시지를 사회에 전달합니다."},
            {"title": "⚖️ 인권 및 공익 전문 변호사", "desc": "자신의 신념과 정의감을 바탕으로 소외된 이들의 목소리를 대변합니다."},
            {"title": "🧠 UX Research & 심리 분석가", "desc": "사용자의 직관적 심리를 이해하여 더 나은 경험을 디자인합니다."}
        ],
        "advice": "세상을 더 따뜻하게 바꾸고자 하는 친구군요! 남을 돕는 것도 좋지만, 스스로의 마음 상태를 먼저 돌보세요.",
        "skills": ["통찰력 있는 분석", "장기적 비전 설계", "진정성 있는 소통"]
    },
    "ENFJ": {
        "title": "정의로운 사회운동가 🌟",
        "jobs": [
            {"title": "👨‍🏫 진로진학 교사 & 교육 코치", "desc": "학생들의 잠재력을 발견하고 꿈을 향해 나아갈 수 있도록 이끌어줍니다."},
            {"title": "🏛️ CSR(기업 사회공헌) 매니저", "desc": "기업이 사회에 선한 영향력을 끼칠 수 있도록 공익 사업을 총괄합니다."},
            {"title": "🎙️ 아나운서 및 커뮤니케이터", "desc": "공감대 형성 능력과 설득력 있는 말하기로 메시지를 전달합니다."}
        ],
        "advice": "리더십이 뛰어난 당신! 다른 사람의 평가에 연연해하지 말고, 본인의 목소리에도 귀를 기울여주세요.",
        "skills": ["리더십 및 동기부여", "명확한 의사소통", "조직 관리 능력"]
    },
    "INTJ": {
        "title": "용의주도한 전략가 ♟️",
        "jobs": [
            {"title": "💻 AI 시스템 아키텍트", "desc": "복잡한 데이터 구조에서 패턴을 찾고 기술 시스템을 설계합니다."},
            {"title": "📈 경영컨설턴트 & 전략기획자", "desc": "문제점을 정확히 진단하고 장기적인 성장 전략 솔루션을 제안합니다."},
            {"title": "🧬 바이오 융합 연구원", "desc": "체계적이고 논리적인 탐구를 통해 미래 신기술 분야를 연구합니다."}
        ],
        "advice": "논리력을 바탕으로 문제를 해결하는 전략가입니다! 함께하는 동료들의 감정도 고려하면 완벽해집니다.",
        "skills": ["논리적 구조화", "장기적 전략 수립", "비판적 사고력"]
    },
    "ENTJ": {
        "title": "대담한 통솔자 🎯",
        "jobs": [
            {"title": "💼 스타트업 대표(CEO)", "desc": "비전을 설정하고 추진력 있게 팀을 끌어나가 새로운 가치를 창출합니다."},
            {"title": "📊 글로벌 펀드매니저", "desc": "시장 동향을 분석하여 과감하고 결단력 있는 투자 의사결정을 내립니다."},
            {"title": "🏗️ 프로젝트 총괄 매니저(PM)", "desc": "목표 달성을 위해 자원을 효율적으로 배분하고 현장을 리드합니다."}
        ],
        "advice": "목표를 향해 나아가는 당당함이 멋집니다! 팀원들의 정성 어린 피드백을 귀담아듣는 여유를 가져보세요.",
        "skills": ["강력한 추진력", "의사결정력", "자원 배분 및 관리"]
    },
    "INTP": {
        "title": "논리적인 사색가 🧠",
        "jobs": [
            {"title": "🤖 알고리즘 & AI 개발자", "desc": "복잡한 논리적 문제를 탐구하고 효율적인 시스템을 개발합니다."},
            {"title": "🔬 기초과학 연구원", "desc": "세상의 작동 원리와 호기심이 드는 원리를 파고들어 깊이 연구합니다."},
            {"title": "🎮 게임 시스템 기획자", "desc": "게임 내 치밀한 규칙과 밸런스, 메커니즘을 창의적으로 설계합니다."}
        ],
        "advice": "지적으로 탐구하는 멋진 지성인입니다! 머릿속 훌륭한 아이디어를 행동으로 직접 실행해보는 습관을 들여보세요.",
        "skills": ["원리 탐구 및 문제해결", "알고리즘적 사고", "객관적 분석"]
    },
    "ENTP": {
        "title": "뜨거운 논쟁을 즐기는 변론가 💡",
        "jobs": [
            {"title": "💡 신사업 기획자", "desc": "기존 틀을 깨는 혁신적인 아이디어로 새로운 비즈니스 모델을 발굴합니다."},
            {"title": "⚖️ 지식재산권 변리사", "desc": "새로운 기술의 논리성을 입증하고 지적 재산을 보호 및 변호합니다."},
            {"title": "📢 벤처투자자(VC) 심사역", "desc": "시장 유행 변화를 감지하고 유망한 새 기업을 발굴합니다."}
        ],
        "advice": "독창적인 시각이 큰 장점입니다! 아이디어를 내는 것에서 나아가 차근차근 디테일을 챙겨 실현해보세요.",
        "skills": ["창의적 문제 재해석", "논리적 설득력", "변화 적응력"]
    },
    "ISTJ": {
        "title": "청렴결백한 논리주의자 📐",
        "jobs": [
            {"title": "📑 공인회계사(CPA)", "desc": "정확한 수치 계산과 법적 기준을 바탕으로 재무 안전성을 책임집니다."},
            {"title": "🏛️ 공공기관 행정 전문가", "desc": "원칙과 절차를 지키며 사회 안정을 뒷받침하는 질서 있는 업무를 수행합니다."},
            {"title": "🔒 정보보안 감리사", "desc": "시스템 허점을 철저히 점검하고 규정에 따라 안전하게 보완합니다."}
        ],
        "advice": "성실하여 신뢰받는 버팀목입니다! 때로는 예상치 못한 변화나 새로운 시도에도 마음을 열어보세요.",
        "skills": ["체계적 일처리", "정확성과 꼼꼼함", "높은 책임감"]
    },
    "ESTJ": {
        "title": "엄격한 관리자 👔",
        "jobs": [
            {"title": "🏢 기업 인사 및 조직 관리자", "desc": "체계적인 규칙을 세우고 직원들의 업무 효율성을 명확히 관리합니다."},
            {"title": "✈️ 항공운항관리사", "desc": "복잡한 현장 스케줄을 원칙에 따라 정확하게 제어하고 총괄합니다."},
            {"title": "🏛️ 행정고시 사무관", "desc": "국가 정책을 체계적으로 수립하고 질서 있게 현장에 적용합니다."}
        ],
        "advice": "실행력이 뛰어난 리더입니다! 원칙도 중요하지만, 구성원들의 사정을 감싸주는 따뜻함을 더해보세요.",
        "skills": ["조직 및 목표 관리", "현실적 실행력", "규칙 및 체계 구축"]
    },
    "ISFJ": {
        "title": "용감한 수호자 🛡️",
        "jobs": [
            {"title": "🏥 전문 간호사", "desc": "세심하고 따뜻한 손길로 환자의 상태를 철저히 관리하고 케어합니다."},
            {"title": "🏫 초등교사 & 아동발달 전문가", "desc": "아이들의 성장 과정을 지원하며 안전하고 따뜻한 환경을 만듭니다."},
            {"title": "📦 박물관 학예사(큐레이터)", "desc": "소중한 문화유산과 기록물을 꼼꼼히 보존하고 알기 쉽게 관리합니다."}
        ],
        "advice": "따뜻한 수호자입니다! 남을 돕느라 정작 본인의 피로를 참지 말고, 거절하는 연습과 휴식도 챙기세요.",
        "skills": ["세심한 케어 및 배려", "꼼꼼한 기록 관리", "성실한 지속성"]
    },
    "ESFJ": {
        "title": "사교적인 외교관 🤝",
        "jobs": [
            {"title": "🤝 VIP 고객관계 관리자(CRM)", "desc": "공감 능력과 친절로 친밀한 관계를 유지하고 해결책을 줍니다."},
            {"title": "🩺 병원 코디네이터", "desc": "따뜻한 소통으로 방문객에게 최고의 서비스 경험을 제공합니다."},
            {"title": "🎈 아동 복지 전문가", "desc": "따뜻한 공동체 분위기를 조성하며 아이들의 행복한 성장을 돕습니다."}
        ],
        "advice": "소통의 달인입니다! 타인의 인정에 지나치게 의존하기보다 스스로에 대한 자존감을 채워나가세요.",
        "skills": ["친화력 및 소통", "관계 형성 능력", "협동심 및 서비스 정신"]
    },
    "ISTP": {
        "title": "만능 재주꾼 🛠️",
        "jobs": [
            {"title": "🛠️ 로봇 및 기계 엔지니어", "desc": "장비의 정밀 정비, 작동 원리를 파악하고 구조를 구축합니다."},
            {"title": "🏎️ 자동차 튜닝 테크니션", "desc": "현장에서 즉각적인 문제점을 발견하고 손재주를 발휘해 해결합니다."},
            {"title": "🕵️ 데이터 포렌식 수사관", "desc": "객관적이고 차분한 시각으로 디테일한 증거를 정밀하게 분석합니다."}
        ],
        "advice": "차분한 실용주의자입니다! 본인의 생각과 감정을 주변 사람들에게 조금 더 나누어주면 더욱 좋습니다.",
        "skills": ["도구 및 기계 활용", "위기 대응력", "객관적 상황 판단"]
    },
    "ESTP": {
        "title": "수완 좋은 활동가 ⚡",
        "jobs": [
            {"title": "🚑 응급구조사 & 소방관", "desc": "긴박한 현장에서 순발력과 민첩성을 발휘해 생명을 구합니다."},
            {"title": "⚽ 스포츠 에이전트 & 트레이너", "desc": "역동적인 현장에서 선수 기량을 끌어올리고 비즈니스를 협상합니다."},
            {"title": "🏬 유통 현장 MD", "desc": "빠르게 변하는 현장 흐름에 발맞추어 즉각적인 행동으로 성과를 만듭니다."}
        ],
        "advice": "넘치는 에너지를 가진 친구! 행동에 옮기기 전, 장기적인 영향을 생각해보는 신중함을 갖춰보세요.",
        "skills": ["순발력 및 순발대응", "현장 행동력", "설득력 있는 협상"]
    },
    "ISFP": {
        "title": "호기심 많은 예술가 🎨",
        "jobs": [
            {"title": "🎨 패션 디자이너", "desc": "시각적인 아름다움과 개성을 직관적으로 표현하여 멋진 스타일을 만듭니다."},
            {"title": "🌸 플로리스트 & 공간 디렉터", "desc": "자연의 요소와 감성을 담아 따뜻하고 세련된 분위기를 연출합니다."},
            {"title": "📸 감성 사진작가", "desc": "순간의 감정과 조화로운 아름다움을 세심하게 포착해 담아냅니다."}
        ],
        "advice": "예술적 감성을 품고 있군요! 자신의 훌륭한 작품과 감성을 세상에 표현하는 자신감을 더해보세요.",
        "skills": ["미적 감각 및 심미안", "섬세한 감성 표현", "유연한 조화로움"]
    },
    "ESFP": {
        "title": "자유로운 영혼의 연예인 🌟",
        "jobs": [
            {"title": "🎭 뮤지컬 배우 & 공연 예술가", "desc": "무대 위에서 에너지와 감정을 마음껏 펼치며 관객들과 호흡합니다."},
            {"title": "✈️ 항공 승무원", "desc": "새로운 환경에서 다양한 사람들에게 감동적인 순간을 선사합니다."},
            {"title": "🎉 이벤트 MC", "desc": "현장 분위기를 한순간에 활기차고 밝게 만드는 친화력을 발휘합니다."}
        ],
        "advice": "주변을 환하게 밝히는 긍정주의자! 순간을 누리는 것 외에도 장기적인 계획을 꾸준히 이어나가 보세요.",
        "skills": ["무대 적응력 및 표현력", "주변 매력 발산", "현장 분위기 리드"]
    }
}

# ==========================================
# 4. 메인 화면 레이아웃
# ==========================================
st.markdown("""
    <div class="header-banner">
        <h1>🌱 청소년 맞춤 MBTI 진로 추천 센터</h1>
        <p>자신의 MBTI를 선택하고 나에게 꼭 맞는 대표 직업 3가지와 상담사의 따뜻한 한마디를 받아보세요 👋</p>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="pastel-card">', unsafe_allow_html=True)
    selected_mbti = st.selectbox("👉 MBTI 유형 선택:", list(MBTI_CAREER_DATA.keys()), index=0)
    info = MBTI_CAREER_DATA[selected_mbti]
    st.subheader(info['title'])
    st.markdown("#### 💡 대표 핵심 역량")
    for skill in info['skills']:
        st.write(f"• **{skill}**")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="pastel-card">', unsafe_allow_html=True)
    st.markdown(f"### 🌟 [{selected_mbti}] 추천 대표 직업 3선")
    cards = ["pastel-card-pink", "pastel-card-blue", "pastel-card-green"]
    for idx, job in enumerate(info['jobs']):
        st.markdown(f"""
            <div class="{cards[idx]}">
                <h4 style="margin:0;">{job['title']}</h4>
                <p style="margin:5px 0 0 0; color:#555;">{job['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(f"""
    <div class="pastel-card-yellow">
        <h4 style="margin:0; color:#D97706;">💬 전문상담사의 한마디</h4>
        <p style="margin-top:5px; font-size:16px;">"{info['advice']}"</p>
    </div>
""", unsafe_allow_html=True)

st.info("💡 **안내**: 왼쪽 사이드바 메뉴에서 다양한 MBTI 통계 차트를 살펴보실 수 있습니다!")

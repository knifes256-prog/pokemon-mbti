import os
import random
 
import streamlit as st
 
st.set_page_config(page_title="MBTI로 포켓몬 찾기", page_icon="🌟", layout="centered")
 
# ------------------------------------------------------------
# 이미지 설정
#  1) main.py와 같은 위치의 images 폴더에 파일을 넣으면 그 사진을 써요.
#  2) 또는 아래 IMAGE_URLS에 이미지 주소를 직접 붙여 넣어도 돼요.
#     예) IMAGE_URLS = {"피카츄": "https://.../pikachu.png"}
#  3) 둘 다 없으면 큰 이모지가 대신 보여요.
# ------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "images")
IMAGE_URLS = {}
 
GROUPS = [
    ("💜 분석가형 · 생각이 깊은 전략가들", ["INTJ", "INTP", "ENTJ", "ENTP"]),
    ("💚 외교관형 · 마음이 따뜻한 이상가들", ["INFJ", "INFP", "ENFJ", "ENFP"]),
    ("💙 관리자형 · 믿음직한 현실파들", ["ISTJ", "ISFJ", "ESTJ", "ESFJ"]),
    ("🧡 탐험가형 · 자유로운 행동파들", ["ISTP", "ISFP", "ESTP", "ESFP"]),
]
 
TYPE_COLORS = {
    "노말": "#A8A878", "불꽃": "#F08030", "물": "#6890F0", "전기": "#F8D030",
    "풀": "#78C850", "얼음": "#98D8D8", "격투": "#C03028", "독": "#A040A0",
    "땅": "#E0C068", "비행": "#A890F0", "에스퍼": "#F85888", "악": "#705848",
    "강철": "#B8B8D0", "드래곤": "#7038F8", "페어리": "#EE99AC",
}
DARK_TEXT_TYPES = {"전기", "얼음", "땅", "강철", "페어리", "노말"}
 
POKEMON = {
    "INTJ": dict(ko="뮤츠", en="Mewtwo", emoji="🧠", file="mewtwo.png", types=["에스퍼"],
        feature="유전자 조작으로 태어난 전설의 포켓몬으로, 엄청난 초능력을 지녔어요.",
        why=["늘 몇 수 앞을 내다보는 전략가예요.", "강한 힘을 가졌지만 쉽게 속마음을 드러내지 않아요.", "혼자서도 목표를 끝까지 해내는 점이 닮았어요."]),
    "INTP": dict(ko="후딘", en="Alakazam", emoji="🌀", file="alakazam.png", types=["에스퍼"],
        feature="아주 뛰어난 두뇌를 가졌고, 숟가락으로 초능력을 더 크게 키워요.",
        why=["엄청난 두뇌로 생각에 푹 빠지는 탐구가예요.", "궁금한 것은 끝까지 파고드는 호기심이 대단해요.", "조용하지만 머릿속은 늘 바쁜 점이 닮았어요."]),
    "ENTJ": dict(ko="리자몽", en="Charizard", emoji="🐉", file="charizard.png", types=["불꽃", "비행"],
        feature="커다란 날개로 하늘을 날고, 꼬리 끝의 불꽃으로 힘차게 싸워요.",
        why=["당당하게 앞장서는 타고난 리더예요.", "목표를 향해 불꽃처럼 힘차게 나아가요.", "사람들을 이끄는 카리스마가 닮았어요."]),
    "ENTP": dict(ko="개굴닌자", en="Greninja", emoji="🥷", file="greninja.png", types=["물", "악"],
        feature="물을 수리검처럼 만들어 던지는 재빠른 닌자 같은 포켓몬이에요.",
        why=["재치 있고 재빨라서 어디서든 방법을 찾아내요.", "새로운 아이디어로 상대를 깜짝 놀라게 해요.", "변화를 즐기고 도전을 좋아하는 점이 닮았어요."]),
    "INFJ": dict(ko="네이티오", en="Xatu", emoji="🦚", file="xatu.png", types=["에스퍼", "비행"],
        feature="한 곳을 가만히 바라보며 과거와 미래를 본다고 전해져요.",
        why=["멀리 미래를 내다보는 신비로운 눈을 가졌어요.", "말수는 적지만 마음속 깊은 생각이 있어요.", "다른 사람의 마음을 잘 헤아리는 점이 닮았어요."]),
    "INFP": dict(ko="이브이", en="Eevee", emoji="🐾", file="eevee.png", types=["노말"],
        feature="환경에 따라 여러 모습으로 진화할 수 있는 가능성 많은 포켓몬이에요.",
        why=["여러 모습으로 변할 수 있는 가능성을 품고 있어요.", "순수하고 따뜻한 마음을 가졌어요.", "자신만의 세계와 꿈을 소중히 하는 점이 닮았어요."]),
    "ENFJ": dict(ko="루카리오", en="Lucario", emoji="🐺", file="lucario.png", types=["격투", "강철"],
        feature="상대의 감정을 파동으로 느낄 수 있는 의리 있는 포켓몬이에요.",
        why=["상대의 마음을 파동으로 느끼는 따뜻한 리더예요.", "친구가 힘들 때 가장 먼저 곁을 지켜줘요.", "정의감과 배려심이 닮았어요."]),
    "ENFP": dict(ko="피카츄", en="Pikachu", emoji="🐭", file="pikachu.png", types=["전기"],
        feature="양쪽 볼에 전기를 모아 두었다가 힘차게 내보내요.",
        why=["어디서든 분위기를 환하게 밝히는 에너자이저예요.", "사람들과 금방 친해지는 매력이 있어요.", "호기심 가득, 늘 활기찬 점이 닮았어요."]),
    "ISTJ": dict(ko="거북왕", en="Blastoise", emoji="🛡️", file="blastoise.png", types=["물"],
        feature="등의 대포에서 강력한 물줄기를 쏘고, 단단한 껍질로 몸을 지켜요.",
        why=["단단한 등껍질처럼 믿음직하고 책임감이 강해요.", "맡은 일은 묵묵히 끝까지 해내요.", "규칙과 약속을 소중히 여기는 점이 닮았어요."]),
    "ISFJ": dict(ko="해피너스", en="Blissey", emoji="🩷", file="blissey.png", types=["노말"],
        feature="다친 사람에게 품고 있는 알을 나눠 주며 기운을 북돋아 줘요.",
        why=["아픈 친구를 정성껏 돌봐주는 다정한 보살핌꾼이에요.", "남을 먼저 챙기는 따뜻한 마음을 가졌어요.", "조용히 곁에서 힘이 되어주는 점이 닮았어요."]),
    "ESTJ": dict(ko="윈디", en="Arcanine", emoji="🦮", file="arcanine.png", types=["불꽃"],
        feature="아주 빠르게 달리며, 예로부터 용맹하고 충성스럽다고 알려졌어요.",
        why=["의리 있고 믿음직한 든든한 지킴이예요.", "질서와 규칙을 지키며 무리를 이끌어요.", "책임감 있게 앞장서는 점이 닮았어요."]),
    "ESFJ": dict(ko="라프라스", en="Lapras", emoji="🌊", file="lapras.png", types=["물", "얼음"],
        feature="사람을 등에 태우고 바다를 건너 주는 온순한 포켓몬이에요.",
        why=["친구들을 등에 태우고 안전하게 데려다주는 다정한 포켓몬이에요.", "다른 사람을 챙기며 기뻐하는 마음이 커요.", "모두가 어울리게 돕는 점이 닮았어요."]),
    "ISTP": dict(ko="한카리아스", en="Garchomp", emoji="🦖", file="garchomp.png", types=["드래곤", "땅"],
        feature="제트기처럼 빠르게 날아다니고, 날카로운 지느러미로 싸워요.",
        why=["말없이 빠르고 정확하게 움직이는 실력자예요.", "필요한 순간에 번개처럼 해결해요.", "혼자서도 척척 해내는 점이 닮았어요."]),
    "ISFP": dict(ko="이상해꽃", en="Venusaur", emoji="🌺", file="venusaur.png", types=["풀", "독"],
        feature="등의 커다란 꽃에서 좋은 향기가 나고, 햇빛을 받으며 힘을 얻어요.",
        why=["등에 핀 꽃처럼 조용하고 아름다운 감성을 가졌어요.", "자연과 평화로운 시간을 좋아해요.", "부드럽지만 마음이 단단한 점이 닮았어요."]),
    "ESTP": dict(ko="번치코", en="Blaziken", emoji="🥊", file="blaziken.png", types=["불꽃", "격투"],
        feature="강력한 발차기와 불꽃으로 싸우는 격투 달인이에요.",
        why=["생각보다 먼저 몸이 움직이는 행동파예요.", "위기에도 겁내지 않고 시원하게 맞서요.", "지금 이 순간을 즐기는 점이 닮았어요."]),
    "ESFP": dict(ko="푸린", en="Jigglypuff", emoji="🎈", file="jigglypuff.png", types=["노말", "페어리"],
        feature="노래로 상대를 스르르 잠들게 하는 포켓몬이에요.",
        why=["노래로 모두를 즐겁게 만드는 분위기 메이커예요.", "어디서든 주목받는 사랑스러운 매력이 있어요.", "함께 있으면 파티가 되는 점이 닮았어요."]),
}
 
CONFETTI_COLORS = ["#F5C842", "#FF8FA3", "#7FD1A8", "#86B8E8", "#B39DDB", "#F09A3E", "#FFF3B0"]
 
CSS = """
<style>
  .stApp { background: #FFF6DC; }
  .block-container { max-width: 760px; padding-top: 2rem; }
  html, body, .stApp, .stMarkdown, p, li, span, div { color: #5A4630; }
  .main-title { text-align: center; font-size: 2.3rem; font-weight: 800; color: #C98A00 !important; margin: 0; }
  .sub-title { text-align: center; font-size: 1.2rem; margin: 6px 0 24px; }
  .group-title { font-size: 1.2rem; font-weight: 800; color: #8A5A00 !important; margin: 18px 0 6px; }
  div.stButton > button {
    width: 100%; padding: 14px 6px; border: 3px solid #F5C842; border-radius: 16px;
    background: #FFFDF5; color: #7A5200; transition: transform .12s, background .12s;
  }
  div.stButton > button p { font-size: 1.35rem; font-weight: 800; color: #7A5200 !important; }
  div.stButton > button:hover { background: #FFE58A; border-color: #F5A800; transform: translateY(-3px); }
  .card { background: #FFFDF5; border: 4px solid #F5C842; border-radius: 28px; padding: 26px 22px;
          text-align: center; box-shadow: 0 8px 0 #EBC55A; animation: pop .5s ease; }
  .badge { display: inline-block; background: #F5A800; color: #fff !important; font-weight: 800;
           padding: 4px 20px; border-radius: 999px; font-size: 1.2rem; }
  .big-emoji { font-size: 8rem; line-height: 1.15; animation: bob 2.4s ease-in-out infinite; }
  .pk-name { font-size: 2.4rem; font-weight: 800; color: #C98A00 !important; margin: 6px 0 2px; }
  .pk-en { font-size: 1.3rem; margin-bottom: 12px; }
  .chip { display: inline-block; padding: 4px 16px; margin: 0 4px; border-radius: 999px;
          font-weight: 800; font-size: 1.1rem; color: #fff !important; }
  .feature { background: #FFEBA8; border-radius: 18px; padding: 14px 18px; margin: 16px 0; font-size: 1.2rem; }
  .reason { text-align: left; background: #FFF1C4; border-radius: 18px; padding: 14px 20px; font-size: 1.15rem; }
  .reason p { margin: 6px 0; }
  .label { font-weight: 800; color: #A56A00 !important; }
  .confetti-wrap span { position: fixed; top: -20px; width: 10px; height: 14px; z-index: 9999;
                        pointer-events: none; animation: fall linear forwards; }
  @keyframes pop { from { transform: scale(.88); opacity: 0; } to { transform: scale(1); opacity: 1; } }
  @keyframes bob { 50% { transform: translateY(-8px); } }
  @keyframes fall { to { transform: translateY(110vh) rotate(720deg); } }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important; } .confetti-wrap { display: none; } }
</style>
"""
 
st.markdown(CSS, unsafe_allow_html=True)
 
if "mbti" not in st.session_state:
    st.session_state.mbti = None
if "celebrate" not in st.session_state:
    st.session_state.celebrate = False
 
 
def pick(mbti_type):
    st.session_state.mbti = mbti_type
    st.session_state.celebrate = True
 
 
def reset():
    st.session_state.mbti = None
    st.session_state.celebrate = False
 
 
def find_image(p):
    path = os.path.join(IMAGE_DIR, p["file"])
    if os.path.exists(path):
        return path
    return IMAGE_URLS.get(p["ko"])
 
 
def confetti_html():
    spans = []
    for _ in range(40):
        spans.append(
            '<span style="left:%dvw;background:%s;animation-duration:%.2fs;animation-delay:%.2fs;'
            'border-radius:%s"></span>'
            % (random.randint(0, 100), random.choice(CONFETTI_COLORS),
               2.2 + random.random() * 2.2, random.random() * 1.2,
               random.choice(["2px", "50%"]))
        )
    return '<div class="confetti-wrap">' + "".join(spans) + "</div>"
 
 
def type_chips(types):
    chips = []
    for t in types:
        color = TYPE_COLORS.get(t, "#A8A878")
        text = "#4A3A00" if t in DARK_TEXT_TYPES else "#fff"
        chips.append('<span class="chip" style="background:%s;color:%s !important">%s</span>' % (color, text, t))
    return "".join(chips)
 
 
# ------------------------------------------------------------
# 화면 1: MBTI 고르기
# ------------------------------------------------------------
if st.session_state.mbti is None:
    st.markdown('<div class="main-title">🌟 MBTI로 포켓몬 찾기 🌟</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">내 MBTI 유형을 눌러보세요.<br>나와 어울리는 단짝 포켓몬을 찾아드릴게요!</div>',
                unsafe_allow_html=True)
    for title, types in GROUPS:
        st.markdown('<div class="group-title">%s</div>' % title, unsafe_allow_html=True)
        cols = st.columns(4)
        for col, t in zip(cols, types):
            with col:
                st.button(t, key="btn_" + t, on_click=pick, args=(t,))
 
# ------------------------------------------------------------
# 화면 2: 결과
# ------------------------------------------------------------
else:
    t = st.session_state.mbti
    p = POKEMON[t]
 
    if st.session_state.celebrate:
        st.markdown(confetti_html(), unsafe_allow_html=True)
        st.balloons()
        st.session_state.celebrate = False
 
    st.markdown('<div class="main-title">🎉 단짝 포켓몬을 찾았어요! 🎉</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title"><span class="badge">%s</span> 유형의 단짝은...</div>' % t,
                unsafe_allow_html=True)
 
    st.markdown('<div class="card">', unsafe_allow_html=True)
 
    img = find_image(p)
    shown = False
    if img:
        left, mid, right = st.columns([1, 2, 1])
        with mid:
            try:
                st.image(img, width=300)
                shown = True
            except Exception:
                shown = False
    if not shown:
        st.markdown('<div class="big-emoji">%s</div>' % p["emoji"], unsafe_allow_html=True)
 
    st.markdown('<div class="pk-name">%s</div><div class="pk-en">(%s)</div>' % (p["ko"], p["en"]),
                unsafe_allow_html=True)
    st.markdown('<div><span class="label">타입</span>&nbsp; %s</div>' % type_chips(p["types"]),
                unsafe_allow_html=True)
    st.markdown('<div class="feature"><span class="label">특징</span><br>%s</div>' % p["feature"],
                unsafe_allow_html=True)
    lines = "".join("<p>✔ %s</p>" % line for line in p["why"])
    st.markdown('<div class="reason"><span class="label">어울리는 이유</span>%s</div>' % lines,
                unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
 
    st.write("")
    st.button("🔄 다시 고르기", key="reset", on_click=reset)

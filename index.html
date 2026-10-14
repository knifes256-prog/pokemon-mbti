<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MBTI로 포켓몬 찾기</title>
<style>
  * { box-sizing: border-box; }
  body {
    margin: 0;
    font-family: "Apple SD Gothic Neo", "Malgun Gothic", "Noto Sans KR", sans-serif;
    background: #FFF6DC;
    color: #5A4630;
    font-size: 20px;
    line-height: 1.6;
  }
  main { max-width: 760px; margin: 0 auto; padding: 32px 18px 60px; }
  h1 { text-align: center; font-size: 2.1rem; margin: 0 0 8px; color: #C98A00; }
  .sub { text-align: center; margin: 0 0 28px; font-size: 1.1rem; }
  .grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
  .type-btn {
    font-family: inherit; font-size: 1.25rem; font-weight: 700;
    padding: 18px 6px; border: 3px solid #F5C842; border-radius: 16px;
    background: #FFFDF5; color: #7A5200; cursor: pointer;
    transition: transform .12s, background .12s;
  }
  .type-btn:hover, .type-btn:focus-visible { background: #FFE58A; transform: translateY(-3px); outline: none; }
  .card {
    background: #FFFDF5; border: 4px solid #F5C842; border-radius: 28px;
    padding: 32px 24px; text-align: center;
    box-shadow: 0 8px 0 #EBC55A;
  }
  .badge {
    display: inline-block; background: #F5C842; color: #5A4000;
    font-weight: 800; padding: 4px 18px; border-radius: 999px; font-size: 1.1rem;
  }
  .emoji { font-size: 8rem; line-height: 1.1; margin: 12px 0 0; }
  .photo { display: block; max-width: 260px; max-height: 260px; width: auto; height: auto; margin: 12px auto 0; border-radius: 20px; }
  .name { font-size: 2.4rem; font-weight: 800; margin: 4px 0 16px; color: #C98A00; }
  .reason { text-align: left; background: #FFF1C4; border-radius: 18px; padding: 16px 22px; margin: 0 0 20px; }
  .reason p { margin: 6px 0; }
  .match { background: #FFEBA8; border-radius: 18px; padding: 14px 18px; margin-bottom: 24px; font-size: 1.15rem; }
  .match b { color: #A56A00; }
  .worst { background: #FFE0D2; }
  .worst b { color: #B8462A; }
  .worst .match-btn { border-color: #E07A5F; color: #B8462A; }
  .worst .match-btn:hover, .worst .match-btn:focus-visible { background: #FFD0BD; }
  .match-row { display: flex; align-items: center; gap: 16px; text-align: left; }
  .match-pic { flex: 0 0 auto; width: 96px; height: 96px; display: flex; align-items: center; justify-content: center;
    background: #FFFDF5; border-radius: 18px; font-size: 3.4rem; }
  .match-pic img { max-width: 88px; max-height: 88px; }
  .match-title { font-weight: 800; font-size: 1.2rem; margin-bottom: 4px; }
  .match-why { margin: 0 0 10px; font-size: 1.05rem; }
  .match-btn { font-family: inherit; font-size: 1.05rem; font-weight: 800; padding: 8px 18px;
    border: 3px solid #F5A800; border-radius: 999px; background: #FFFDF5; color: #A56A00; cursor: pointer; }
  .match-btn:hover, .match-btn:focus-visible { background: #FFE58A; outline: none; }
  @media (max-width: 520px) { .match-row { flex-direction: column; text-align: center; } }
  .reset {
    font-family: inherit; font-size: 1.3rem; font-weight: 800;
    padding: 14px 36px; border: none; border-radius: 999px;
    background: #F5A800; color: #fff; cursor: pointer;
  }
  .reset:hover, .reset:focus-visible { background: #D98F00; outline: none; }
  .hidden { display: none; }
  body { overflow-x: hidden; }
  main { position: relative; z-index: 1; }
  .rainbow { background: linear-gradient(90deg, #9B7FD4, #4FAF84, #4F8FD0, #F09A3E);
    -webkit-background-clip: text; background-clip: text; color: transparent; }
  .g-nt { --c: #B39DDB; --dark: #6F4FB0; --soft: #EFE7FB; }
  .g-nf { --c: #7FD1A8; --dark: #2F8F63; --soft: #E3F6EC; }
  .g-sj { --c: #86B8E8; --dark: #2F6DAE; --soft: #E3EFFB; }
  .g-sp { --c: #F7C04A; --dark: #B87800; --soft: #FFF1C4; }
  .group { margin-bottom: 20px; padding: 14px; border-radius: 22px; background: var(--soft); border: 3px dashed var(--c); }
  .group h2 { margin: 0 0 12px; font-size: 1.15rem; color: var(--dark); }
  .group .type-btn { border-color: var(--c); color: var(--dark); }
  .group .type-btn:hover, .group .type-btn:focus-visible { background: var(--c); color: #fff; }
  .card { border-color: var(--c, #F5C842); box-shadow: 0 8px 0 var(--c, #EBC55A); animation: pop .45s ease; }
  .badge { background: var(--dark, #C98A00); color: #fff; }
  .name { color: var(--dark, #C98A00); }
  .reason { background: var(--soft, #FFF1C4); }
  .photo { background: #fff; border: 5px solid var(--c, #F5C842); padding: 10px; }
  .emoji, .photo { animation: bob 2.4s ease-in-out infinite; }
  .bg { position: fixed; inset: 0; overflow: hidden; pointer-events: none; z-index: 0; }
  .bg span { position: absolute; bottom: -70px; opacity: .55; animation: rise linear infinite; }
  .confetti { position: fixed; top: -20px; width: 10px; height: 14px; z-index: 5; pointer-events: none; animation: fall 2s ease-in forwards; }
  @keyframes pop { from { transform: scale(.85); opacity: 0; } to { transform: scale(1); opacity: 1; } }
  @keyframes bob { 50% { transform: translateY(-8px); } }
  @keyframes rise { to { transform: translateY(-115vh) rotate(360deg); } }
  @keyframes fall { to { transform: translateY(110vh) rotate(720deg); } }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important; } .bg, .confetti { display: none; } }
  @media (max-width: 520px) {
    .grid { grid-template-columns: repeat(2, 1fr); }
    .emoji { font-size: 6rem; }
  }
</style>
</head>
<body>
<main>
  <section id="pick">
    <h1>🌟 <span class="rainbow">MBTI로 포켓몬 찾기</span> 🌟</h1>
    <p class="sub">내 MBTI 유형을 눌러보세요. 어울리는 포켓몬을 알려드릴게요!</p>
    <div id="grid"></div>
  </section>

  <section id="result" class="hidden">
    <div class="card" id="card">
      <span class="badge" id="r-type"></span>
      <div class="emoji" id="r-emoji"></div>
      <img class="photo hidden" id="r-img" alt="">
      <div class="name" id="r-name"></div>
      <div class="reason" id="r-reason"></div>
      <div class="match" id="r-match"></div>
      <div class="match worst" id="r-worst"></div>
      <button class="reset" id="reset">🔄 다시 고르기</button>
    </div>
  </section>
</main>

<script>
  var DATA = {
    INTJ: { pk: "뮤츠", emoji: "🧠", match: "ENFP",
      why: ["늘 몇 수 앞을 내다보는 전략가예요.", "강한 힘을 가졌지만 쉽게 속마음을 드러내지 않아요.", "혼자서도 목표를 끝까지 해내는 점이 닮았어요."] },
    INTP: { pk: "후딘", emoji: "🌀", match: "ENTJ",
      why: ["엄청난 두뇌로 생각에 푹 빠지는 탐구가예요.", "궁금한 것은 끝까지 파고드는 호기심이 대단해요.", "조용하지만 머릿속은 늘 바쁜 점이 닮았어요."] },
    ENTJ: { pk: "리자몽", emoji: "🐉", match: "INTP",
      why: ["당당하게 앞장서는 타고난 리더예요.", "목표를 향해 불꽃처럼 힘차게 나아가요.", "사람들을 이끄는 카리스마가 닮았어요."] },
    ENTP: { pk: "개굴닌자", emoji: "🥷", match: "INFJ",
      why: ["재치 있고 재빨라서 어디서든 방법을 찾아내요.", "새로운 아이디어로 상대를 깜짝 놀라게 해요.", "변화를 즐기고 도전을 좋아하는 점이 닮았어요."] },
    INFJ: { pk: "네이티오", emoji: "🦚", match: "ENTP",
      why: ["멀리 미래를 내다보는 신비로운 눈을 가졌어요.", "말수는 적지만 마음속 깊은 생각이 있어요.", "다른 사람의 마음을 잘 헤아리는 점이 닮았어요."] },
    INFP: { pk: "이브이", emoji: "🐾", match: "ENFJ",
      why: ["여러 모습으로 변할 수 있는 가능성을 품고 있어요.", "순수하고 따뜻한 마음을 가졌어요.", "자신만의 세계와 꿈을 소중히 하는 점이 닮았어요."] },
    ENFJ: { pk: "루카리오", emoji: "🐺", match: "INFP",
      why: ["상대의 마음을 파동으로 느끼는 따뜻한 리더예요.", "친구가 힘들 때 가장 먼저 곁을 지켜줘요.", "정의감과 배려심이 닮았어요."] },
    ENFP: { pk: "피카츄", emoji: "🐭", match: "INTJ",
      why: ["어디서든 분위기를 환하게 밝히는 에너자이저예요.", "사람들과 금방 친해지는 매력이 있어요.", "호기심 가득, 늘 활기찬 점이 닮았어요."] },
    ISTJ: { pk: "거북왕", emoji: "🛡️", match: "ESFP",
      why: ["단단한 등껍질처럼 믿음직하고 책임감이 강해요.", "맡은 일은 묵묵히 끝까지 해내요.", "규칙과 약속을 소중히 여기는 점이 닮았어요."] },
    ISFJ: { pk: "해피너스", emoji: "🩷", match: "ESTP",
      why: ["아픈 친구를 정성껏 돌봐주는 다정한 보살핌꾼이에요.", "남을 먼저 챙기는 따뜻한 마음을 가졌어요.", "조용히 곁에서 힘이 되어주는 점이 닮았어요."] },
    ESTJ: { pk: "윈디", emoji: "🦮", match: "ISFP",
      why: ["의리 있고 믿음직한 든든한 지킴이예요.", "질서와 규칙을 지키며 무리를 이끌어요.", "책임감 있게 앞장서는 점이 닮았어요."] },
    ESFJ: { pk: "라프라스", emoji: "🌊", match: "ISTP",
      why: ["친구들을 등에 태우고 안전하게 데려다주는 다정한 포켓몬이에요.", "다른 사람을 챙기며 기뻐하는 마음이 커요.", "모두가 어울리게 돕는 점이 닮았어요."] },
    ISTP: { pk: "한카리아스", emoji: "🦖", match: "ESFJ",
      why: ["말없이 빠르고 정확하게 움직이는 실력자예요.", "필요한 순간에 번개처럼 해결해요.", "혼자서도 척척 해내는 점이 닮았어요."] },
    ISFP: { pk: "이상해꽃", emoji: "🌺", match: "ESTJ",
      why: ["등에 핀 꽃처럼 조용하고 아름다운 감성을 가졌어요.", "자연과 평화로운 시간을 좋아해요.", "부드럽지만 마음이 단단한 점이 닮았어요."] },
    ESTP: { pk: "번치코", emoji: "🥊", match: "ISFJ",
      why: ["생각보다 먼저 몸이 움직이는 행동파예요.", "위기에도 겁내지 않고 시원하게 맞서요.", "지금 이 순간을 즐기는 점이 닮았어요."] },
    ESFP: { pk: "푸린", emoji: "🎈", match: "ISTJ",
      why: ["노래로 모두를 즐겁게 만드는 분위기 메이커예요.", "어디서든 주목받는 사랑스러운 매력이 있어요.", "함께 있으면 파티가 되는 점이 닮았어요."] }
  };

  // 사진 파일은 index.html과 같은 위치의 images 폴더에 넣어주세요.
  // 파일이 없으면 이모지가 대신 보여요.
  var PHOTO = {
    "피카츄": "images/pikachu.png",
    "뮤츠": "images/mewtwo.png",
    "후딘": "images/alakazam.png",
    "리자몽": "images/charizard.png",
    "개굴닌자": "images/greninja.png",
    "네이티오": "images/xatu.png",
    "이브이": "images/eevee.png",
    "루카리오": "images/lucario.png",
    "거북왕": "images/blastoise.png",
    "해피너스": "images/blissey.png",
    "윈디": "images/arcanine.png",
    "라프라스": "images/lapras.png",
    "한카리아스": "images/garchomp.png",
    "이상해꽃": "images/venusaur.png",
    "번치코": "images/blaziken.png",
    "푸린": "images/jigglypuff.png"
  };

  var COMPAT_WHY = {
    "ENFP-INTJ": "INTJ의 탄탄한 계획과 ENFP의 톡톡 튀는 아이디어가 만나, 서로에게 없는 부분을 채워줘요.",
    "ENTJ-INTP": "INTP의 깊은 생각을 ENTJ가 현실로 이끌어줘서, 함께하면 멋진 결과가 나와요.",
    "ENTP-INFJ": "INFJ의 깊은 마음과 ENTP의 재치가 만나 이야기가 끝없이 이어지는 사이예요.",
    "ENFJ-INFP": "INFP의 순수한 마음을 ENFJ가 따뜻하게 알아주고 응원해 줘요.",
    "ESFP-ISTJ": "ISTJ의 든든함과 ESFP의 활기가 서로에게 균형을 만들어줘요.",
    "ESTP-ISFJ": "ISFJ의 다정한 배려와 ESTP의 시원한 행동력이 서로를 보완해줘요.",
    "ESFJ-ISTP": "ISTP의 차분함을 ESFJ의 다정함이 편안하게 풀어줘요.",
    "ESTJ-ISFP": "ISFP의 부드러운 감성과 ESTJ의 믿음직함이 서로를 안정시켜줘요."
  };

  var WORST = { INTJ:"ESFP", ESFP:"INTJ", INTP:"ESFJ", ESFJ:"INTP", ENTJ:"ISFP", ISFP:"ENTJ",
                ENTP:"ISFJ", ISFJ:"ENTP", INFJ:"ESTP", ESTP:"INFJ", INFP:"ESTJ", ESTJ:"INFP",
                ENFJ:"ISTP", ISTP:"ENFJ", ENFP:"ISTJ", ISTJ:"ENFP" };
  var WORST_WHY = {
    "ESFP-INTJ": "INTJ는 계획과 조용한 시간이 중요하고, ESFP는 지금 이 순간의 즐거움이 중요해서 서로 답답해할 수 있어요.",
    "ESFJ-INTP": "INTP는 혼자 깊이 생각하는 시간이 필요한데, ESFJ는 함께 어울리길 원해서 마음이 엇갈리기 쉬워요.",
    "ENTJ-ISFP": "ENTJ는 빠르게 밀어붙이고, ISFP는 자기 속도와 감정이 중요해서 서로 부담을 느낄 수 있어요.",
    "ENTP-ISFJ": "ENTP는 새로운 것을 계속 바꾸고 싶어 하고, ISFJ는 익숙하고 안정된 것이 편해서 부딪히기 쉬워요.",
    "ESTP-INFJ": "ESTP는 바로 행동하는 편이고, INFJ는 깊이 생각한 뒤 움직여서 속도 차이가 크게 느껴져요.",
    "ESTJ-INFP": "ESTJ는 규칙과 현실이 먼저이고, INFP는 마음과 꿈이 먼저여서 서로를 이해하기 어려울 수 있어요.",
    "ENFJ-ISTP": "ENFJ는 마음을 말로 나누고 싶어 하고, ISTP는 말없이 혼자 해결하는 편이라 서운함이 생길 수 있어요.",
    "ENFP-ISTJ": "ENFP는 자유롭게 아이디어를 바꾸고, ISTJ는 계획과 약속을 지키는 게 중요해서 답답해질 수 있어요."
  };

  var GROUPS = [
    { cls: "g-nt", title: "💜 분석가형 · 생각이 깊은 전략가들", types: ["INTJ","INTP","ENTJ","ENTP"], colors: ["#B39DDB","#6F4FB0","#D1C4E9"] },
    { cls: "g-nf", title: "💚 외교관형 · 마음이 따뜻한 이상가들", types: ["INFJ","INFP","ENFJ","ENFP"], colors: ["#7FD1A8","#2F8F63","#C6EBD7"] },
    { cls: "g-sj", title: "💙 관리자형 · 믿음직한 현실파들", types: ["ISTJ","ISFJ","ESTJ","ESFJ"], colors: ["#86B8E8","#2F6DAE","#C5DDF5"] },
    { cls: "g-sp", title: "🧡 탐험가형 · 자유로운 행동파들", types: ["ISTP","ISFP","ESTP","ESFP"], colors: ["#F7C04A","#F09A3E","#FFE29A"] }
  ];
  var GROUP_OF = {};
  GROUPS.forEach(function (g) { g.types.forEach(function (t) { GROUP_OF[t] = g; }); });

  var ORDER = ["INTJ","INTP","ENTJ","ENTP","INFJ","INFP","ENFJ","ENFP",
               "ISTJ","ISFJ","ESTJ","ESFJ","ISTP","ISFP","ESTP","ESFP"];

  var grid = document.getElementById("grid");
  var pick = document.getElementById("pick");
  var result = document.getElementById("result");

  GROUPS.forEach(function (g) {
    var box = document.createElement("div");
    box.className = "group " + g.cls;
    var h = document.createElement("h2");
    h.textContent = g.title;
    box.appendChild(h);
    var row = document.createElement("div");
    row.className = "grid";
    g.types.forEach(function (t) {
      var b = document.createElement("button");
      b.className = "type-btn";
      b.textContent = t;
      b.addEventListener("click", function () { show(t); });
      row.appendChild(b);
    });
    box.appendChild(row);
    grid.appendChild(box);
  });

  // 배경에 떠오르는 장식
  (function () {
    var bg = document.createElement("div");
    bg.className = "bg";
    bg.setAttribute("aria-hidden", "true");
    var icons = ["⭐","✨","🎈","🍀","💛","🌈","🫧","🌸"];
    for (var i = 0; i < 14; i++) {
      var sp = document.createElement("span");
      sp.textContent = icons[i % icons.length];
      sp.style.left = (Math.random() * 96) + "vw";
      sp.style.fontSize = (22 + Math.random() * 26) + "px";
      sp.style.animationDuration = (14 + Math.random() * 14) + "s";
      sp.style.animationDelay = (-Math.random() * 20) + "s";
      bg.appendChild(sp);
    }
    document.body.insertBefore(bg, document.body.firstChild);
  })();

  function confetti(colors) {
    var all = colors.concat(["#FF8FA3", "#FFF3B0", "#F5C842"]);
    for (var i = 0; i < 36; i++) {
      var c = document.createElement("span");
      c.className = "confetti";
      c.style.left = (Math.random() * 100) + "vw";
      c.style.background = all[i % all.length];
      c.style.borderRadius = (i % 3) ? "2px" : "50%";
      c.style.animationDuration = (1.4 + Math.random() * 1.4) + "s";
      c.style.animationDelay = (Math.random() * 0.4) + "s";
      document.body.appendChild(c);
      (function (el) { setTimeout(function () { el.remove(); }, 3400); })(c);
    }
  }

  function show(t) {
    var d = DATA[t];
    var m = DATA[d.match];
    var g = GROUP_OF[t];
    var card = document.getElementById("card");
    card.className = "card " + g.cls;
    card.style.animation = "none";
    void card.offsetWidth;
    card.style.animation = "";
    confetti(g.colors);
    document.getElementById("r-type").textContent = t;
    var emojiEl = document.getElementById("r-emoji");
    var imgEl = document.getElementById("r-img");
    emojiEl.textContent = d.emoji;
    emojiEl.classList.remove("hidden");
    imgEl.classList.add("hidden");
    imgEl.onload = function () {
      imgEl.classList.remove("hidden");
      emojiEl.classList.add("hidden");
    };
    imgEl.onerror = function () {
      imgEl.classList.add("hidden");
      emojiEl.classList.remove("hidden");
    };
    imgEl.alt = d.pk;
    if (PHOTO[d.pk]) { imgEl.src = PHOTO[d.pk]; } else { imgEl.onerror(); }
    document.getElementById("r-name").textContent = d.pk;
    document.getElementById("r-reason").innerHTML =
      d.why.map(function (line) { return "<p>✔ " + line + "</p>"; }).join("");
    var why = COMPAT_WHY[[t, d.match].sort().join("-")] || "";
    var pic = PHOTO[m.pk] ? '<img src="' + PHOTO[m.pk] + '" alt="' + m.pk + '">' : m.emoji;
    document.getElementById("r-match").innerHTML =
      '<div class="match-row"><div class="match-pic">' + pic + '</div><div>' +
      '<div class="match-title">💛 찰떡궁합: <b>' + d.match + '</b> (' + m.pk + ')</div>' +
      '<p class="match-why">' + why + '</p>' +
      '<button class="match-btn" id="go-match">' + m.pk + ' 보러 가기 ➜</button></div></div>';
    document.getElementById("go-match").addEventListener("click", function () { show(d.match); });
    var w = WORST[t], wd = DATA[w];
    var wwhy = WORST_WHY[[t, w].sort().join("-")] || "";
    var wpic = PHOTO[wd.pk] ? '<img src="' + PHOTO[wd.pk] + '" alt="' + wd.pk + '">' : wd.emoji;
    document.getElementById("r-worst").innerHTML =
      '<div class="match-row"><div class="match-pic">' + wpic + '</div><div>' +
      '<div class="match-title">💔 조심! 상극 궁합: <b>' + w + '</b> (' + wd.pk + ')</div>' +
      '<p class="match-why">' + wwhy + ' 그래도 서로 이해하려고 하면 충분히 친해질 수 있어요!</p>' +
      '<button class="match-btn" id="go-worst">' + wd.pk + ' 보러 가기 ➜</button></div></div>';
    document.getElementById("go-worst").addEventListener("click", function () { show(w); });
    pick.classList.add("hidden");
    result.classList.remove("hidden");
    window.scrollTo(0, 0);
  }

  document.getElementById("reset").addEventListener("click", function () {
    result.classList.add("hidden");
    pick.classList.remove("hidden");
    window.scrollTo(0, 0);
  });
</script>
</body>
</html>

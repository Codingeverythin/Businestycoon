import streamlit as st

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=VT323&display=swap');
  :root{--g:#00ff41;--gd:#00aa2b;--gf:#003d0f;--gm:#00cc35;--amber:#ffb300;--red:#ff4444;--bg:#0a0f0a;--blue:#00cfff;--purple:#cc44ff;}
  *{box-sizing:border-box;margin:0;padding:0;}

  /* ── INTRO ── */
  #intro{
    font-family:'Share Tech Mono',monospace;
    background:var(--bg);
    color:var(--g);
    min-height:520px;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    position:relative;
    overflow:hidden;
    padding:24px;
  }
  #intro::before{
    content:'';position:absolute;inset:0;
    background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,0.1) 2px,rgba(0,0,0,0.1) 4px);
    pointer-events:none;
  }
  .intro-logo{
    font-family:'VT323',monospace;
    font-size:42px;
    color:var(--g);
    letter-spacing:3px;
    text-align:center;
    margin-bottom:8px;
    opacity:0;
    animation:logoIn 0.8s ease 0.3s forwards;
    text-shadow:0 0 24px #00ff4188;
  }
  .intro-sub{
    font-size:13px;color:var(--gd);letter-spacing:2px;
    margin-bottom:48px;
    opacity:0;
    animation:logoIn 0.6s ease 1s forwards;
  }
  @keyframes logoIn{from{opacity:0;transform:translateY(-16px);}to{opacity:1;transform:translateY(0);}}

  .typewriter-wrap{
    background:var(--gf);
    border:1px solid var(--gd);
    padding:20px 28px;
    max-width:420px;
    width:100%;
    text-align:left;
    margin-bottom:36px;
    position:relative;
    opacity:0;
    animation:logoIn 0.5s ease 1.5s forwards;
  }
  .typewriter-wrap::before{
    content:'> CREDITS.TXT';
    position:absolute;
    top:-10px;left:12px;
    background:var(--bg);
    padding:0 6px;
    font-size:10px;
    color:var(--gd);
  }
  #typewriter{
    font-size:14px;
    color:var(--g);
    line-height:2;
    min-height:60px;
  }
  .cursor-blink{
    display:inline-block;
    width:10px;height:14px;
    background:var(--g);
    margin-left:2px;
    vertical-align:middle;
    animation:blink 0.8s step-end infinite;
  }
  @keyframes blink{50%{opacity:0;}}

  .intro-skip{
    font-family:'Share Tech Mono',monospace;
    background:var(--gf);
    border:1px solid var(--gm);
    color:var(--g);
    padding:10px 28px;
    font-size:13px;
    cursor:pointer;
    letter-spacing:2px;
    border-radius:3px;
    opacity:0;
    animation:logoIn 0.5s ease 3.8s forwards;
    transition:all 0.15s;
  }
  .intro-skip:hover{background:var(--gm);color:#000;}
  .intro-skip:active{transform:scale(0.96);}

  .scanline{
    position:absolute;top:0;left:0;right:0;height:60px;
    background:linear-gradient(to bottom,transparent,rgba(0,255,65,0.04),transparent);
    animation:scanMove 4s linear infinite;
    pointer-events:none;
  }
  @keyframes scanMove{from{top:-60px;}to{top:100%;}}

  /* stars */
  .star{position:absolute;width:2px;height:2px;background:var(--g);border-radius:50%;opacity:0;animation:twinkle var(--d) ease-in-out var(--del) infinite;}
  @keyframes twinkle{0%,100%{opacity:0;}50%{opacity:0.6;}}

  /* ── GAME (hidden until intro done) ── */
  #game{display:none;font-family:'Share Tech Mono',monospace;background:var(--bg);color:var(--g);padding:16px;border:1px solid var(--gd);position:relative;min-height:520px;}
  #game::before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,0.07) 2px,rgba(0,0,0,0.07) 4px);pointer-events:none;z-index:10;}
  .title{font-family:'VT323',monospace;font-size:28px;color:var(--g);text-align:center;border-bottom:1px solid var(--gd);padding-bottom:8px;margin-bottom:12px;letter-spacing:2px;animation:titlePulse 3s ease-in-out infinite;}
  @keyframes titlePulse{0%,100%{text-shadow:0 0 8px #00ff4155;}50%{text-shadow:0 0 18px #00ff4199;}}
  .stats-row{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-bottom:12px;}
  .stat{background:var(--gf);border:1px solid var(--gd);padding:6px 8px;transition:border-color 0.3s;}
  .stat:hover{border-color:var(--g);}
  .stat-label{color:var(--gd);font-size:10px;}
  .stat-val{color:var(--amber);font-size:15px;font-family:'VT323',monospace;}
  .log{background:var(--gf);border:1px solid var(--gd);padding:6px 8px;font-size:10px;height:75px;overflow-y:auto;margin-bottom:10px;}
  .log-line{margin-bottom:2px;color:var(--gd);animation:fadeIn 0.3s ease;}
  @keyframes fadeIn{from{opacity:0;transform:translateX(-6px);}to{opacity:1;transform:translateX(0);}}
  .log-line.good{color:var(--g);}
  .log-line.warn{color:var(--amber);}
  .log-line.err{color:var(--red);}
  .money-btn{width:100%;font-family:'VT323',monospace;font-size:32px;background:linear-gradient(135deg,#001a05,#002d0a);border:2px solid var(--g);color:var(--g);padding:14px;cursor:pointer;letter-spacing:3px;margin-bottom:10px;transition:all 0.15s;position:relative;overflow:hidden;}
  .money-btn:hover{background:linear-gradient(135deg,#002d0a,#004015);border-color:#00ff88;color:#00ff88;}
  .money-btn:active{transform:scale(0.97);}
  .money-btn::before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(0,255,65,0.08),transparent);animation:shimmer 2s linear infinite;}
  @keyframes shimmer{0%{transform:translateX(-100%);}100%{transform:translateX(100%);}}
  .btn-row{display:flex;gap:6px;margin-bottom:10px;flex-wrap:wrap;}
  .btn{font-family:'Share Tech Mono',monospace;padding:8px 14px;cursor:pointer;font-size:12px;letter-spacing:1px;border:none;border-radius:3px;font-weight:bold;transition:all 0.15s;position:relative;overflow:hidden;}
  .btn:active{transform:scale(0.95);}
  .btn::after{content:'';position:absolute;inset:0;background:rgba(255,255,255,0.12);opacity:0;transition:opacity 0.15s;}
  .btn:hover::after{opacity:1;}
  .btn-biz{background:linear-gradient(135deg,#003a5c,#005a8c);color:var(--blue);border:1px solid var(--blue);box-shadow:0 0 8px #00cfff33;}
  .btn-biz:hover{box-shadow:0 0 16px #00cfff66;color:#fff;}
  .btn-upg{background:linear-gradient(135deg,#3a2000,#5c3500);color:var(--amber);border:1px solid var(--amber);box-shadow:0 0 8px #ffb30033;}
  .btn-upg:hover{box-shadow:0 0 16px #ffb30066;color:#fff;}
  .btn-collect{background:linear-gradient(135deg,#003a1a,#005a28);color:var(--g);border:1px solid var(--g);box-shadow:0 0 8px #00ff4133;}
  .btn-collect:hover{box-shadow:0 0 16px #00ff4166;color:#fff;}
  .btn-settings{background:linear-gradient(135deg,#2a0044,#440066);color:var(--purple);border:1px solid var(--purple);box-shadow:0 0 8px #cc44ff33;}
  .btn-settings:hover{box-shadow:0 0 16px #cc44ff66;color:#fff;}
  .btn-reset{background:linear-gradient(135deg,#3a0000,#5c0000);color:var(--red);border:1px solid var(--red);box-shadow:0 0 8px #ff444433;}
  .btn-reset:hover{box-shadow:0 0 16px #ff444466;color:#fff;}
  .btn-pause{background:linear-gradient(135deg,#002244,#003366);color:var(--blue);border:1px solid var(--blue);}
  .btn-pause.paused{background:linear-gradient(135deg,#1a1a00,#2a2a00);color:var(--amber);border-color:var(--amber);}
  .panel{display:none;position:absolute;inset:0;background:rgba(0,6,0,0.97);z-index:20;padding:16px;overflow-y:auto;animation:panelIn 0.2s ease;}
  @keyframes panelIn{from{opacity:0;transform:scale(0.97);}to{opacity:1;transform:scale(1);}}
  .panel.open{display:block;}
  .panel-header{display:flex;justify-content:space-between;align-items:center;padding-bottom:8px;margin-bottom:12px;}
  .panel-title{font-family:'VT323',monospace;font-size:26px;letter-spacing:2px;}
  .biz-panel .panel-title{color:var(--blue);border-bottom:1px solid var(--blue);}
  .upg-panel .panel-title{color:var(--amber);border-bottom:1px solid var(--amber);}
  .set-panel .panel-title{color:var(--purple);border-bottom:1px solid var(--purple);}
  .grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;}
  .card{background:var(--gf);border:1px solid var(--gd);padding:9px;cursor:pointer;transition:all 0.18s;border-radius:3px;}
  .card:hover{border-color:var(--g);transform:translateY(-1px);}
  .card.bought{opacity:0.38;cursor:default;transform:none!important;}
  .card-name{font-size:12px;margin-bottom:2px;}
  .card-desc{font-size:10px;color:var(--gd);margin-top:1px;}
    .card-cost{font-size:11px;}
</style>
""", unsafe_allow_html=True)
size:11px;margin-top:4px;}
</style>
""", unsafe_allow_html=True)
  .biz-bar{height:4px;background:#001205;border:1px solid var(--gd);margin-top:5px;overflow:hidden;border-radius:2px;}
  .biz-fill{height:100%;background:var(--gm);transition:width 0.2s;}
  .owned-badge{font-size:10px;color:var(--amber);}
  .popup-overlay{display:none;position:absolute;inset:0;background:rgba(0,0,0,0.82);z-index:50;align-items:center;justify-content:center;}
  .popup-overlay.open{display:flex;}
  .popup{background:#0a0f0a;border:2px solid var(--red);padding:24px;max-width:280px;width:90%;text-align:center;animation:popIn 0.2s ease;border-radius:4px;}
  @keyframes popIn{from{transform:scale(0.8);opacity:0;}to{transform:scale(1);opacity:1;}}
  .popup-icon{font-size:36px;margin-bottom:10px;}
  .popup-title{font-family:'VT323',monospace;font-size:26px;color:var(--red);letter-spacing:2px;margin-bottom:6px;}
  .popup-msg{font-size:11px;color:var(--gd);margin-bottom:16px;line-height:1.6;}
  .popup-btns{display:flex;gap:10px;justify-content:center;}
  .set-row{display:flex;align-items:center;gap:12px;padding:10px 0;border-bottom:1px solid var(--gf);}
  .set-label{font-size:12px;color:var(--gd);min-width:120px;}
  .set-val{font-size:12px;color:var(--g);min-width:40px;text-align:right;}
  input[type=range]{flex:1;accent-color:var(--purple);cursor:pointer;}
  .float-label{position:fixed;pointer-events:none;font-family:'VT323',monospace;font-size:22px;color:var(--g);z-index:200;animation:floatUp 0.9s ease-out forwards;}
  @keyframes floatUp{0%{opacity:1;transform:translateY(0);}100%{opacity:0;transform:translateY(-60px);}}
  .paused-banner{display:none;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);z-index:15;font-family:'VT323',monospace;font-size:52px;color:var(--amber);letter-spacing:4px;pointer-events:none;animation:blinkPause 1s step-end infinite;}
  @keyframes blinkPause{50%{opacity:0;}}
  .paused-banner.show{display:block;}
  .ticker{font-size:10px;color:var(--gd);border-top:1px dashed var(--gf);padding-top:6px;margin-top:4px;overflow:hidden;white-space:nowrap;}
  .tick-inner{display:inline-block;animation:scroll 20s linear infinite;}
  @keyframes scroll{from{transform:translateX(100%);}to{transform:translateX(-100%);}}
  .section-title{color:var(--gd);font-size:11px;margin:4px 0;border-bottom:1px dashed var(--gf);padding-bottom:2px;}
</style>

<!-- ══ INTRO SCREEN ══ -->
<div id="intro">
  <div class="scanline"></div>
  <div id="stars"></div>
  <div class="intro-logo">▓▒░ BUSINESS TYCOON ░▒▓</div>
  <div class="intro-sub">V 1 . 2  —  T E R M I N A L  E D I T I O N</div>
  <div class="typewriter-wrap">
    <div id="typewriter"><span class="cursor-blink"></span></div>
  </div>
  <button class="intro-skip" id="skip-btn" onclick="launchGame()">[ PRESS TO PLAY ]</button>
</div>

<!-- ══ GAME ══ -->
<div id="game">
  <h2 class="sr-only">Business Tycoon V1.2</h2>
  <div class="title">▓▒░ BUSINESS TYCOON V1.2 ░▒▓</div>
  <div class="paused-banner" id="paused-banner">⏸ PAUSED</div>
  <div class="stats-row" id="stats-row"></div>
  <button class="money-btn" onclick="clickMoney(event)">💰 CLICK FOR MONEY 💰</button>
  <div class="section-title">> ACTIVITY LOG</div>
  <div class="log" id="log"></div>
  <div class="btn-row">
    <button class="btn btn-biz" onclick="openPanel('biz-panel')">🏢 BUSINESSES</button>
    <button class="btn btn-upg" onclick="openPanel('upg-panel')">⚙ UPGRADES</button>
    <button class="btn btn-collect" onclick="collectAll()">💵 COLLECT</button>
    <button class="btn btn-settings" onclick="openPanel('set-panel')">⚙ SETTINGS</button>
    <button class="btn btn-pause" id="pause-btn" onclick="togglePause()">⏸ PAUSE</button>
    <button class="btn btn-reset" onclick="openResetPopup()">🗑 RESET</button>
  </div>
  <div class="ticker"><span class="tick-inner" id="ticker-text">C:\> BUSINESS TYCOON V1.2 LOADING...</span></div>

  <div class="panel biz-panel" id="biz-panel">
    <div class="panel-header">
      <div class="panel-title">🏢 BUSINESSES</div>
      <button class="btn btn-biz" onclick="closePanel('biz-panel')" style="padding:4px 10px;">✕ CLOSE</button>
    </div>
    <div class="grid2" id="biz-grid"></div>
  </div>
  <div class="panel upg-panel" id="upg-panel">
    <div class="panel-header">
      <div class="panel-title">⚙ UPGRADES</div>
      <button class="btn btn-upg" onclick="closePanel('upg-panel')" style="padding:4px 10px;">✕ CLOSE</button>
    </div>
    <div class="grid2" id="upg-grid"></div>
  </div>
  <div class="panel set-panel" id="set-panel">
    <div class="panel-header">
      <div class="panel-title">⚙ SETTINGS</div>
      <button class="btn btn-settings" onclick="closePanel('set-panel')" style="padding:4px 10px;">✕ CLOSE</button>
    </div>
    <div class="set-row">
      <span class="set-label">🔊 Volume</span>
      <input type="range" min="0" max="100" value="60" id="vol-slider" oninput="setVolume(this.value)">
      <span class="set-val" id="vol-val">60%</span>
    </div>
    <div class="set-row">
      <span class="set-label">🎵 Sound FX</span>
      <button class="btn btn-settings" id="sfx-toggle" onclick="toggleSFX()" style="padding:5px 14px;">ON</button>
    </div>
    <div class="set-row">
      <span class="set-label">⏸ Game Pause</span>
      <button class="btn btn-pause" id="set-pause-btn" onclick="togglePause()" style="padding:5px 14px;">RUNNING</button>
    </div>
    <div class="set-row" style="border:none;margin-top:12px;">
      <span class="set-label" style="color:var(--gd);font-size:10px;">Made by Metehan Ata.Als<br>Business Tycoon V1.2</span>
    </div>
  </div>
  <div class="popup-overlay" id="reset-popup">
    <div class="popup">
      <div class="popup-icon">⚠️</div>
      <div class="popup-title">WARNING!</div>
      <div class="popup-msg">FORMAT C: /Y will delete ALL save data.<br>Your businesses, money and upgrades<br>will be permanently wiped.<br><br>Are you absolutely sure?</div>
      <div class="popup-btns">
        <button class="btn btn-reset" onclick="confirmReset()" style="padding:8px 18px;font-size:13px;">YES, RESET</button>
        <button class="btn btn-collect" onclick="closeResetPopup()" style="padding:8px 18px;font-size:13px;">CANCEL</button>
      </div>
    </div>
  </div>
</div>

<script>
// ── Stars ──────────────────────────────────────────────
const starsEl=document.getElementById('stars');
for(let i=0;i<40;i++){
  const s=document.createElement('div');s.className='star';
  s.style.cssText=`left:${Math.random()*100}%;top:${Math.random()*100}%;--d:${2+Math.random()*3}s;--del:${Math.random()*3}s`;
  starsEl.appendChild(s);
}

// ── Typewriter ─────────────────────────────────────────
const INTRO_TEXT=[
  'Initializing TYCOON.EXE...',
  '',
  'This game was made by',
  'Metehan Ata.Als',
  '',
  '> All rights reserved.',
  '> Version 1.2 — Terminal Edition',
];
let lineIdx=0,charIdx=0,introDone=false;
const tw=document.getElementById('typewriter');

function typeNext(){
  if(introDone)return;
  if(lineIdx>=INTRO_TEXT.length){introDone=true;return;}
  const line=INTRO_TEXT[lineIdx];
  if(charIdx<line.length){
    renderTW(line.substring(0,charIdx+1),true);
    charIdx++;
    setTimeout(typeNext,line.startsWith('>')&&charIdx<4?80:charIdx===1?60:45);
  } else {
    renderTW(line,false);
    lineIdx++;charIdx=0;
    setTimeout(typeNext,lineIdx===3?300:120);
  }
}
function renderTW(partial,showCursor){
  const lines=INTRO_TEXT.slice(0,lineIdx).map((l,i)=>{
    if(l==='')return'<br>';
    const color=l.startsWith('>')?' style="color:var(--gd)"':l==='Metehan Ata.Als'?' style="color:var(--amber);font-size:16px"':'';
    return`<div${color}>${l}</div>`;
  }).join('');
  const cur=`<div style="color:var(--g)">${partial}${showCursor?'<span class="cursor-blink"></span>':''}</div>`;
  tw.innerHTML=lines+cur;
}

setTimeout(typeNext, 1800);

// ── Launch game ────────────────────────────────────────
function launchGame(){
  const intro=document.getElementById('intro');
  intro.style.transition='opacity 0.5s ease';
  intro.style.opacity='0';
  introSnd();
  setTimeout(()=>{
    intro.style.display='none';
    const g=document.getElementById('game');
    g.style.display='block';
    g.style.opacity='0';
    g.style.transition='opacity 0.5s ease';
    setTimeout(()=>g.style.opacity='1',50);
    bootGame();
  },500);
}

// ── GAME CODE ──────────────────────────────────────────
const CLICK_AMOUNT=5;
const BUSINESSES=[
  {id:'lemonade',name:'LEMONADE STAND',baseCost:15,baseIncome:0.5,timeMs:1200,icon:'🍋'},
  {id:'newspaper',name:'NEWSPAPER ROUND',baseCost:80,baseIncome:2,timeMs:3000,icon:'📰'},
  {id:'carwash',name:'CAR WASH',baseCost:400,baseIncome:8,timeMs:6000,icon:'🚗'},
  {id:'pizza',name:'PIZZA DELIVERY',baseCost:2000,baseIncome:40,timeMs:12000,icon:'🍕'},
  {id:'software',name:'SOFTWARE SHOP',baseCost:12000,baseIncome:200,timeMs:30000,icon:'💾'},
  {id:'datacenter',name:'DATA CENTER',baseCost:60000,baseIncome:1000,timeMs:60000,icon:'🖥️'},
];
const UPGRADES=[
  {id:'turbo_lemon',name:'TURBO LEMONS',desc:'Lemonade 2x faster',cost:50,effect:()=>{bizState.lemonade.speedMult*=0.5;}},
  {id:'double_news',name:'2X PAPERS',desc:'Newspaper income x2',cost:300,effect:()=>{bizState.newspaper.incomeMult*=2;}},
  {id:'auto_collect',name:'AUTO-COLLECT',desc:'Auto-collect all income',cost:1500,effect:()=>{gs.autoCollect=true;}},
  {id:'tax_patch',name:'TAX PATCH',desc:'All income +25%',cost:8000,effect:()=>{gs.globalMult*=1.25;}},
  {id:'turbo_oven',name:'TURBO OVEN',desc:'Pizza 2x faster',cost:6000,effect:()=>{bizState.pizza.speedMult*=0.5;}},
  {id:'corp_lawyer',name:'CORP LAWYER',desc:'All income x2',cost:50000,effect:()=>{gs.globalMult*=2;}},
  {id:'click_boost',name:'CLICK BOOST',desc:'Click gives 5x more',cost:2000,effect:()=>{gs.clickMult=(gs.clickMult||1)*5;}},
];
const initGS=()=>({money:0,totalEarned:0,clicks:0,autoCollect:false,globalMult:1,clickMult:1,boughtUpgrades:[]});
const initBS=()=>{const s={};BUSINESSES.forEach(b=>s[b.id]={owned:0,progress:0,speedMult:1,incomeMult:1,pending:0});return s;};
let gs=initGS(),bizState=initBS(),intervals={},paused=false,sfxOn=true,volume=0.6;

// Audio
const AudioCtx=window.AudioContext||window.webkitAudioContext;
let actx=null;
function getACtx(){if(!actx)actx=new AudioCtx();return actx;}
function playTone(freq,type,dur,vol){
  if(!sfxOn)return;
  try{const c=getACtx(),o=c.createOscillator(),g=c.createGain();o.connect(g);g.connect(c.destination);o.type=type;o.frequency.setValueAtTime(freq,c.currentTime);g.gain.setValueAtTime(vol*volume,c.currentTime);g.gain.exponentialRampToValueAtTime(0.001,c.currentTime+dur);o.start(c.currentTime);o.stop(c.currentTime+dur);}catch(e){}
}
function introSnd(){[300,500,700,900,1100].forEach((f,i)=>setTimeout(()=>playTone(f,'sine',0.15,0.3),i*80));}
function sndClick(){playTone(440,'sine',0.08,0.3);setTimeout(()=>playTone(600,'sine',0.06,0.2),50);}
function sndBuy(){[300,500,700].forEach((f,i)=>setTimeout(()=>playTone(f,'square',0.08,0.18),i*65));}
function sndUpgrade(){[400,600,800,1000].forEach((f,i)=>setTimeout(()=>playTone(f,'sine',0.12,0.25),i*70));}
function sndCollect(){[523,659,784].forEach((f,i)=>setTimeout(()=>playTone(f,'sine',0.08,0.12),i*80));}
function sndError(){playTone(200,'sawtooth',0.12,0.2);setTimeout(()=>playTone(150,'sawtooth',0.1,0.25),100);}
function sndReset(){[800,600,400,200].forEach((f,i)=>setTimeout(()=>playTone(f,'sawtooth',0.1,0.18),i*80));}
function sndPause(){playTone(300,'square',0.08,0.15);setTimeout(()=>playTone(200,'square',0.1,0.2),100);}
function sndOpen(){playTone(500,'sine',0.06,0.08);setTimeout(()=>playTone(700,'sine',0.06,0.1),60);}
function setVolume(v){volume=v/100;document.getElementById('vol-val').textContent=v+'%';}
function toggleSFX(){sfxOn=!sfxOn;document.getElementById('sfx-toggle').textContent=sfxOn?'ON':'OFF';playTone(440,'sine',0.1,0.3);}

const save=()=>localStorage.setItem('bizTycoon12',JSON.stringify({gs,bizState}));
function load(){try{const d=JSON.parse(localStorage.getItem('bizTycoon12')||'null');if(d&&d.gs&&d.bizState){gs=d.gs;bizState=d.bizState;}}catch(e){}}
function resetGame(){sndReset();gs=initGS();bizState=initBS();Object.values(intervals).forEach(clearInterval);intervals={};paused=false;updatePauseUI();save();log('SYSTEM: ALL DATA WIPED','err');renderAll();}
function openPanel(id){sndOpen();document.getElementById(id).classList.add('open');renderAll();}
function closePanel(id){sndOpen();document.getElementById(id).classList.remove('open');}
function openResetPopup(){sndError();document.getElementById('reset-popup').classList.add('open');}
function closeResetPopup(){sndOpen();document.getElementById('reset-popup').classList.remove('open');}
function confirmReset(){closeResetPopup();resetGame();}
function togglePause(){
  paused=!paused;sndPause();updatePauseUI();
  if(paused){Object.values(intervals).forEach(clearInterval);intervals={};}
  else{BUSINESSES.forEach(b=>{if(bizState[b.id].owned>0)startLoop(b);});}
}
function updatePauseUI(){
  const pb=document.getElementById('pause-btn'),spb=document.getElementById('set-pause-btn'),banner=document.getElementById('paused-banner');
  pb.textContent=paused?'▶ RESUME':'⏸ PAUSE';
  pb.className='btn btn-pause'+(paused?' paused':'');
  if(spb){spb.textContent=paused?'PAUSED':'RUNNING';spb.className='btn '+(paused?'btn-reset':'btn-pause');}
  banner.className='paused-banner'+(paused?' show':'');
}
function clickMoney(e){
  if(paused){sndError();log('Game is paused!','err');return;}
  sndClick();const amt=CLICK_AMOUNT*(gs.clickMult||1);
  gs.money+=amt;gs.totalEarned+=amt;gs.clicks++;
  spawnFloat(e,'+'+fmt(amt));renderStats();save();
}
function spawnFloat(e,text){
  const el=document.createElement('div');el.className='float-label';el.textContent=text;
  el.style.left=(e.clientX-20)+'px';el.style.top=(e.clientY-20)+'px';
  document.body.appendChild(el);setTimeout(()=>el.remove(),900);
}
function buyBiz(id){
  if(paused){sndError();log('Unpause first!','err');return;}
  const b=BUSINESSES.find(x=>x.id===id),cost=bizCost(b);
  if(gs.money<cost){sndError();log('INSUFFICIENT FUNDS: Need '+fmt(cost),'err');return;}
  sndBuy();gs.money-=cost;bizState[id].owned++;
  log('ACQUIRED: '+b.name+' #'+bizState[id].owned+' for '+fmt(cost),'good');
  if(bizState[id].owned===1)startLoop(b);
  renderAll();save();
}
function startLoop(b){
  if(intervals[b.id])clearInterval(intervals[b.id]);
  intervals[b.id]=setInterval(()=>{
    if(paused)return;
    const s=bizState[b.id];if(!s.owned)return;
    s.progress+=100/(b.timeMs*(s.speedMult||1));
    if(s.progress>=1){s.progress=0;const earned=b.baseIncome*s.owned*(s.incomeMult||1)*gs.globalMult;if(gs.autoCollect){gs.money+=earned;gs.totalEarned+=earned;save();}else s.pending=(s.pending||0)+earned;}
    const f=document.getElementById('fill-'+b.id);if(f)f.style.width=Math.min(100,s.progress*100)+'%';
  },100);
}
function collectAll(){
  if(paused){sndError();log('Game is paused!','err');return;}
  let total=0;BUSINESSES.forEach(b=>{const s=bizState[b.id];if(s.pending){total+=s.pending;s.pending=0;}});
  if(total>0){sndCollect();gs.money+=total;gs.totalEarned+=total;log('COLLECTED: '+fmt(total),'good');}
  else log('Nothing to collect yet.','');
  renderAll();save();
}
function buyUpgrade(id){
  if(paused){sndError();log('Unpause first!','err');return;}
  const u=UPGRADES.find(x=>x.id===id);
  if(!u||gs.boughtUpgrades.includes(id))return;
  if(gs.money<u.cost){sndError();log('INSUFFICIENT FUNDS: Need '+fmt(u.cost),'err');return;}
  sndUpgrade();gs.money-=u.cost;gs.boughtUpgrades.push(id);u.effect();
  log('UPGRADE INSTALLED: '+u.name,'warn');
  BUSINESSES.forEach(b=>{if(bizState[b.id].owned>0)startLoop(b);});
  renderAll();save();
}
const fmt=n=>n>=1e9?'$'+(n/1e9).toFixed(2)+'B':n>=1e6?'$'+(n/1e6).toFixed(2)+'M':n>=1e3?'$'+(n/1e3).toFixed(2)+'K':'$'+n.toFixed(2);
const bizCost=b=>Math.floor(b.baseCost*Math.pow(1.15,bizState[b.id].owned));
const bizIncome=b=>b.baseIncome*bizState[b.id].owned*(bizState[b.id].incomeMult||1)*gs.globalMult;
function renderStats(){
  const totalIncome=BUSINESSES.reduce((s,b)=>s+bizIncome(b),0);
  document.getElementById('stats-row').innerHTML=[{label:'BALANCE',val:fmt(gs.money)},{label:'TOTAL EARNED',val:fmt(gs.totalEarned)},{label:'INCOME/CYC',val:fmt(totalIncome)},{label:'CLICKS',val:gs.clicks}].map(v=>`<div class="stat"><div class="stat-label">${v.label}</div><div class="stat-val">${v.val}</div></div>`).join('');
}
function renderBizGrid(){
  document.getElementById('biz-grid').innerHTML=BUSINESSES.map(b=>{
    const s=bizState[b.id],cost=bizCost(b),canAfford=gs.money>=cost;
    const pend=s.pending>0.01?` <span style="color:var(--amber)">[+${fmt(s.pending)}]</span>`:'';
    return`<div class="card" onclick="buyBiz('${b.id}')"><div class="card-name" style="color:var(--blue)">${b.icon} ${b.name}</div><div class="owned-badge">OWNED: ${s.owned}${pend}</div>${s.owned>0?`<div class="card-desc">Income: ${fmt(bizIncome(b))}/cycle</div>`:''}<div class="card-cost" style="color:${canAfford?'var(--g)':'var(--red)'}">${canAfford?'BUY':'NEED'}: ${fmt(cost)}</div><div class="biz-bar"><div class="biz-fill" id="fill-${b.id}" style="width:${Math.min(100,(s.progress||0)*100)}%"></div></div></div>`;
  }).join('');
}
function renderUpgrades(){
  document.getElementById('upg-grid').innerHTML=UPGRADES.map(u=>{
    const bought=gs.boughtUpgrades.includes(u.id),canAfford=gs.money>=u.cost;
    return`<div class="card${bought?' bought':''}" onclick="${bought?'':` buyUpgrade('${u.id}')`}"><div class="card-name" style="color:var(--amber)">${u.name}</div><div class="card-desc">${u.desc}</div><div class="card-cost" style="color:${bought?'var(--gd)':canAfford?'var(--g)':'var(--red)'}">${bought?'[INSTALLED]':(canAfford?'INSTALL: ':'NEED: ')+fmt(u.cost)}</div></div>`;
  }).join('');
}
function renderAll(){renderStats();renderBizGrid();renderUpgrades();}
const logEl=document.getElementById('log');
function log(msg,cls=''){const l=document.createElement('div');l.className='log-line '+cls;l.textContent=`[${new Date().toLocaleTimeString('en-US',{hour12:false})}] ${msg}`;logEl.prepend(l);while(logEl.children.length>30)logEl.removeChild(logEl.lastChild);}
function tickerUpdate(){
  const income=BUSINESSES.reduce((s,b)=>s+bizIncome(b),0);
  document.getElementById('ticker-text').textContent=['C:\\> BUSINESS TYCOON V1.2','Made by Metehan Ata.Als','BALANCE: '+fmt(gs.money),'INCOME/CYC: '+fmt(income),'CLICKS: '+gs.clicks,paused?'*** GAME PAUSED ***':'COMPETITOR.EXE DETECTED'].join('  >>>  ');
}
function bootGame(){
  load();renderAll();
  log('BOOT: BUSINESS TYCOON V1.2 READY','good');
  log('Welcome back, Tycoon!','warn');
  BUSINESSES.forEach(b=>{if(bizState[b.id].owned>0)startLoop(b);});
  setInterval(renderAll,500);setInterval(tickerUpdate,5000);tickerUpdate();
}
</script>

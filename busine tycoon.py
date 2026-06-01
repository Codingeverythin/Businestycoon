import streamlit as st

# Tasarım kodlarınızın Python tarafından hatasız okunmasını sağlıyoruz
st.markdown("""
<style>
  @import url('https://googleapis.com');
  :root{--g:#00ff41;--gd:#00aa2b;--gf:#003d0f;--gm:#00cc35;--amber:#ffb300;--red:#ff4444;--bg:#0a0f0a;--blue:#00cfff;--purple:#cc44ff;--pink:#ff44aa;}
  *{box-sizing:border-box;margin:0;padding:0;}
  .crt{font-family:'Share Tech Mono',monospace;background:var(--bg);color:var(--g);padding:16px;border:1px solid var(--gd);position:relative;min-height:520px;}
  .crt::before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,0.07) 2px,rgba(0,0,0,0.07) 4px);pointer-events:none;z-index:10;}
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
  .money-btn::before{content:'';position:absolute;inset:-2px;background:linear-gradient(90deg,transparent,rgba(0,255,65,0.08),transparent);animation:shimmer 2s linear infinite;}
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
  /* PANELS */
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
  .card-cost{font-size:11px;margin-top:4px;}
  .biz-bar{height:4px;background:#001205;border:1px solid var(--gd);margin-top:5px;overflow:hidden;border-radius:2px;}
  .biz-fill{height:100%;background:var(--gm);transition:width 0.2s;}
  .owned-badge{font-size:10px;color:var(--amber);}
  /* RESET POPUP */
  .popup-overlay{display:none;position:absolute;inset:0;background:rgba(0,0,0,0.82);z-index:50;align-items:center;justify-content:center;animation:fadeIn 0.15s ease;}
  .popup-overlay.open{display:flex;}
  .popup{background:#0a0f0a;border:2px solid var(--red);padding:24px;max-width:280px;width:90%;text-align:center;animation:popIn 0.2s ease;border-radius:4px;}
  @keyframes popIn{from{transform:scale(0.8);opacity:0;}to{transform:scale(1);opacity:1;}}
  .popup-icon{font-size:36px;margin-bottom:10px;}
  .popup-title{font-family:'VT323',monospace;font-size:26px;color:var(--red);letter-spacing:2px;margin-bottom:6px;}
  .popup-msg{font-size:11px;color:var(--gd);margin-bottom:16px;line-height:1.6;}
  .popup-btns{display:flex;gap:10px;justify-content:center;}
  /* SETTINGS */
  .set-row{display:flex;align-items:center;gap:12px;padding:10px 0;border-bottom:1px solid var(--gf);}
  .set-label{font-size:12px;color:var(--gd);min-width:120px;}
  .set-val{font-size:12px;color:var(--g);min-width:40px;text-align:right;}
  input[type=range]{flex:1;accent-color:var(--purple);cursor:pointer;}
  /* FLOAT */
  .float-label{position:fixed;pointer-events:none;font-family:'VT323',monospace;font-size:22px;color:var(--g);z-index:200;animation:floatUp 0.9s ease-out forwards;}
  @keyframes floatUp{0%{opacity:1;transform:translateY(0);}100%{opacity:0;transform:translateY(-60px);}}
  /* PAUSED BANNER */
  .paused-banner{display:none;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);z-index:15;font-family:'VT323',monospace;font-size:52px;color:var(--amber);letter-spacing:4px;pointer-events:none;animation:blinkPause 1s step-end infinite;}
  @keyframes blinkPause{50%{opacity:0;}}
  .paused-banner.show{display:block;}
  .ticker{font-size:10px;color:var(--gd);border-top:1px dashed var(--gf);padding-top:6px;margin-top:4px;overflow:hidden;white-space:nowrap;}
  .tick-inner{display:inline-block;animation:scroll 20s linear infinite;}
  @keyframes scroll{from{transform:translateX(100%);}to{transform:translateX(-100%);}}
  .section-title{color:var(--gd);font-size:11px;margin:4px 0;border-bottom:1px dashed var(--gf);padding-bottom:2px;}
</style>

<div class="crt" id="game">
  <h2 class="sr-only">Business Tycoon V1.2</h2>
  <div class="title">▓▒░ BUSINESS TYCOON V1.2 ░▒▓</div>
  <div class="paused-banner" id="paused-banner">⏸ PAUSED</div>
  <div class="stats-row" id="stats-row"></div>
  <button class="money-btn" onclick="clickMoney(event)">💰 CLICK FOR MONEY 💰</button>
  <div class="section-title">></div>
</div>
""", unsafe_allow_html=True)

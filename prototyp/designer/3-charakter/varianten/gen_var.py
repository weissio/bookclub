import random
OUT='/home/claude/bookclub/prototyp/designer/3-charakter/varianten/'
CUR=[('Salz und Asche','Jonas Brehm',142,384,'#3F6F8F','#E0637A'),
     ('Die Gezeitenkarte','Mira Olsen',38,296,'#7C6BB0','#F2B33D'),
     ('Kleine Geschichte der Stille','Ina Roth',61,220,'#4F8A6A','#FFD98A'),
     ('Das Haus am Moor','Clara Feld',12,340,'#B85A6E','#7FA1E2')]
# echte Cover-Farben der eigenen Bücher (Beispieldaten)
VOL={
 'gelesen':('Gelesen',148,'mit deinen Worten',['#4C69B8','#3F6F8F','#8A63A8','#4F8A6A','#C8607A','#D7A13A','#5A7FC4','#B85A6E','#6C73B0','#2F5D50','#E3C27A','#7C6BB0','#9C4F5E','#3B5A86','#C79A6B','#5E8C7A','#A86BB5','#4C69B8']),
 'ungelesen':('Ungelesen im Regal',61,'haben Zeit',['#D7A13A','#5A7FC4','#8A63A8','#E8D5B0','#3F6F8F','#C8607A','#4F8A6A','#B9A3D6','#2F5D50','#D98F5C','#6C73B0','#F0C060']),
 'wunsch':('Wunschliste',23,'irgendwann',['#C8607A','#7C6BB0','#E3C27A','#5A7FC4','#4F8A6A','#B85A6E','#9AB4DA']),
 'mehr':('Abgebrochen, Regale, Verliehen',13,'',['#B85A6E','#6C73B0','#4F8A6A','#D7A13A']),
}
def ink(hexc):
    v=int(hexc[1:],16); r,g,b=v>>16,(v>>8)&255,v&255
    return '#2A2440' if (0.299*r+0.587*g+0.114*b)>165 else '#FFFFFF'
def spines(colors,w,h,seed=1,lean=True):
    rnd=random.Random(seed); x=0; out=[]; i=0
    while True:
        bw=rnd.choice([9,10,11,12,13,14,16]); 
        if x+bw>w-2: break
        bh=round(h*rnd.uniform(.74,1.0)); c=colors[i%len(colors)]; i+=1
        out.append(f'<rect x="{x}" y="{h-bh}" width="{bw}" height="{bh}" rx="2" fill="{c}"/>'
                   f'<rect x="{x}" y="{h-bh}" width="{max(2,bw//4)}" height="{bh}" rx="1" fill="#fff" opacity=".16"/>'
                   f'<rect x="{x+2}" y="{h-bh+7}" width="{bw-4}" height="3" rx="1" fill="#fff" opacity=".35"/>')
        x+=bw+1
    if lean:
        c=colors[i%len(colors)]
        out.append(f'<rect x="{x+4}" y="{h-int(h*.86)}" width="11" height="{int(h*.86)}" rx="2" fill="{c}" transform="rotate(9 {x+4} {h})"/>')
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true" style="display:block">'+''.join(out)+'</svg>'
def openbook(c,page,w=120):
    cover,rib=c[4],c[5]; h=round(w*132/170)
    return f'''<span style="position:relative;display:block;width:{w}px;height:{h}px"><svg width="{w}" height="{h}" viewBox="0 0 170 132" aria-hidden="true" style="display:block">
<ellipse cx="85" cy="122" rx="78" ry="7" fill="#12152B" opacity=".45"/>
<path d="M4 18 Q44 8 85 16 Q126 8 166 18 L166 116 Q126 106 85 114 Q44 106 4 116 Z" fill="{cover}"/>
<path d="M9 14 Q46 4 85 13 L85 110 Q46 101 9 111 Z" fill="#FFF3DA"/><path d="M161 14 Q124 4 85 13 L85 110 Q124 101 161 111 Z" fill="#FFF8EA"/>
<path d="M70 12 Q78 12 85 13 L85 110 Q78 108 70 108 Z" fill="#E9D7B4" opacity=".7"/><path d="M85 13 Q92 12 100 12 L100 108 Q92 108 85 110 Z" fill="#F1E3C6" opacity=".6"/>
<g fill="#2A2440" opacity=".13"><rect x="18" y="26" width="50" height="3" rx="1.5"/><rect x="18" y="36" width="54" height="3" rx="1.5"/><rect x="18" y="46" width="46" height="3" rx="1.5"/><rect x="18" y="56" width="53" height="3" rx="1.5"/><rect x="18" y="66" width="40" height="3" rx="1.5"/><rect x="100" y="26" width="50" height="3" rx="1.5"/><rect x="100" y="36" width="44" height="3" rx="1.5"/></g>
<path d="M82 108 L82 130 L86 126 L90 130 L90 108 Z" fill="{rib}"/></svg>
<span style="position:absolute;right:{round(w*.12)}px;top:{round(h*.38)}px;display:flex;flex-direction:column;align-items:flex-end;font-size:{round(w*.16)}px;line-height:1;font-weight:900;color:#2A2440"><span style="font-size:.4em;font-weight:700;color:#8A7E9E">Seite</span>{page}</span></span>'''
def cover3d(c,w=52):
    h=round(w*1.4)
    return f'''<svg width="{w}" height="{h+6}" viewBox="0 0 52 79" aria-hidden="true" style="display:block;flex-shrink:0"><ellipse cx="27" cy="75" rx="23" ry="3.5" fill="#12152B" opacity=".5"/><path d="M10 4 L46 2 L49 4 L13 6 Z" fill="#FFF6E6"/><path d="M4 7 Q4 4 7 4 L13 6 L13 72 L7 70 Q4 70 4 67 Z" fill="{c}" opacity=".75"/><path d="M13 6 L46 3 Q50 3 50 7 L50 66 Q50 70 46 70 L13 72 Z" fill="{c}"/><path d="M17 10 Q17 8 20 8" stroke="#fff" stroke-width="2.5" stroke-linecap="round" fill="none" opacity=".35"/><rect x="19" y="22" width="25" height="16" rx="3" fill="#FFF3DA" opacity=".9"/></svg>'''
HEAD='''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=390"><title>Licht an – {title}</title>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@500;600;700;800;900&display=swap" rel="stylesheet">
<style>
:root{{--bg:#222746;--bg2:#1A1E39;--line:#353B69;--ink:#EEF0FA;--mute:#A9AED0;--acc:#FFD98A;--accBg:rgba(255,217,138,.10);--accLine:rgba(255,217,138,.5);--card:rgba(255,255,255,.045);--shadow:#12152B}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:390px;height:844px;background:var(--bg);overflow:hidden}}
body{{font-family:'Nunito',system-ui,sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased}}
button{{font:inherit;color:inherit;border:none;background:none;cursor:pointer;text-align:left}}
.phone{{position:relative;width:390px;height:844px;overflow:hidden;background:var(--bg)}}
.status{{position:absolute;top:0;left:0;right:0;height:54px;display:flex;align-items:center;justify-content:space-between;padding:0 30px 0 34px;font-weight:700;font-size:16px;z-index:5}}
.main{{position:absolute;top:54px;left:0;right:0;bottom:83px;display:flex;flex-direction:column;padding:8px 16px 10px;z-index:2}}
.kopf{{padding:0 6px;height:74px;flex-shrink:0}}
.kopf small{{display:block;font-size:13px;font-weight:700;color:var(--mute);letter-spacing:.02em}}
.kopf h1{{font-size:22px;line-height:28px;font-weight:900;letter-spacing:-.01em;margin-top:2px}}
.sec{{display:flex;justify-content:space-between;align-items:baseline;padding:0 6px;margin-bottom:8px}}
.sec h2{{font-size:16px;font-weight:900}} .sec span{{font-size:13px;font-weight:600;color:var(--mute)}}
.paket{{flex-shrink:0;height:56px;width:100%;border-radius:18px;background:var(--accBg);box-shadow:inset 0 0 0 1.5px var(--accLine);display:flex;align-items:center;gap:12px;padding:0 14px}}
.paket b{{display:block;font-size:15px;font-weight:800;color:var(--acc)}} .paket i{{display:block;font-style:normal;font-size:12.5px;font-weight:600;color:var(--mute)}}
.vermerk{{flex-shrink:0;margin-top:8px;padding:0 6px;font-size:12.5px;font-weight:600;color:var(--mute);display:flex;justify-content:space-between;align-items:center;height:20px}}
.bsp{{font-size:10px;font-weight:800;letter-spacing:.05em;border:1px solid var(--line);border-radius:6px;padding:0 5px}}
.tabs{{position:absolute;left:0;right:0;bottom:0;height:83px;background:var(--bg2);border-top:1px solid #2F3561;display:flex;padding:0 6px 34px;z-index:4}}
.tab{{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;font-size:10.5px;font-weight:700;color:#8C91B6}} .tab.on{{color:var(--acc)}}
.home{{position:absolute;bottom:8px;left:128px;width:134px;height:5px;border-radius:3px;background:#E9EBF7;z-index:6}}
{css}
</style></head><body><div class="phone">
<svg width="390" height="844" viewBox="0 0 390 844" aria-hidden="true" style="position:absolute;inset:0;z-index:1">
<defs><radialGradient id="kegel" cx="300" cy="118" r="{cone}" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFD98A" stop-opacity=".26"/><stop offset=".6" stop-color="#FFD98A" stop-opacity=".07"/><stop offset="1" stop-color="#FFD98A" stop-opacity="0"/></radialGradient>
<linearGradient id="schirm" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFCF62"/><stop offset="1" stop-color="#D9921E"/></linearGradient></defs>
<path d="M268 106 L328 106 L520 {coneY} L-130 {coneY} Z" fill="url(#kegel)"/>
<path d="M300 54 L300 72" stroke="#5A608F" stroke-width="2"/>
<g transform="rotate(-8 300 92)"><path d="M280 102 C280 80 289 72 300 72 C311 72 320 80 320 102 Z" fill="url(#schirm)"/><path d="M287 88 C289 80 294 76 299 75" stroke="#FFF0C4" stroke-width="3" stroke-linecap="round" fill="none" opacity=".8"/><ellipse cx="300" cy="102" rx="20" ry="4.5" fill="#B87412"/><ellipse cx="300" cy="103" rx="9" ry="3.5" fill="#FFF6D8"/><path d="M313 102 L313 118" stroke="#8A8FB8" stroke-width="1.4" stroke-dasharray="2 2"/><circle cx="313" cy="122" r="4" fill="#C9CCE6"/></g>
</svg>
<div class="status"><span>21:47</span><span style="display:flex;gap:6px;align-items:center"><svg width="18" height="12" viewBox="0 0 18 12"><rect x="0" y="8" width="3" height="4" rx="1" fill="#EEF0FA"/><rect x="5" y="5" width="3" height="7" rx="1" fill="#EEF0FA"/><rect x="10" y="2.5" width="3" height="9.5" rx="1" fill="#EEF0FA"/><rect x="15" y="0" width="3" height="12" rx="1" fill="#EEF0FA"/></svg><svg width="26" height="12" viewBox="0 0 26 12"><rect x=".5" y=".5" width="22" height="11" rx="3.5" stroke="#EEF0FA" fill="none" opacity=".5"/><rect x="2" y="2" width="15" height="8" rx="2" fill="#EEF0FA"/></svg></span></div>
<main class="main">
<div class="kopf"><small>Bibliothek</small><h1>Das Licht ist noch an.</h1></div>
'''
PAKET='''<button class="paket" aria-label="Neue Bücher auspacken: scannen, ISBN oder von Hand"><svg width="40" height="34" viewBox="0 6 60 46" aria-hidden="true"><path d="M10 24 L50 24 L48 48 L12 48 Z" fill="#C9955A"/><path d="M10 24 L2 15 L24 15 L30 24 Z" fill="#E2B57C"/><path d="M50 24 L58 15 L36 15 L30 24 Z" fill="#D9A86C"/><rect x="26" y="30" width="8" height="18" fill="#E9C996" opacity=".8"/></svg><span style="flex:1"><b>Neue Bücher auspacken</b><i>Scannen, ISBN oder von Hand</i></span><svg width="22" height="22" viewBox="0 0 22 22" aria-hidden="true"><circle cx="11" cy="11" r="10" fill="#FFD98A"/><path d="M11 6.5v9M6.5 11h9" stroke="#2A2440" stroke-width="2.2" stroke-linecap="round"/></svg></button>'''
TAIL='''<div class="vermerk"><span>240 Bücher · gesammelt seit März 2025</span><span class="bsp">BEISPIELDATEN</span></div>
</main>
<nav class="tabs">
<div class="tab on"><svg width="26" height="24" viewBox="0 0 26 24"><rect x="3" y="4" width="5" height="17" rx="1.6" fill="#FFD98A"/><rect x="10" y="2" width="5" height="19" rx="1.6" fill="#FFD98A"/><rect x="17.5" y="5" width="5" height="16" rx="1.6" fill="#FFD98A" transform="rotate(10 20 13)"/></svg>Bibliothek</div>
<div class="tab"><svg width="26" height="24" viewBox="0 0 26 24"><rect x="3" y="4" width="20" height="16" rx="3" fill="none" stroke="#8C91B6" stroke-width="2"/><path d="M13 4 V20 M3 12 H23" stroke="#8C91B6" stroke-width="2"/></svg>Schaufenster</div>
<div class="tab"><svg width="26" height="24" viewBox="0 0 26 24"><circle cx="13" cy="12" r="9" fill="none" stroke="#8C91B6" stroke-width="2"/><path d="M16.5 8.5 L14.5 14.5 L9.5 15.5 L11.5 9.5 Z" fill="#8C91B6"/></svg>Entdecken</div>
<div class="tab"><svg width="26" height="24" viewBox="0 0 26 24"><circle cx="13" cy="9" r="4.5" fill="none" stroke="#8C91B6" stroke-width="2"/><path d="M5 21 C6 16 9.5 14.5 13 14.5 C16.5 14.5 20 16 21 21" fill="none" stroke="#8C91B6" stroke-width="2" stroke-linecap="round"/></svg>Ich</div>
</nav><div class="home"></div></div></body></html>'''
WORD={2:'Zwei',4:'Vier'}
def bm():
    return '<svg width="12" height="14" viewBox="0 0 14 16" aria-hidden="true"><path d="M2 1h10v14l-5-4-5 4z" fill="none" stroke="#FFD98A" stroke-width="2.2" stroke-linejoin="round"/></svg>'

# ---------- V1: Leselicht-Leiste + 2x2 Regalfächer ----------
def v1(n):
    css='''.strip{display:flex;gap:10px;overflow:hidden;margin:0 -16px;padding:0 16px}
.ob{flex-shrink:0;width:122px;display:flex;flex-direction:column;align-items:center}
.ob .t{margin-top:4px;font-size:13px;font-weight:800;line-height:16px;text-align:center;width:122px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ob .p{margin-top:5px;height:36px;padding:0 12px;border-radius:18px;border:1.5px solid var(--accLine);background:var(--accBg);color:var(--acc);font-size:13px;font-weight:800;display:flex;align-items:center;gap:6px}
.fach{display:grid;grid-template-columns:1fr 1fr;gap:10px;flex:1;min-height:0;margin-bottom:10px}
.f{border-radius:20px;background:var(--card);box-shadow:inset 0 0 0 1px rgba(255,255,255,.06);padding:14px 14px 0;display:flex;flex-direction:column;overflow:hidden}
.f b{font-size:16px;font-weight:900;line-height:20px} .f em{font-style:normal;font-size:13px;font-weight:700;color:var(--mute);margin-top:2px}
.f .n{font-size:28px;font-weight:900;line-height:1;margin-top:8px;font-variant-numeric:tabular-nums}
.f .reg{margin-top:auto;border-bottom:4px solid #3A4072;margin-left:-2px;margin-right:-2px}
.mehr{display:flex;flex-direction:column;gap:3px;margin-top:8px;font-size:14px;font-weight:700}
.mehr span{display:flex;justify-content:space-between;color:var(--ink)} .mehr span i{font-style:normal;color:var(--mute)}'''
    cards=''
    for c in CUR[:n]:
        cards+=f'<div class="ob"><button aria-label="{c[0]}, Seite {c[2]}, Seite eintragen">{openbook(c,c[2],116)}</button><div class="t">{c[0]}</div><button class="p">{bm()}Eintragen</button></div>'
    lesen=f'<section id="amlesen"><div class="sec"><h2>Am Lesen</h2><span>{WORD[n]} Bücher offen{" · wischen" if n>2 else ""}</span></div><div class="strip">{cards}</div></section>'
    def fach(k,seed):
        name,cnt,q,cols=VOL[k]
        return f'<button class="f" aria-label="{name}, {cnt} Bücher"><span class="n" style="margin:0 0 6px">{cnt}</span><b>{name}</b><em>{q}</em><div class="reg">{spines(cols,150,46 if n==2 else 34,seed)}</div></button>'
    mehr='<button class="f" aria-label="Weitere Bände"><b>Weitere Bände</b><div class="mehr"><span>Abgebrochen <i>6</i></span><span>Eigene Regale <i>5</i></span><span>Verliehen <i>2</i></span><span>Rückblick <i>›</i></span></div></button>'
    lib=f'<div class="sec" style="margin-top:14px"><h2>Im Regal</h2><span>240 Bücher</span></div><div class="fach">{fach("gelesen",3)}{fach("ungelesen",5)}{fach("wunsch",7)}{mehr}</div>'
    return HEAD.format(title='V1',css=css,cone=320,coneY=450)+lesen+lib+PAKET+TAIL
# ---------- V2: Zeilen am Lesen + Regalbretter aus eigenen Rücken ----------
def v2(n):
    css='''.rows{display:flex;flex-direction:column;gap:6px}
.r{display:flex;align-items:center;gap:12px;height:54px;padding:0 6px 0 4px;border-radius:16px;background:rgba(255,217,138,.07)}
.sp{width:16px;height:42px;border-radius:3px;flex-shrink:0;box-shadow:inset 3px 0 0 rgba(255,255,255,.18)}
.r .x{flex:1;min-width:0;display:flex;flex-direction:column} .r .x b{font-size:15px;font-weight:800;white-space:nowrap;overflow:hidden;text-overflow:ellipsis} .r .x i{font-style:normal;font-size:12.5px;font-weight:600;color:var(--mute)}
.pg{flex-shrink:0;height:44px;min-width:92px;padding:0 12px;border-radius:22px;border:1.5px solid var(--accLine);color:var(--acc);font-size:14px;font-weight:800;display:flex;align-items:center;justify-content:center;gap:6px;font-variant-numeric:tabular-nums}
.bretter{flex:1;min-height:0;display:flex;flex-direction:column;gap:8px;margin-bottom:10px}
.brett{flex:1;min-height:0;position:relative;display:flex;align-items:flex-end;justify-content:space-between;padding:0 12px;border-radius:16px;background:var(--card);overflow:hidden}
.brett::after{content:"";position:absolute;left:0;right:0;bottom:0;height:5px;background:#3A4072}
.brett .lab{position:relative;z-index:2;align-self:center;display:flex;flex-direction:column;padding-right:8px}
.brett .lab b{font-size:17px;font-weight:900;line-height:20px} .brett .lab i{font-style:normal;font-size:13px;font-weight:700;color:var(--mute)}
.brett .rs{position:relative;z-index:1;margin-bottom:5px}'''
    rows=''
    for c in CUR[:n]:
        rows+=f'<div class="r"><span class="sp" style="background:{c[4]}"></span><span class="x"><b>{c[0]}</b><i>{c[1]} · von {c[3]}</i></span><button class="pg" aria-label="{c[0]}: Seite {c[2]}, neue Seite eintragen">{bm()}S. {c[2]}</button></div>'
    lesen=f'<section id="amlesen"><div class="sec"><h2>Am Lesen</h2><span>{WORD[n]} Bücher offen</span></div><div class="rows">{rows}</div></section>'
    hb=52 if n==2 else 40
    def brett(k,seed,label=None,sub=None):
        name,cnt,q,cols=VOL[k]
        return f'<button class="brett" aria-label="{label or name}"><span class="lab"><b>{label or name}</b><i>{sub or (str(cnt)+" · "+q)}</i></span><span class="rs">{spines(cols,128,hb,seed)}</span></button>'
    lib=f'<div class="sec" style="margin-top:16px"><h2>Im Regal</h2><span>240 Bücher</span></div><div class="bretter">{brett("gelesen",3,sub="148 Bücher")}{brett("ungelesen",5,sub="61 · haben Zeit")}{brett("wunsch",7,sub="23 · irgendwann")}{brett("mehr",9,label="Weitere Bände",sub="Abgebrochen, Regale, Verliehen")}</div>'
    return HEAD.format(title='V2',css=css,cone=320,coneY=450)+lesen+lib+PAKET+TAIL
# ---------- V3: ein Buch im Licht + Liste mit Cover-Fächern ----------
def v3(n):
    css='''.pult{border-radius:22px;background:rgba(255,217,138,.08);box-shadow:inset 0 0 0 1px rgba(255,217,138,.16);padding:12px 12px 10px}
.top{display:flex;align-items:center;gap:14px}
.top .x{flex:1;min-width:0} .top b{display:block;font-size:17px;font-weight:900;line-height:21px} .top i{display:block;font-style:normal;font-size:13px;font-weight:600;color:var(--mute)}
.top .s{display:block;margin-top:4px;font-size:13px;font-weight:800;color:var(--acc)}
.pg{flex-shrink:0;height:48px;padding:0 16px;border-radius:24px;background:var(--acc);color:#2A2440;font-size:15px;font-weight:900;display:flex;align-items:center;gap:7px;white-space:nowrap}
.auch{display:flex;gap:6px;margin-top:10px;align-items:center;overflow:hidden}
.auch small{font-size:12px;font-weight:700;color:var(--mute);flex-shrink:0;margin-right:2px}
.chip{flex-shrink:1;min-width:0;height:44px;display:flex;align-items:center;gap:8px;padding:0 12px 0 8px;border-radius:14px;background:rgba(255,255,255,.06);font-size:13px;font-weight:800;max-width:170px}
.chip span.c{width:8px;height:26px;border-radius:2px;flex-shrink:0} .chip em{font-style:normal;white-space:nowrap;overflow:hidden;text-overflow:ellipsis} .chip u{text-decoration:none;color:var(--acc);flex-shrink:0}
.liste{flex:1;min-height:0;display:flex;flex-direction:column;margin-bottom:10px}
.z{flex:1;min-height:60px;display:flex;align-items:center;gap:16px;padding:0 6px;border-bottom:1px solid #2F3561;width:100%}
.z:last-child{border-bottom:none}
.fan{position:relative;width:74px;height:56px;flex-shrink:0}
.fan span{position:absolute;bottom:0;width:36px;height:52px;border-radius:3px 5px 5px 3px;box-shadow:0 3px 6px rgba(10,12,30,.4), inset 4px 0 0 rgba(0,0,0,.15)}
.fan span::after{content:"";position:absolute;left:10px;right:5px;top:12px;height:10px;border-radius:2px;background:#FFF3DA;opacity:.85}
.z .x{flex:1} .z b{display:block;font-size:18px;font-weight:900;line-height:22px} .z i{display:block;font-style:normal;font-size:13px;font-weight:600;color:var(--mute)}
.z .n{font-size:20px;font-weight:900;font-variant-numeric:tabular-nums}'''
    c=CUR[0]
    chips=''.join(f'<button class="chip" aria-label="{x[0]}, Seite {x[2]}, ins Licht legen"><span class="c" style="background:{x[4]}"></span><em>{x[0]}</em><u>{x[2]}</u></button>' for x in CUR[1:n])
    lesen=f'''<section id="amlesen"><div class="sec"><h2>Im Licht</h2><span>{WORD[n]} Bücher am Lesen</span></div><div class="pult">
<div class="top">{cover3d(c[4],46)}<span class="x"><b>{c[0]}</b><i>{c[1]}</i><span class="s">Lesebändchen auf Seite {c[2]} von {c[3]}</span></span></div>
<div class="auch"><button class="pg" style="flex:1;justify-content:center">{'<svg width="13" height="15" viewBox="0 0 14 16" aria-hidden="true"><path d="M2 1h10v14l-5-4-5 4z" fill="none" stroke="#2A2440" stroke-width="2.2" stroke-linejoin="round"/></svg>'}Seite eintragen</button>{chips if n==2 else ''}</div>
{'<div class="auch"><small>Daneben</small>'+chips+'</div>' if n>2 else ''}
</div></section>'''
    def fan(cols):
        return '<span class="fan">'+''.join(f'<span style="left:{i*19}px;background:{col};transform:rotate({[-6,0,5][i]}deg);z-index:{i}"></span>' for i,col in enumerate(cols[:3]))+'</span>'
    def z(name,sub,cnt,cols): return f'<button class="z" aria-label="{name}, {cnt}">{fan(cols)}<span class="x"><b>{name}</b><i>{sub}</i></span><span class="n">{cnt}</span></button>'
    lib=f'''<div class="sec" style="margin-top:16px"><h2>Im Regal</h2><span>240 Bücher</span></div><div class="liste">
{z("Gelesen","zuletzt: Die Uhrmacherin","148",VOL["gelesen"][3])}{z("Ungelesen im Regal","haben Zeit","61",VOL["ungelesen"][3])}{z("Wunschliste","irgendwann","23",VOL["wunsch"][3])}{z("Abgebrochen und mehr","Regale, Verliehen, Rückblick","13",["#B85A6E","#6C73B0","#4F8A6A"])}</div>'''
    return HEAD.format(title='V3',css=css,cone=320,coneY=450)+lesen+lib+PAKET+TAIL
for name,f in [('v1',v1),('v2',v2),('v3',v3)]:
    open(OUT+name+'.html','w').write(f(2))
    open(OUT+name+'-4buecher.html','w').write(f(4))
print('ok')

"""Generate both static language versions. Run: python3 tools/build.py."""
from pathlib import Path
from html import escape
import os
import hashlib
from content import UI, PROJECTS, PROJECT_META
ROOT = Path(__file__).resolve().parents[1]
ASSET_VERSIONS = {name: hashlib.sha256((ROOT/'assets'/name).read_bytes()).hexdigest()[:12] for name in ['style.css','app.js']}

def relative(target, route):
    return os.path.relpath(ROOT / target, (ROOT / route).parent).replace(os.sep, '/')

def local_route(lang, name):
    return ('zh/' if lang == 'zh' else '') + name

def head(title, description, route, lang):
    prefix = relative('assets', route) + '/'
    language = 'zh-CN' if lang == 'zh' else 'en'
    alternate = route[3:] if lang == 'zh' else 'zh/' + route
    return f'''<!doctype html><html lang="{language}" data-route="{route}" data-language="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="dark"><title>{escape(title)}</title><meta name="description" content="{escape(description, quote=True)}"><link rel="alternate" hreflang="{'en' if lang=='zh' else 'zh-CN'}" href="{relative(alternate,route)}"><link rel="icon" type="image/svg+xml" href="{prefix}favicon.svg"><link rel="stylesheet" href="{prefix}style.css?v={ASSET_VERSIONS['style.css']}"><script src="{prefix}app.js?v={ASSET_VERSIONS['app.js']}" defer></script></head><body><a class="skip" href="#main">{UI[lang]['skip']}</a>'''

def header(route, lang):
    u=UI[lang]; home=relative(local_route(lang,'index.html'),route)
    en=route[3:] if lang=='zh' else route; zh='zh/'+en
    switch=''.join(f'<a href="{relative(target,route)}" data-set-language="{key}" lang="{key if key=="en" else "zh-CN"}" hreflang="{key if key=="en" else "zh-CN"}" aria-label="{label}"'+(' aria-current="true"' if key==lang else '')+f'>{text}</a>' for key,target,text,label in [('en',en,'EN','English'),('zh',zh,'中文','简体中文')])
    return f'''<header><div class="wrap"><a class="brand" href="{home}" aria-label="Merci">Merci<span>.</span></a><div class="header-right"><nav aria-label="{u['nav']}"><a href="{home}#work">{u['work']}</a><a href="{home}#about">{u['about']}</a><a href="{home}#contact">{u['contact']}</a></nav><div class="language-switch" role="group" aria-label="{u['language']}">{switch}</div></div></div></header>'''

def footer(lang):
    u=UI[lang]
    return f'''<footer><div class="wrap"><span>{u['footer']}</span><div class="footer-links"><a href="https://github.com/hyandnn">GitHub</a><a href="mailto:haoling.yang@rwth-aachen.de">{u['email']}</a></div></div></footer></body></html>'''

def paragraphs(texts):
    return ''.join('<p>'+p+'</p>' for p in texts)

def controls(lang, layers):
    u=UI[lang]
    layer_html=''.join(f'<label><input type="checkbox" data-layer="{key}" checked>{u[label]}</label>' for key,label in layers)
    return f'''<div class="demo-controls"><button type="button" data-play>{u['play']}</button><label class="timeline"><input type="range" min="0" max="1000" value="0" data-time aria-label="{u['time']}"><output data-time-label>0.0 s</output></label>{f'<div class="layers" aria-label="{u["layers"]}">{layer_html}</div>' if layer_html else ''}</div>'''

def demo(p, lang):
    u=UI[lang];slug=p['slug']
    if slug in ('stereo','lidar'):
        content=f'<canvas data-scene="{slug}" role="img" aria-label="{escape(p["caption"])}"></canvas>'
        layers=[('points','points'),('geometry','geometry')] if slug=='stereo' else [('points','returns'),('rays','rays'),('tracks','tracks')]
    else:
        content='<div class="phase-grid">'
        for i,(title,description) in enumerate(p['panels']):
            content+=f'<figure class="phase"><canvas data-scene="{slug}" data-panel="{i}" role="img" aria-label="{escape(description)}"></canvas><figcaption><h3>{title}</h3><p>{description}</p></figcaption></figure>'
        content+='</div>';layers=[]
    return f'''<div class="demo" data-demo="{slug}"><div class="demo-head"><span>{u['demo']}</span><span>{u['synthetic']}</span></div>{content}{controls(lang,layers)}<p class="demo-caption">{p['caption']}</p></div>'''

def functional_view(p,lang):
    if p['slug']=='motion':
        nodes={key:(title,desc) for key,title,desc in p['research_nodes']}
        def node(key):
            title,desc=nodes[key]
            return f'<div class="research-node" data-research-node="{key}"><h3>{title}</h3><p>{desc}</p></div>'
        badge='Pipeline designed & implemented' if lang=='en' else '流程设计与实现'
        wall='Wall-reference observations' if lang=='en' else '墙面参考观测'
        athlete='Athlete observations' if lang=='en' else '攀岩者观测'
        return f'''<figure class="research-map" aria-label="{p['system_title']}"><figcaption class="map-caption"><span>{badge}</span></figcaption><div class="research-source">{node('video')}</div><div class="research-branches"><div class="research-path"><span class="path-label">{wall}</span>{node('holds')}{node('matching')}</div><div class="research-path"><span class="path-label">{athlete}</span>{node('pose')}</div></div><div class="research-merge">{node('mapping')}</div><div class="research-output">{node('analysis')}</div></figure>'''
    groups=''
    for i,(title,scope,nodes) in enumerate(p['groups']):
        groups+=f'<div class="capability-group'+(' supporting' if i in (0,3) else '')+f'"><div class="group-heading"><h3>{title}</h3><span class="scope-badge">{scope}</span></div><ul>'+''.join(f'<li>{label}</li>' for label in nodes)+'</ul></div>'
    return f'<div class="capability-board" role="group" aria-label="{p["system_title"]}">{groups}</div>'

def height_view(lang):
    en=lang=='en'
    title='A footprint does not show the full height structure.' if en else '平面投影不能表达完整的高度结构。'
    intro='Two illustrative structures share a similar plan-view footprint but occupy different heights.' if en else '两组示意结构具有相近的俯视投影，却分布在不同高度。'
    grid=''.join(f'<path d="M {x} 22 V 204"/>' for x in range(30,381,35))+''.join(f'<path d="M 20 {y} H 390"/>' for y in range(29,205,35))
    top_points=''.join(f'<circle cx="{125+(i%9)*20}" cy="{65+(i//9)*20}" r="3.1" fill="'+('#62e4d2' if i%2==0 else '#f3bf77')+'"/>' for i in range(45))
    side_points=''.join(f'<circle cx="{125+i*20}" cy="{y+(i%3-1)*5}" r="3.1" fill="{color}"/>' for y,color in [(174,'#62e4d2'),(62,'#f3bf77')] for i in range(9))
    top=f'<svg viewBox="0 0 410 225" role="img" aria-label="'+('Overlapping plan-view footprints' if en else '相近的平面投影')+f'"><g stroke="#253644" stroke-width="1">{grid}</g><rect x="109" y="48" width="194" height="116" rx="3" fill="#85bbff0d" stroke="#85bbff" stroke-dasharray="5 5"/>{top_points}</svg>'
    ground='Ground' if en else '地面'
    height='Height' if en else '高度'
    side=f'<svg viewBox="0 0 410 245" role="img" aria-label="'+('Different vertical distributions above ground; height increases upward' if en else '地面以上的不同高度分布；向上为高度方向')+f'"><g stroke="#253644" stroke-width="1">{grid}</g><path d="M 40 194 H 374" stroke="#879cac" stroke-width="1.5"/><path d="M 54 178 V 56 M 48 65 L 54 56 L 60 65" fill="none" stroke="#a2b1bf" stroke-width="1.5"/><text x="68" y="111" fill="#bcc8d3" font-size="16">{height}</text><text x="329" y="219" fill="#bcc8d3" font-size="16">{ground}</text><rect x="109" y="47" width="194" height="142" rx="3" fill="#85bbff08" stroke="#486779" stroke-dasharray="5 5"/>{side_points}</svg>'
    a='Plan view · overlapping footprint' if en else '俯视 · 相近投影'
    b='Side view · different heights' if en else '侧视 · 不同高度'
    legend='Cyan and amber identify two independent illustrative structures.' if en else '青色与橙黄色分别表示两组独立的示意结构。'
    return f'<aside class="height-study"><div><h3>{title}</h3><p>{intro}</p></div><div class="height-grid"><figure>{top}<figcaption>{a}</figcaption></figure><figure>{side}<figcaption>{b}</figcaption></figure></div><p class="height-legend">{legend}</p></aside>'

def story(index,label,title,content,anchor='',intro=''):
    """One chapter layout for prose, functional views, contributions and scenes."""
    introduction=f'<p>{intro}</p>' if intro else ''
    return f'<section class="case-section"'+(f' id="{anchor}"' if anchor else '')+f'><div class="section-heading"><span class="story-index">{index:02d} / {label}</span><h2>{title}</h2>{introduction}</div><div class="section-content">{content}</div></section>'

for lang in ['en','zh']:
    u=UI[lang]
    projects=[]
    for meta,source in zip(PROJECT_META,PROJECTS[lang]):
        p=dict(source);p.update(slug=meta[0],number=meta[1],theme=meta[2]);projects.append(p)
    route=local_route(lang,'index.html')
    cards=''
    for p in projects:
        cards+=f'''<a class="project-card {p['theme']}" href="projects/{p['slug']}.html"><div class="card-view"><canvas data-scene="{p['slug']}-cover" data-preview="true" role="img" aria-label="{escape(p['summary'])}"></canvas></div><div class="card-copy"><div class="card-heading"><span class="index">{p['number']}</span><h3>{p['name']}</h3></div><p>{p['summary']}</p><div class="card-foot"><span class="mono">{p['topic']}</span><span>{u['read']}</span></div></div></a>'''
    tools=''.join(f'<div><b>{name}</b><p>{desc}</p></div>' for name,desc in u['toolkit'])
    home=head('Merci — '+u['hero_role'],u['about_p1'],route,lang)+header(route,lang)
    home+=f'''<main id="main"><section class="hero" aria-labelledby="hero-title"><div><div class="eyebrow">{u['hero_role']}</div><h1 id="hero-title">{u['hero_title']}</h1><p class="intro">{u['hero_intro']}</p><div class="hero-actions"><a class="primary-link" href="#work">{u['explore']}</a><a class="text-link secondary-link" href="https://github.com/hyandnn">{u['github']}</a></div></div><div class="hero-visual"><div class="visual-top"><span>{u['hero_visual']}</span><span>{u['synthetic']}</span></div><canvas data-scene="hero" role="img" aria-label="{u['hero_visual']}"></canvas><div class="visual-bottom"><span>{u['hero_bottom']}</span></div></div></section><div class="info-strip">{''.join('<span>'+s+'</span>' for s in u['strip'])}</div><section id="work" aria-labelledby="work-title"><div class="section-top"><div><div class="eyebrow">{u['selected']}</div><h2 id="work-title">{u['work_title']}</h2></div><p>{u['work_intro']}</p></div><div class="work-grid">{cards}</div><p class="notice">{u['notice']}</p></section><section class="about" id="about" aria-labelledby="about-title"><div><div class="eyebrow">{u['about']} / Merci</div><h2 id="about-title">{u['about_title']}</h2></div><div class="about-text"><p>{u['about_p1']}</p><p>{u['about_p2']}</p><div class="toolkit">{tools}</div><p class="additional">{u['about_extra']}</p></div></section><section class="contact" id="contact" aria-labelledby="contact-title"><div><div class="eyebrow">{u['contact']}</div><h2 id="contact-title">{u['contact_title']}</h2><p>{u['contact_copy']}</p></div><a class="text-link" href="mailto:haoling.yang@rwth-aachen.de">haoling.yang@rwth-aachen.de</a></section></main>'''+footer(lang)
    (ROOT/route).parent.mkdir(parents=True,exist_ok=True);(ROOT/route).write_text(home)
    for i,p in enumerate(projects):
        route=local_route(lang,'projects/'+p['slug']+'.html')
        home=relative(local_route(lang,'index.html'),route)
        page=head(p['name']+' — Merci',p['summary'],route,lang)+header(route,lang)
        contributions_label='My contribution' if lang=='en' else '我的贡献'
        explore_label='Concept illustration' if lang=='en' else '概念示意'
        limits_label='Technical boundaries' if lang=='en' else '技术边界'
        page+=f'''<main id="main" class="{p['theme']}"><a class="back" href="{home}#work">{u['back']}</a><section class="case-head"><div class="eyebrow">{p['number']} / {p['name']}</div><h1>{p['title']}</h1><p class="lead">{p['lead']}</p><div class="case-meta"><div><span class="label">{u['role']}</span><p>{p['role']}</p></div><div><span class="label">{u['context']}</span><p>{p['context']}</p></div></div><nav class="case-jumps" aria-label="{'Case sections' if lang=='en' else '案例章节'}"><a href="#system">{u['method']}</a><a href="#contribution">{contributions_label}</a><a href="#illustration">{explore_label}</a><a href="#outcome">{u['result']}</a></nav></section>'''
        page+=story(1,u['problem'],p['overview_title'],paragraphs(p['overview']))
        page+=story(2,u['method'],p['system_title'],functional_view(p,lang),'system',p['system_intro'])
        contributions='<div class="contribution-grid">'+''.join(f'<article class="contribution"><span class="contribution-role">{role}</span><h3>{title}</h3><p>{copy}</p></article>' for title,role,copy in p['contributions'])+'</div>'
        page+=story(3,contributions_label,p['contribution_title'],contributions,'contribution')
        choices='<div class="decision-grid">'+''.join(f'<div class="decision"><h3>{title}</h3><p>{copy}</p></div>' for title,copy in p['choices'])+'</div>'
        if p['slug']=='lidar':choices+=height_view(lang)
        page+=story(4,u['choices'],p['choices_title'],choices)
        page+=story(5,explore_label,p['demo_title'],demo(p,lang),'illustration',p['demo_intro'])
        page+=story(6,u['result'],p['result_title'],paragraphs(p['result'])+f'<div class="technical-boundary"><h3>{limits_label}</h3><p>{p["limits"]}</p></div>','outcome')
        page+=f'<p class="notice case-notice">{u["notice"]}</p>'
        prev,nxt=projects[(i-1)%4],projects[(i+1)%4]
        page+=f'''<div class="case-nav"><div><small>{u['previous']}</small><a href="{prev['slug']}.html">{prev['name']}</a></div><div><small>{u['next']}</small><a href="{nxt['slug']}.html">{nxt['name']}</a></div></div></main>'''+footer(lang)
        (ROOT/route).parent.mkdir(parents=True,exist_ok=True);(ROOT/route).write_text(page)
    route=local_route(lang,'404.html')
    (ROOT/route).write_text(head('404 — Merci',u['notfound'],route,lang)+header(route,lang)+f'<main id="main" class="empty-page"><div class="eyebrow">404</div><h1>{u["notfound"]}</h1><a class="text-link" href="index.html">{u["return"]}</a></main>'+footer(lang))
print('Built 12 static pages: 2 languages × (homepage, four cases, 404).')

// Behavior checks against the actual app, using a small DOM shim and native canvas.
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const {createCanvas}=require('@napi-rs/canvas');
const app=fs.readFileSync(path.join(path.resolve(process.argv[2]||'.'),'assets/app.js'),'utf8');
function assert(v,m){if(!v)throw new Error(m);}
class Element{constructor(){this.listeners={};this.attributes={};this.dataset={};this.value='0';}addEventListener(n,fn){(this.listeners[n]||=[]).push(fn);}emit(n){for(const fn of this.listeners[n]||[])fn({});}setAttribute(k,v){this.attributes[k]=v;}getAttribute(k){return this.attributes[k];}}
function run(language,saved=null,route='/projects/motion.html',hash=''){
 const button=new Element(),range=new Element(),output=new Element(),demo=new Element();
 demo.querySelector=s=>({'[data-play]':button,'[data-time]':range,'[data-time-label]':output}[s]);demo.querySelectorAll=()=>[];
 const canvases=[0,1,2].map(panel=>{const c=createCanvas(348,325);c.dataset={scene:'motion',panel:String(panel)};c.closest=()=>demo;c.getBoundingClientRect=()=>({width:348,height:325});return c;});
 const links=['en','zh'].map(lang=>{const a=new Element();a.dataset.setLanguage=lang;a.attributes.href=route==='/'?(lang==='en'?'index.html':'zh/index.html'):(lang==='en'?'../projects/motion.html':'../zh/projects/motion.html');a.href=a.attributes.href;return a;});
 const document={documentElement:{dataset:{language}},URL:'https://hyandnn.github.io'+route,hidden:false,querySelectorAll:s=>({'[data-set-language]':links,'[data-demo]':[demo],'canvas[data-scene]':canvases}[s]||[])};
 let savedLanguage=saved,assigned=null,raf=null,reduce=null;
 const window={devicePixelRatio:1,matchMedia:()=>({matches:false,addEventListener:(n,fn)=>reduce=fn}),location:{pathname:route,search:'',hash,assign:x=>assigned=x}};window.parent=window;
 const ctx={document,window,localStorage:{getItem:()=>savedLanguage,setItem:(k,v)=>savedLanguage=v},ResizeObserver:class{observe(){}},IntersectionObserver:class{observe(){}},requestAnimationFrame:fn=>raf=fn};
 vm.createContext(ctx);vm.runInContext(app,ctx);
 assert(button.textContent===(language==='zh'?'播放':'Play'),'Localized initial control');
 range.value='400';range.emit('input');assert(output.textContent==='4.8 s','Scrubbed time');
 const paused=canvases.map(c=>c.toBuffer('image/png'));
 button.emit('click');assert(button.textContent===(language==='zh'?'暂停':'Pause'),'Localized playing control');raf(1000);raf(1040);
 assert(Number(range.value)>400,'Playback did not advance');
 for(let i=0;i<3;i++)assert(!paused[i].equals(canvases[i].toBuffer('image/png')),'Phase panel did not follow shared clock');
 reduce({matches:true});assert(button.textContent===(language==='zh'?'播放':'Play'),'Reduced-motion change did not pause');
 range.value='1000';range.emit('input');button.emit('click');assert(Number(range.value)===0,'Replay should restart at bottom');
 links[1].emit('click');assert(savedLanguage==='zh','Explicit language preference not saved');
 if(route==='/'&&saved==='zh')assert(assigned==='zh/index.html'+hash,'Default entrance should use the saved preference and preserve its fragment');
 else assert(assigned===null,'An explicit language URL must not be overridden by saved preference: '+route);
 if(hash)assert(links[1].href.endsWith(hash),'Language switch should preserve the fragment');
}
run('en');run('zh');
for(const language of ['en','zh'])for(const page of ['index.html','projects/stereo.html','projects/lidar.html','projects/collision.html','projects/motion.html','404.html'])run(language,language==='en'?'zh':'en','/'+(language==='zh'?'zh/':'')+page);
run('en','zh','/','#work');run('en','en','/');run('en',null,'/');run('en','invalid','/');
console.log('PASS: explicit language routes beat saved preference; default entrance honors valid saved choices; fragment preservation; English/Chinese controls, shared phase playback, scrubbing, replay and reduced-motion pause. These are behavior checks, not browser layout tests.');

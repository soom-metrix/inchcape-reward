const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1500,height:900}});
const errs=[];p.on('pageerror',e=>errs.push(String(e)));
await p.goto('http://localhost:8765/Inchcape_Reward_Review.html');await p.waitForTimeout(1500);
const tabs=await p.evaluate(()=>[...document.querySelectorAll('.tab')].map(b=>b.dataset.c));console.log(tabs);for(const c of tabs){
  await p.click('.tab[data-c="'+c+'"]');
  await p.waitForTimeout(2500);
  const r=await p.evaluate(()=>{const im=[...document.querySelectorAll('.card[data-side="tr"] img')];return {n:im.length,ok:im.filter(i=>i.src.startsWith('data:')).length,rib:document.querySelectorAll('.ribbon').length,title:document.querySelector('#rTitle').textContent}});
  console.log(JSON.stringify(r));}
console.log(errs);await b.close()})();

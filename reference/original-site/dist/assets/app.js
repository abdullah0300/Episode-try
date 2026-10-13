const menu = document.querySelector('.menu-button');
menu?.addEventListener('click', () => { const expanded = menu.getAttribute('aria-expanded') === 'true'; menu.setAttribute('aria-expanded', String(!expanded)); document.querySelector('.site-header').classList.toggle('menu-open', !expanded); });
document.querySelectorAll('.site-header nav a').forEach(a => a.addEventListener('click', () => { menu?.setAttribute('aria-expanded','false');document.querySelector('.site-header').classList.remove('menu-open'); }));
const search = document.querySelector('.episode-search input');
search?.addEventListener('input', () => {let count=0;document.querySelectorAll('[data-episode]').forEach(row => { const match = row.dataset.episode.split(' ').some(number => number.includes(search.value.trim()));row.hidden = !match;count += Number(match);});document.querySelector('.no-results').hidden = count > 0;});
document.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click', () => { document.querySelectorAll('[data-filter]').forEach(b => {b.classList.toggle('active',b===button);b.setAttribute('aria-pressed',String(b===button));});document.querySelectorAll('[data-language]').forEach(cell => cell.hidden = button.dataset.filter !== 'All' && cell.dataset.language !== button.dataset.filter); }));
const clock = document.querySelector('[data-countdown]');
let countdownInterval;
function tick(){
 if(!clock)return;
 const target = Date.parse(clock.dataset.countdown);
 const status = document.querySelector('[data-countdown-status]');
 if(!Number.isFinite(target)){status.textContent='Broadcast time is awaiting confirmation.';return;}
 const totalSeconds = Math.max(0, Math.ceil((target-Date.now())/1000));
 const values = {hours:Math.floor(totalSeconds/3600),minutes:Math.floor(totalSeconds%3600/60),seconds:totalSeconds%60};
 for(const [unit,value] of Object.entries(values))clock.querySelector(`[data-unit="${unit}"]`).textContent=String(value).padStart(2,'0');
 clock.setAttribute('aria-label',`${values.hours} hours and ${values.minutes} minutes until the scheduled Turkish broadcast`);
 if(totalSeconds===0){
  clock.setAttribute('aria-label','The scheduled broadcast time has passed');
  status.textContent='Scheduled broadcast time has passed. Check the subtitle guides for availability.';
  if(countdownInterval)clearInterval(countdownInterval);
 }
}
tick();if(clock&&Date.parse(clock.dataset.countdown)>Date.now())countdownInterval=setInterval(tick,1000);
document.querySelector('#alert-form')?.addEventListener('submit', e => { e.preventDefault();const form=e.target;if(!form.reportValidity())return;const preferences={email:form.elements.email.value,language:form.elements.language.value};const message=document.querySelector('#form-message');try{localStorage.setItem('episode-journal-alert',JSON.stringify(preferences));message.textContent=`${preferences.language} preference saved on this device. Email delivery is not connected in this preview.`;}catch{message.textContent='Your selection is ready. This browser could not save it; email delivery is not connected.'} });
if('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches){const observer=new IntersectionObserver(entries => entries.forEach(entry => {if(entry.isIntersecting){entry.target.classList.add('in-view');observer.unobserve(entry.target);}}),{threshold:0.08});document.querySelectorAll('.story-section,.schedule-section,.questions-section,.alerts-section').forEach(section=>{section.classList.add('reveal-ready');observer.observe(section);});}

"use strict";
const $=id=>document.getElementById(id);
let csrf="",ready=false,verified=false,busy=false,exists=false;
const err=text=>{$("error").textContent=text;$("error").hidden=!text;};
function refresh(){ $("check").disabled=!ready||busy; $("confirm").disabled=!verified||busy||exists; $("save").disabled=!verified||busy||exists||!$("confirm").checked; $("username").disabled=busy; $("token").disabled=busy; }
async function api(path,body){const options={cache:"no-store",credentials:"same-origin"};if(body!==undefined)Object.assign(options,{method:"POST",headers:{"Content-Type":"application/json","X-CSRF-Token":csrf},body:JSON.stringify(body)});const response=await fetch("api/"+path,options);const data=await response.json();if(!response.ok)throw Error(data.error||"Operazione non riuscita.");return data;}
function registry(value){exists=value.configured;$("registry").textContent=exists?"GHCR già configurato per "+value.username+". Puoi verificare un token, ma non sostituire quello salvato.":"GHCR non configurato: puoi registrare la prima credenziale.";refresh();}
async function status(){const s=await api("status");csrf=s.csrf;ready=true;registry(s.registry);}
for(const id of ["username","token"])$(id).addEventListener("input",()=>{verified=false;$("confirm").checked=false;$("verification").textContent="";refresh();});
$("confirm").addEventListener("change",refresh);
$("help").addEventListener("click",()=>$("guide").showModal());
$("close").addEventListener("click",()=>$("guide").close());
$("guide").addEventListener("close",()=>$("help").focus());
$("check").addEventListener("click",async()=>{
  busy=true;verified=false;err("");$("verification").textContent="Verifica account, permessi e manifest privato…";refresh();
  try{const r=await api("check",{username:$("username").value.trim(),token:$("token").value});verified=true;registry(r.registry);$("verification").textContent="Accesso GHCR verificato · "+r.package+(r.expiration?" · Scadenza: "+r.expiration:" · Scadenza non comunicata da GitHub");}
  catch(e){err(e.message);$("verification").textContent="Verifica non riuscita.";$("token").value="";}
  finally{busy=false;refresh();}
});
$("save").addEventListener("click",async()=>{
  busy=true;err("");$("result").textContent="Verifica finale e salvataggio nel Supervisor…";refresh();
  try{const r=await api("save",{username:$("username").value.trim(),token:$("token").value,confirm:$("confirm").checked});$("result").textContent=r.message;$("next").hidden=false;}
  catch(e){err(e.message);$("result").textContent="Salvataggio non confermato. Controlla lo stato del registro prima di riprovare.";}
  finally{$("token").value="";verified=false;$("confirm").checked=false;try{await status();}catch{ready=false;err("Stato registro non disponibile. Non ripetere il salvataggio finché non è verificabile.");}busy=false;refresh();}
});
status().catch(e=>{err(e.message);refresh();});

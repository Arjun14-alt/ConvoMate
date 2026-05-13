function addMsg(text,type){

let chat=document.getElementById("chat");

let div=document.createElement("div");

div.className="msg "+type;

div.innerText=text;

chat.appendChild(div);

chat.scrollTop=chat.scrollHeight;
}

async function send(){

let input=document.getElementById("input");

let text=input.value.trim();

if(!text)return;

addMsg(text,"user");

input.value="";

let res=await fetch("/chat",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
message:text
})

});

let data=await res.json();

addMsg(data.reply,"bot");
}

document
.getElementById("input")
.addEventListener("keypress",function(e){

if(e.key==="Enter"){
send();
}

});
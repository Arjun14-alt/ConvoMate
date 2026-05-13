function addHistory(text){

let box=document.getElementById("history");

let item=document.createElement("div");

item.className="history-item";

item.innerText=text.slice(0,40);

box.prepend(item);

}

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

let text=input.value;

if(!text)return;

addMsg(text,"user");

addHistory(text);

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
function addMsg(text,type){

const chat=document.getElementById("chat");

const div=document.createElement("div");
div.className="msg "+type;
div.innerText=text;

chat.appendChild(div);
chat.scrollTop=chat.scrollHeight;
}

async function send(){

const input=document.getElementById("input");
const text=input.value.trim();
if(!text)return;

addMsg(text,"user");
input.value="";

const res=await fetch("/chat",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({message:text})
});

const data=await res.json();
addMsg(data.reply,"bot");
}

/* FILE UPLOAD + READ */
document.getElementById("file").addEventListener("change", async function(){

const file=this.files[0];
if(!file)return;

const form=new FormData();
form.append("file",file);

const res=await fetch("/upload",{
method:"POST",
body:form
});

const data=await res.json();

addMsg("File uploaded: "+data.file,"bot");
addMsg("Now you can ask questions about it.","bot");
});
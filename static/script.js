// SPLASH SCREEN CONTROL
window.onload = () => {
    setTimeout(() => {
        document.getElementById("splash").style.display = "none";
        document.getElementById("app").classList.remove("hidden");
    }, 1200);
};

// CHAT
function addMsg(text, type){
    const chat = document.getElementById("chat");

    const div = document.createElement("div");
    div.className = "msg " + type;
    div.innerText = text;

    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}

// FAKE STREAMING EFFECT (ChatGPT-like typing)
function typeText(element, text, speed=15){
    let i = 0;
    element.innerText = "";

    function typing(){
        if(i < text.length){
            element.innerText += text[i];
            i++;
            setTimeout(typing, speed);
        }
    }

    typing();
}

async function send(){

    const input = document.getElementById("input");
    const text = input.value.trim();
    if(!text) return;

    addMsg(text, "user");
    input.value = "";

    const res = await fetch("/chat",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({message:text})
    });

    const data = await res.json();

    const chat = document.getElementById("chat");

    const div = document.createElement("div");
    div.className = "msg bot";

    chat.appendChild(div);

    typeText(div, data.reply, 12);
}
function addMessage(text, type){

    const chat = document.getElementById("chat");

    const div = document.createElement("div");

    div.className = "msg " + type;

    chat.appendChild(div);

    // smooth typing effect
    if(type === "bot"){
        typeText(div, text);
    }else{
        div.innerText = text;
    }

    chat.scrollTop = chat.scrollHeight;
}


/* CHATGPT-LIKE TYPING EFFECT */

function typeText(element, text){

    let index = 0;

    element.innerText = "";

    const speed = 12;

    function typing(){

        if(index < text.length){

            element.innerText += text.charAt(index);

            index++;

            const chat = document.getElementById("chat");
            chat.scrollTop = chat.scrollHeight;

            setTimeout(typing, speed);

        }
    }

    typing();
}


async function send(){

    const input = document.getElementById("input");

    const message = input.value.trim();

    if(!message) return;

    addMessage(message, "user");

    input.value = "";

    // typing placeholder
    const chat = document.getElementById("chat");

    const loading = document.createElement("div");

    loading.className = "msg bot";

    loading.id = "loading";

    loading.innerText = "Thinking...";

    chat.appendChild(loading);

    chat.scrollTop = chat.scrollHeight;

    try{

        const response = await fetch("/api/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        document.getElementById("loading").remove();

        addMessage(data.reply, "bot");

    } catch(err){

        document.getElementById("loading").remove();

        addMessage("Connection error.", "bot");
    }
}


/* ENTER KEY */

document
.getElementById("input")
.addEventListener("keypress", function(e){

    if(e.key === "Enter"){
        send();
    }
});
function addMessage(text, type){

    const chat = document.getElementById("chat");

    const div = document.createElement("div");

    div.className = "msg " + type;

    div.innerText = text;

    chat.appendChild(div);

    chat.scrollTop = chat.scrollHeight;
}


async function send(){

    const input = document.getElementById("input");

    const message = input.value.trim();

    if(!message) return;

    addMessage(message, "user");

    input.value = "";

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

        addMessage(data.reply, "bot");

    } catch(err){

        addMessage("Connection error.", "bot");
    }
}


document
.getElementById("input")
.addEventListener("keypress", function(e){

    if(e.key === "Enter"){
        send();
    }
});
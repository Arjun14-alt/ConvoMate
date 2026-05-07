function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value;

    if (!message) return;

    addMessage("You", message);

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        addMessage("Bot", data.reply);
    });

    input.value = "";
}


function addMessage(sender, text) {
    let chatBox = document.getElementById("chat-box");

    let msg = document.createElement("div");
    msg.className = sender === "You" ? "user-msg" : "bot-msg";

    msg.innerHTML = `<b>${sender}:</b> ${text}`;
    chatBox.appendChild(msg);

    chatBox.scrollTop = chatBox.scrollHeight;
}
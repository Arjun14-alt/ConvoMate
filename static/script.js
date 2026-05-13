function addMsg(text, type) {
    const chat = document.getElementById("chat");

    const msg = document.createElement("div");
    msg.className = "msg " + type;
    msg.innerText = text;

    chat.appendChild(msg);

    // smooth scroll to bottom
    chat.scrollTo({
        top: chat.scrollHeight,
        behavior: "smooth"
    });
}

async function send() {
    const input = document.getElementById("input");
    const text = input.value.trim();

    if (!text) return;

    addMsg(text, "user");
    input.value = "";

    // typing indicator (fake but smooth UX)
    const typing = document.createElement("div");
    typing.className = "msg bot";
    typing.innerText = "typing...";
    typing.id = "typing";
    document.getElementById("chat").appendChild(typing);

    try {
        const res = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: text })
        });

        const data = await res.json();

        document.getElementById("typing")?.remove();

        addMsg(data.reply, "bot");

    } catch (err) {
        document.getElementById("typing")?.remove();
        addMsg("Connection error. Try again.", "bot");
    }
}

// ENTER KEY SUPPORT (IMPORTANT FOR MOBILE FEEL)
document.getElementById("input").addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        send();
    }
});

// OPTIONAL: auto focus on mobile open
window.onload = () => {
    document.getElementById("input").focus();
};

// PWA SERVICE WORKER
if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("/static/sw.js");
}
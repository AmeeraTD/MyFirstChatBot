function appendMessage(sender, text) {
    const chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += `<p><strong>${sender}:</strong> ${text}</p>`;
    chatbox.scrollTop = chatbox.scrollHeight;
}

function sendMessage() {
    const userInput = document.getElementById("userInput");
    const message = userInput.value.trim();
    if (message === "") return;

    appendMessage("You", message);

    fetch("/get", {
        method: "POST",
        body: JSON.stringify({ message }),
        headers: { "Content-Type": "application/json" },
    })
    .then((res) => res.json())
    .then((data) => {
        appendMessage("Bot", data.response);
        userInput.value = "";
    });
}

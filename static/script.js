function appendMessage(sender, text) {
    const chatbox = document.getElementById("chatbox");
    
    const message = document.createElement("div");
    message.classList.add("message");
  
    if (sender === "You") {
      message.classList.add("user");
    } else {
      message.classList.add("bot");
    }
  
    message.textContent = text;
    chatbox.appendChild(message);
    chatbox.scrollTop = chatbox.scrollHeight;
  }
  
  function sendMessage() {
    const userInput = document.getElementById("userInput");
    const message = userInput.value.trim();
  
    if (message === "") return;
  
    // Append user message to chat
    appendMessage("You", message);
  
    // Fetch response from backend
    fetch("/get", {
      method: "POST",
      body: JSON.stringify({ message }),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        appendMessage("Bot", data.response);
      })
      .catch((error) => {
        console.error("Error:", error);
        appendMessage("Bot", "Oops! Something went wrong.");
      });
  
    userInput.value = "";
  }
  
  // Allow pressing Enter to send
  document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("userInput");
    input.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        sendMessage();
      }
    });
  });
  
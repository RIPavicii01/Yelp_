const chatBox = document.getElementById("chat-box");
const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");

function addMessage(text, isUser = false, isTyping = false) {
  const msgDiv = document.createElement("div");
  msgDiv.className = "message" + (isUser ? " user" : "");
  const bubble = document.createElement("div");
  bubble.className = "bubble" + (isUser ? " user" : " bot");
  bubble.textContent = text;
  msgDiv.appendChild(bubble);

  // 메타(이름/시간)
  const meta = document.createElement("div");
  meta.className = "meta" + (isUser ? "" : " bot");
  meta.textContent = isUser ? "장형준" : "AI";
  msgDiv.appendChild(meta);

  if (isTyping) {
    bubble.classList.add("typing");
    bubble.textContent = "AI가 응답 중...";
  }
  chatBox.appendChild(msgDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
  return msgDiv;
}

function removeTyping() {
  const typingDiv = chatBox.querySelector(".bubble.typing");
  if (typingDiv && typingDiv.parentNode) {
    typingDiv.parentNode.remove();
  }
}

chatForm.addEventListener("submit", async function (e) {
  e.preventDefault();
  const text = userInput.value.trim();
  if (!text) return;
  addMessage(text, true);
  userInput.value = "";
  addMessage("", false, true);

  try {
    const res = await fetch("http://localhost:8000/chat/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt: text }),
    });
    const data = await res.json();
    removeTyping();
    addMessage(data.response, false);
  } catch (err) {
    removeTyping();
    addMessage("서버 오류가 발생했습니다.", false);
  }
});

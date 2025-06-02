const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");
const messagesContainer = document.getElementById("messagesContainer");
const welcomeScreen = document.getElementById("welcomeScreen");
const chatHistory = document.getElementById("chatHistory");
const statsContent = document.getElementById("statsContent");

let conversationIndex = 0;

chatForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const query = messageInput.value.trim();
  if (!query) return;

  welcomeScreen.style.display = "none";
  addMessage("user", query);
  messageInput.value = "";

  const formData = new FormData();
  formData.append("query", query);

  const response = await fetch("/", {
    method: "POST",
    headers: { "X-Requested-With": "XMLHttpRequest" },
    body: formData,
  });

  const data = await response.json();
  addMessage("bot", data.answer);

  // History
  const preview = query.slice(0, 40) + (query.length > 40 ? "..." : "");
  const histItem = document.createElement("div");
  histItem.className = "chat-history-item";
  histItem.innerHTML = `
    <div class="chat-title">Q${conversationIndex + 1}: ${preview}</div>
    <div class="chat-preview">F1: ${data.scores.f1} | P: ${data.scores.precision} | R: ${data.scores.recall}</div>
  `;
  chatHistory.appendChild(histItem);
  conversationIndex++;

  // Stats
  const statHTML = `
    <div class="stats-card">
      <h4><i class="fas fa-chart-bar"></i> BERTScore</h4>
      <div class="metric-item"><span>Precision</span><span class="metric-value metric-medium">${data.scores.precision}</span></div>
      <div class="metric-item"><span>Recall</span><span class="metric-value metric-medium">${data.scores.recall}</span></div>
      <div class="metric-item"><span>F1 Score</span><span class="metric-value metric-high">${data.scores.f1}</span></div>
    </div>
    <div class="stats-card">
      <h4><i class="fas fa-book"></i> Sources</h4>
      ${data.sources.map(src => `
        <div class="source-item">
          <div class="source-title">${src.pdf_name}</div>
          <div class="source-page">Page ${src.page_number}</div>
        </div>
      `).join("")}
    </div>
  `;
  statsContent.innerHTML = statHTML;
});

function addMessage(role, text) {
  const msg = document.createElement("div");
  msg.className = `message ${role}`;
  msg.innerHTML = `
    <div class="message-header">
      <div class="message-avatar">${role === 'user' ? 'U' : 'Q'}</div>
      <div class="message-author">${role === 'user' ? 'You' : 'QanoonAI'}</div>
    </div>
    <div class="message-content">${text}</div>
  `;
  messagesContainer.appendChild(msg);
  messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function askExample(q) {
  messageInput.value = q;
  chatForm.dispatchEvent(new Event("submit"));
}

document.getElementById("menuToggle").onclick = () =>
  document.getElementById("sidebar").classList.toggle("open");

document.getElementById("statsToggle").onclick = () =>
  document.getElementById("statsPanel").classList.add("open");

document.getElementById("closeStats").onclick = () =>
  document.getElementById("statsPanel").classList.remove("open");

document.getElementById("newChatBtn").onclick = () => {
  messagesContainer.innerHTML = "";
  chatHistory.innerHTML = "";
  statsContent.innerHTML = "";
  conversationIndex = 0;
  welcomeScreen.style.display = "flex";
};

document.getElementById("clearChat").onclick = () => {
  messagesContainer.innerHTML = "";
  statsContent.innerHTML = "";
};

then(data => {
    const container = document.getElementById("aiAnswerContainer");
    container.innerHTML = data.answer;  // Render Gemini's HTML response directly
})


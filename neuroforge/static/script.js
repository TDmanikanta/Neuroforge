async function askAI() {
  const question = document.getElementById("question").value;
  const responseDiv = document.getElementById("response");
  responseDiv.innerHTML = "Thinking...";

  const res = await fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question })
  });

  const data = await res.json();
  if (data.answer) {
    responseDiv.innerText = data.answer;
  } else {
    responseDiv.innerText = "Error: " + (data.error || "Unknown");
  }
}

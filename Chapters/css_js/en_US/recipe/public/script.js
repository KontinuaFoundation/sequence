// Dark mode
const themeButton = document.querySelector("#theme-button");

themeButton.addEventListener("click", () => {
  document.body.classList.toggle("dark");
  if (document.body.classList.contains("dark")) {
    themeButton.textContent = "Light mode";
  } else {
    themeButton.textContent = "Dark mode";
  }
});

// Click a step to cross it off
for (const step of document.querySelectorAll(".steps-section li")) {
  step.addEventListener("click", () => {
    step.classList.toggle("done");
  });
}

// Scale the recipe
function formatAmount(x) {
  const whole = Math.floor(x);
  const quarters = Math.round((x - whole) * 4);
  const fraction = ["", "1/4", "1/2", "3/4"][quarters];
  if (whole === 0) {
    return fraction;
  }
  if (fraction === "") {
    return String(whole);
  }
  return whole + " " + fraction;
}

const batchesInput = document.querySelector("#batches");

batchesInput.addEventListener("input", () => {
  const batches = Number(batchesInput.value);
  if (batches < 1) {
    return;
  }
  for (const span of document.querySelectorAll(".amount")) {
    span.textContent = formatAmount(Number(span.dataset.amount) * batches);
  }
});

// Likes, stored on the server
const likeButton = document.querySelector("#like-button");
const likeCount = document.querySelector("#like-count");

async function updateLikes(method) {
  const response = await fetch("/api/likes", { method: method });
  const data = await response.json();
  likeCount.textContent = data.likes;
}

updateLikes("GET");
likeButton.addEventListener("click", () => {
  updateLikes("POST");
});

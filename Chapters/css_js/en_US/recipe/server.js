const express = require("express");

const app = express();
const PORT = 3000;

let likes = 0;

// Send the files in the public folder: index.html, style.css, script.js, ...
app.use(express.static("public"));

app.get("/api/likes", (req, res) => {
  res.json({ likes: likes });
});

app.post("/api/likes", (req, res) => {
  likes += 1;
  res.json({ likes: likes });
});

app.listen(PORT, () => {
  console.log(`Recipe site running at http://localhost:${PORT}`);
});

const express = require("express");

const app = express();
const PORT = 3000;

const student = {
  student_id: 42,
  name: "John Smith",
  major: "Computer Science",
  credits_completed: 88
};

app.get("/students/42", (req, res) => {
  res.json(student);
});

app.listen(PORT, () => {
  console.log(`API running at http://localhost:${PORT}`);
});
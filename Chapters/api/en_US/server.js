const express = require("express");

const app = express();

// parse JSON bodies before route handlers
app.use(express.json());

const PORT = 3000;


// From Part One
// const student = {
//   student_id: 42,
//   name: "John Smith",
//   major: "Computer Science",
//   credits_completed: 88
// };

// app.get("/students/42", (req, res) => {
//   res.json(student);
// });


// Part Two
const students = [
  {
    student_id: 42,
    name: "John Smith",
    major: "Computer Science",
    credits_completed: 88
  },
  {
    student_id: 43,
    name: "Jane Doe",
    major: "Mathematics",
    credits_completed: 61
  }
];

app.get("/students", (req, res) => {
  res.json(students);
});

app.get("/students/:id", (req, res) => {
  // use the id that is passed in the route
  const id = Number(req.params.id);
  // find a student from our students array
  const student = students.find((s) => s.student_id === id);

  // if the id is not found, we assume the student is not in the array
  if (!student) {
    return res.status(404).json({ error: "Student not found" });
  }

  res.json(student);
});

app.post("/students", (req, res) => {
  const student = req.body;

  // basic validation: ensure we received an object
  if (!student || Object.keys(student).length === 0) {
    return res.status(400).json({ error: "Invalid student data" });
  }

  students.push(student);

  // status 201 means that the student was pushed successfully
  res.status(201).json(student);
});

app.listen(PORT, () => {
  console.log(`API running at http://localhost:${PORT}`);
});

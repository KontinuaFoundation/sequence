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

app.put("/students/:id", (req, res) => {
  const id = Number(req.params.id);
  const index = students.findIndex((s) => s.student_id === id);
 
  if (index === -1) {
    return res.status(404).json({ error: "Student not found" });
  }
 
  // PUT replaces the whole object, so we overwrite it completely
  students[index] = { 
    student_id: id, ...req.body // this format keeps the same student_id and updates the rest of the fields with the new data
  }; 
  res.json(students[index]);
});

app.patch("/students/:id", (req, res) => {
  const id = Number(req.params.id);
  const student = students.find((s) => s.student_id === id);
 
  if (!student) {
    return res.status(404).json({ error: "Student not found" });
  }
 
  // PATCH merges the incoming fields onto the existing object
  Object.assign(student, req.body);
  res.json(student);
});

app.delete("/students/:id", (req, res) => {
  const id = Number(req.params.id);
  const index = students.findIndex((s) => s.student_id === id);
 
  if (index === -1) {
    return res.status(404).json({ error: "Student not found" });
  }
 
  students.splice(index, 1);
  // status 204 means "success, but there is nothing to send back"
  res.status(204).send();
});
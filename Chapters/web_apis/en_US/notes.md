# Web APIs — Notes

## Summary
Explains HTTP requests and responses (methods, URLs, headers, bodies, status codes, JSON), then builds a small Express server for a student resource and exercises it with curl (GET, POST, PUT, PATCH, DELETE), API keys with a Bearer header, and Postman. Ends with a summary.

## Changes in this pass
- Corrected the CRUD description. It is CREATE, READ, UPDATE, and DELETE (not REMOVE). GET is the READ operation, and the table now says READ.
- Fixed the POST text. The handler does add to the in-memory array (the old text said it did not). Added that the data is lost when the server restarts.
- Fixed the DELETE example. It removes student 44 (Jerry Doe), who is added with POST in the next section, so the text now says to run it after that section.
- Corrected the curl -i Content-Length to 76 (it was 78). Noted that Express adds headers the example omits.
- Made the POST validation reject an empty object, not only a missing body.
- Changed a python code fence that held a text request to a text fence.
- Fixed typos ("test our an API", "imagine n API") and the plural "API's" to "APIs".
- Added an unworked exercise: a PATCH request that changes Jane Doe's credits to 70 (answer: the updated student, with the name and major unchanged).

## Strengths
- The request and response concepts are explained with clear, everyday pictures (restaurant, librarian, package note).
- The PUT versus PATCH distinction and the status codes are correct.
- The API key rules are accurate and practical.

## Open items
- The -i output is illustrative. Run the server to confirm the exact headers before publishing.
- The API key example hardcodes a key for simplicity, as the text says. Keep the warning.

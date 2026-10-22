# CSS and JavaScript: Summary

## What the chapter covers
Turns the HTML chapter's plain recipe page into a site a student would show friends:
- before-and-after screenshots of the page;
- project setup (recipe/ with public/);
- a first stylesheet (fonts, hex colors from Data Representation, units, centering);
- selectors and the cascade;
- the box model (TikZ figure), restyling the image and the facts table;
- flexbox for a pill-button nav and a responsive two-column layout (phone screenshot);
- a Python-to-JavaScript translation table and the browser console;
- the DOM and event listeners: dark mode (JavaScript flips a class, CSS styles it), crossing off steps, and a batches box that scales every amount with data attributes and a quarter-cup formatter;
- serving the page with express.static from the Web APIs server, plus a like button using fetch and async/await;
- showing friends on local Wi-Fi, hosting, and never shipping secrets in front-end code.

## Key ideas
- CSS rules = selector + properties; the more specific selector wins, then the later one.
- Every element is a box: content, padding, border, margin.
- display: flex with flex-wrap gives layouts that adapt to the screen.
- JavaScript finds elements with querySelector, reacts with addEventListener, and changes classes and text; CSS decides the look.
- fetch talks to a server without freezing the page; shared data must live on the server.

## Changes in this pass
- New chapter, placed in volume 26 after data_representation (which provides hex color codes) and before digital_logic. It builds on html (same volume) and web_apis (volume 25, Express and curl).
- Complete working project in recipe/ (server.js, public/index.html, style.css, script.js, cookies.jpg). Run under Node with Express and tested in headless Chrome: scaling gives 4 1/2 cups and 48 cookies for 2 batches and 6 3/4 cups and 72 cookies for 3, an empty box is ignored, dark mode and crossing off work, likes persist across reloads, and there are no script errors. Screenshots are real renders.
- 8 exercises with answers (cascade, box model arithmetic, hover rule, Python-to-JS translation, fixing '2 cup butter', a progress counter, persisting likes with fs, and why the server cannot trust a like). All answer code was run in Node.
- Edited html: fixed the Recipe Facts exercise starter (it said Baking Tips), added a forward pointer, and added a closing 'The Finished Page' section with the full assembled page (also saved as html/en_US/index.html), which is where this chapter begins.

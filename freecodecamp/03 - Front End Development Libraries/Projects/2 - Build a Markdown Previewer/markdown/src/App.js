import { useState } from 'react';
import { marked } from 'marked';
import './App.css';

function App() {
  const [text, setText] = useState(`
  # Markdown Previewer (Made with React)
  ## Sub-heading
  ### Features:
  
  You can write \`<div>inline</div>\` code.
  \`\`\`
  // or multi-line code:
  
  {
    "firstName": "Charlotte",
    "lastName": "Belmont",
    "age": 24
  }

  \`\`\`
  
  You can also make text

  **bold**
  _italic_
  **_both_**
  ~~crossed~~
  **_~~Try it out!~~_**

  You can

  - Make
  - Lists
  - Like
  - This
    - And
      - Also
        - Indent like crazy

  and

  > Block Quotes!

  And of course, embed images, links..
  Here's a picture of the [Ada Lovelace Tribute Page](https://vittv.github.io/ada-tribute/) I made when I took Responsive Web Design!

  ![Ada Lovelace Tribute Page](https://raw.githubusercontent.com/Vittv/portfolio-study/main/images/adalovelacetribute.png)


  ### Check out my [GitHub](https://github.com/Vittv) for more projects!
  `);

  marked.setOptions({
    breaks: true
  })

  return (
    <div className="App">
      <div id="app-wrapper">
        <div id="editor-wrapper">
          <div class="toolbar">
            <h3>EDIT</h3>
          </div>
            <textarea
            id="editor"
              onChange={(event) => {
                setText(event.target.value)
              }}
              value={text}
            ></textarea>
        </div>
        <div id="preview-wrapper">
          <div class="toolbar">
            <h3>PREVIEW</h3>
          </div>
            <div
              id="preview"
              dangerouslySetInnerHTML={{
                __html: marked(text),
              }}
            ></div>
        </div>
      </div>
    </div>
  );
}

export default App;

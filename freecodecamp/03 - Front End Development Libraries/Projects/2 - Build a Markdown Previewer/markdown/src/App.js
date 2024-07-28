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
  
  You can also make text **bold** or _italic_.
  Or **_both_**!

  You can

  - Make
  - Lists!

  and

  > Block Quotes!

  And of course, embed images

  ![alt text](image.jpg)

  Checkout my [GitHub](https://github.com/Vittv) for more projects!

  `);

  marked.setOptions({
    breaks: true
  })

  return (
    <div className="App">
      <div id="app-wrapper">
        <div id="editor-wrapper">
          <div class="toolbar">
            <h3>Editor</h3>
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
            <h3>Previewer</h3>
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

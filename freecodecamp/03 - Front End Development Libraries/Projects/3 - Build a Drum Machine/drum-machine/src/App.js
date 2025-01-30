import { useEffect, useState } from "react";
import './App.css';

function App() {
  const [activeKey, setActiveKey] = useState("");
  useEffect(() => {
    document.addEventListener("keydown", (event) => {
      console.log(event.key);
      playSound(event.key.toUpperCase());
    });
  }, []);

  const drumPads = [
    {
      keyCode: 81,
      text: "Q",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/Heater-1.mp3"
    },
    {
      keyCode: 87,
      text: "W",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/Heater-2.mp3"
    },
    {
      keyCode: 69,
      text: "E",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/Heater-3.mp3"
    },
    {
      keyCode: 65,
      text: "A",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/Heater-4_1.mp3"
    },
    {
      keyCode: 83,
      text: "S",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/Heater-6.mp3"
    },
    {
      keyCode: 68,
      text: "D",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/Dsc_Oh.mp3"
    },
    {
      keyCode: 90,
      text: "Z",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/Kick_n_Hat.mp3"
    },
    {
      keyCode: 88,
      text: "X",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/RP4_KICK_1.mp3"
    },
    {
      keyCode: 67,
      text: "C",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/Cev_H2.mp3"
    }
  ];

  function playSound(selector) {
    const audio = document.getElementById(selector);
    console.log(audio);
    audio.play();
    setActiveKey(selector)
  }

  return (
    <div className="App">
      <div id="drum-machine">
        <h3 id="title">DRUM MACHINE</h3>
        <div id="display">{activeKey}</div>
        <div className="drum-pads">
          {drumPads.map((drumPad) => (
            <div
              key={drumPad.src}
              onClick={() => {
                playSound(drumPad.text)
              }} 
              className="drum-pad"
              id={drumPad.src}
            >
              {drumPad.text}
              <audio 
                className="clip"
                id={drumPad.text}
                src={drumPad.src}
              ></audio>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;

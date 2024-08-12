import { useEffect, useState } from "react";
import './App.css';

function App() {
  const [activeKey, setActiveKey] = useState("");

  useEffect(() => {
    const handleKeydown = (event) => {
      const key = event.key.toUpperCase();
      const drumPad = drumPads.find(pad => pad.text === key);
      if (drumPad) {
        playSound(drumPad.text, drumPad.name);
        const padElement = document.getElementById(drumPad.src);
        if (padElement) {
          padElement.classList.add("active");
        }
      }
    };

    const handleKeyup = (event) => {
      const key = event.key.toUpperCase();
      const drumPad = drumPads.find(pad => pad.text === key);
      if (drumPad) {
        const padElement = document.getElementById(drumPad.src);
        if (padElement) {
          padElement.classList.remove("active");
        }
      }
    };

    document.addEventListener("keydown", handleKeydown);
    document.addEventListener("keyup", handleKeyup);

    return () => {
      document.removeEventListener("keydown", handleKeydown);
      document.removeEventListener("keyup", handleKeyup);
    };
  }, []);

  const drumPads = [
    {
      keyCode: 81,
      text: "Q",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/Heater-1.mp3",
      name: "HEATER 1"
    },
    {
      keyCode: 87,
      text: "W",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/Heater-2.mp3",
      name: "HEATER 2"
    },
    {
      keyCode: 69,
      text: "E",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/Heater-3.mp3",
      name: "HEATER 3"
    },
    {
      keyCode: 65,
      text: "A",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/Heater-4_1.mp3",
      name: "HEATER 4"
    },
    {
      keyCode: 83,
      text: "S",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/Heater-6.mp3",
      name: "CLAP"
    },
    {
      keyCode: 68,
      text: "D",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/Dsc_Oh.mp3",
      name: "OPEN-HH"
    },
    {
      keyCode: 90,
      text: "Z",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/Kick_n_Hat.mp3",
      name: "KICK-N'-HAT"
    },
    {
      keyCode: 88,
      text: "X",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/RP4_KICK_1.mp3",
      name: "KICK"
    },
    {
      keyCode: 67,
      text: "C",
      src: "https://cdn.freecodecamp.org/testable-projects-fcc/audio/Cev_H2.mp3",
      name: "CLOSED-HH"
    }
  ];

  function playSound(selector, name) {
    const audio = document.getElementById(selector);
    if (audio) { // Check if audio element exists
      if (!audio.paused) {
        audio.pause();
        audio.currentTime = 0;
      }
      audio.play();
      setActiveKey(name); // Set the drum sound name to display
    }
  }

  return (
    <div className="App">
      <div id="drum-machine">
        <h3 id="title">♪ DRUM MACHINE</h3>
        <div id="display">{activeKey}</div>
        <div className="drum-pads">
          {drumPads.map((drumPad) => (
            <div
              key={drumPad.src}
              onClick={() => {
                playSound(drumPad.text, drumPad.name);
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

import React, { useState, useEffect, useRef } from 'react';

const Clock = () => {
  const [breakLength, setBreakLength] = useState(5);
  const [sessionLength, setSessionLength] = useState(25);
  const [timeLeft, setTimeLeft] = useState(25 * 60);
  const [isSession, setIsSession] = useState(true);
  const [isRunning, setIsRunning] = useState(false);
  const timerRef = useRef(null);
  const audioRef = useRef(null);

  const formatTime = (time) => {
    const minutes = Math.floor(time / 60);
    const seconds = time % 60;
    return `${minutes < 10 ? '0' : ''}${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
  };

  const handleReset = () => {
    clearInterval(timerRef.current);
    setBreakLength(5);
    setSessionLength(25);
    setTimeLeft(25 * 60);
    setIsSession(true);
    setIsRunning(false);
    audioRef.current.pause();
    audioRef.current.currentTime = 0;
  };

  const handleIncrement = (type) => {
    if (type === 'break') {
      setBreakLength(prev => Math.min(prev + 1, 60));
    } else if (type === 'session') {
      setSessionLength(prev => {
        const newSessionLength = Math.min(prev + 1, 60);
        if (isSession && !isRunning) {
          setTimeLeft(newSessionLength * 60);
        }
        return newSessionLength;
      });
    }
  };

  const handleDecrement = (type) => {
    if (type === 'break') {
      setBreakLength(prev => Math.max(prev - 1, 1));
    } else if (type === 'session') {
      setSessionLength(prev => {
        const newSessionLength = Math.max(prev - 1, 1);
        if (isSession && !isRunning) {
          setTimeLeft(newSessionLength * 60);
        }
        return newSessionLength;
      });
    }
  };

  const handleStartStop = () => {
    if (isRunning) {
      clearInterval(timerRef.current);
      setIsRunning(false);
    } else {
      setIsRunning(true);
      timerRef.current = setInterval(() => {
        setTimeLeft(prev => {
          if (prev === 0) {
            audioRef.current.play();
            if (isSession) {
              setIsSession(false);
              return breakLength * 60;
            } else {
              setIsSession(true);
              return sessionLength * 60;
            }
          }
          return prev - 1;
        });
      }, 1000);
    }
  };

  useEffect(() => {
    if (isRunning) {
      timerRef.current = setInterval(() => {
        setTimeLeft(prev => {
          if (prev === 0) {
            audioRef.current.play();
            if (isSession) {
              setIsSession(false);
              return breakLength * 60;
            } else {
              setIsSession(true);
              return sessionLength * 60;
            }
          }
          return prev - 1;
        });
      }, 1000);
    }
    return () => clearInterval(timerRef.current);
  }, [isRunning, isSession, breakLength, sessionLength]);

  return (
    <div id="clock">
      <div id="break-label">Break Length</div>
      <button id="break-decrement" onClick={() => handleDecrement('break')}>-</button>
      <span id="break-length">{breakLength}</span>
      <button id="break-increment" onClick={() => handleIncrement('break')}>+</button>
      <div id="session-label">Session Length</div>
      <button id="session-decrement" onClick={() => handleDecrement('session')}>-</button>
      <span id="session-length">{sessionLength}</span>
      <button id="session-increment" onClick={() => handleIncrement('session')}>+</button>
      <div id="timer">
        <div id="timer-label">{isSession ? 'Session' : 'Break'}</div>
        <div id="time-left">{formatTime(timeLeft)}</div>
        <button id="start_stop" onClick={handleStartStop}>
          {isRunning ? 'Pause' : 'Start'}
        </button>
        <button id="reset" onClick={handleReset}>Reset</button>
        <audio id="beep" ref={audioRef} src="https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg" />
      </div>
    </div>
  );
};

export default Clock;

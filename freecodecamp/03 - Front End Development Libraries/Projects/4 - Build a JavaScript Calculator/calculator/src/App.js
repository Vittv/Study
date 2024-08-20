import React, { useState } from 'react';
import './Calculator.css';

const Calculator = () => {
  const [displayValue, setDisplayValue] = useState('0');
  const [expression, setExpression] = useState([]);
  const [isResult, setIsResult] = useState(false);

  const handleClear = () => {
    setDisplayValue('0');
    setExpression([]);
    setIsResult(false);
  };

  const handleNumberClick = (e) => {
    const value = e.target.innerText;
    if (isResult) {
      setDisplayValue(value);
      setExpression([value]);
      setIsResult(false);
    } else {
      const newDisplayValue =
        displayValue === '0' || ['+', '-', '*', '/'].includes(displayValue)
          ? value
          : displayValue + value;
      setDisplayValue(newDisplayValue);
      setExpression([...expression, value]);
    }
  };

  const handleDecimalClick = () => {
    if (isResult) {
      setDisplayValue('0.');
      setExpression(['0.']);
      setIsResult(false);
    } else if (!displayValue.includes('.')) {
      const newDisplayValue = displayValue + '.';
      setDisplayValue(newDisplayValue);
      setExpression([...expression, '.']);
    }
  };

  const handleOperatorClick = (e) => {
    const operator = e.target.innerText;
    const lastItem = expression[expression.length - 1];

    if (isResult) {
      setExpression([displayValue, operator]);
      setIsResult(false);
    } else {
      if (['+', '*', '/'].includes(lastItem) && operator !== '-') {
        setExpression([...expression.slice(0, -1), operator]);
      } else if (lastItem === '-' && ['+', '*', '/'].includes(expression[expression.length - 2])) {
        setExpression([...expression.slice(0, -2), operator]);
      } else {
        setExpression([...expression, operator]);
      }
      setDisplayValue(operator);
    }
  };

  const handleCalculation = () => {
    if (isResult) return;

    try {
      const expressionStr = expression.join('');
      const result = eval(expressionStr);
      setDisplayValue(String(result));
      setExpression([String(result)]);
      setIsResult(true);
    } catch (error) {
      setDisplayValue('Error');
    }
  };

  return (
    <div class="calculator-container">
      <div className="calculator">
        <div id="display" className="display">{displayValue}</div>
        <button id="clear" className="btn-clear" onClick={handleClear}>AC</button>
        <button id="divide" className="btn-operator" onClick={handleOperatorClick}>/</button>
        <button id="multiply" className="btn-operator" onClick={handleOperatorClick}>*</button>
        <button id="seven" className="btn-number" onClick={handleNumberClick}>7</button>
        <button id="eight" className="btn-number" onClick={handleNumberClick}>8</button>
        <button id="nine" className="btn-number" onClick={handleNumberClick}>9</button>
        <button id="subtract" className="btn-operator" onClick={handleOperatorClick}>-</button>
        <button id="four" className="btn-number" onClick={handleNumberClick}>4</button>
        <button id="five" className="btn-number" onClick={handleNumberClick}>5</button>
        <button id="six" className="btn-number" onClick={handleNumberClick}>6</button>
        <button id="add" className="btn-operator" onClick={handleOperatorClick}>+</button>
        <button id="one" className="btn-number" onClick={handleNumberClick}>1</button>
        <button id="two" className="btn-number" onClick={handleNumberClick}>2</button>
        <button id="three" className="btn-number" onClick={handleNumberClick}>3</button>
        <button id="zero" className="btn-number" onClick={handleNumberClick}>0</button>
        <button id="decimal" className="btn-decimal" onClick={handleDecimalClick}>.</button>
        <button id="equals" className="btn-equals" onClick={handleCalculation}>=</button>
      </div>
    </div>
  );
};

export default Calculator;

$(document).ready(function() {
    let current = '';
    let result = '';
    let operator = '';
    let isDecimal = false;
    let newOperation = false;

    function updateDisplay(value) {
        $('.result').text(value || '0');
    }

    function clearAll() {
        current = '';
        result = '';
        operator = '';
        isDecimal = false;
        newOperation = false;
        $('.operation').text('');
        updateDisplay('0');
    }

    function handleOperation(value) {
        if (current === '' && result !== '') {
            current = result;
        }

        if (result !== '') {
            result = operate(result, current, operator);
        } else {
            result = current;
        }

        operator = value;
        current = '';
        isDecimal = false;
        $('.operation').text(`${result} ${operator}`);
        newOperation = false;
    }

    function operate(a, b, op) {
        a = parseFloat(a);
        b = parseFloat(b);

        switch(op) {
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            case '/': return a / b;
            default: return b;
        }
    }

    function calculatePercentage(value) {
        return (parseFloat(result) * parseFloat(value)) / 100;
    }

    $('.button').click(function() {
        const value = $(this).text().trim();

        if (!isNaN(value) || value === '.') {
            if (newOperation) {
                clearAll();
                newOperation = false;
            }

            if (value === '.' && isDecimal) return;
            if (value === '.') isDecimal = true;
            current += value;
            updateDisplay(current);
        } else {
            switch (value) {
                case 'C':
                    clearAll();
                    break;
                case 'CE':
                    current = '';
                    updateDisplay('');
                    break;
                case '⌫':
                    current = current.slice(0, -1);
                    updateDisplay(current);
                    break;
                case '+/-':
                    if (current) {
                        current = (parseFloat(current) * -1).toString();
                        updateDisplay(current);
                    }
                    break;
                case '=':
                    if (result !== '' && current !== '') {
                        result = operate(result, current, operator);
                        updateDisplay(result);
                        current = result.toString();
                        operator = '';
                        $('.operation').text('');
                        newOperation = true;
                    }
                    break;
                case '+':
                case '-':
                case '*':
                case '/':
                    handleOperation(value);
                    break;
                case '%':
                    if (current) {
                        current = calculatePercentage(current).toString();
                        updateDisplay(current);
                    }
                    break;
                case '1/x':
                    if (current) {
                        current = (1 / parseFloat(current)).toString();
                        updateDisplay(current);
                    }
                    break;
                case 'x²':
                    if (current) {
                        current = (Math.pow(parseFloat(current), 2)).toString();
                        updateDisplay(current);
                    }
                    break;
                case '²√x':
                    if (current) {
                        current = (Math.sqrt(parseFloat(current))).toString();
                        updateDisplay(current);
                    }
                    break;
            }
        }
    });
});

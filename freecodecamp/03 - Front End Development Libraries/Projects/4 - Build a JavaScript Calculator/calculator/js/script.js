$(document).ready(function () {
    let result = $('#result');
    let currentInput = '';
    let operator = '';
    let inputHistory = '';

    $('.btn').not('#equals, #clear').on('click', function () {
        let value = $(this).text();
        currentInput += value;
        result.val(currentInput);
    });

    $('.operator').on('click', function () {
        operator = $(this).text();
        inputHistory += currentInput + ' ' + operator + ' ';
        currentInput = '';
        result.val('');
    });

    $('#equals').on('click', function () {
        inputHistory += currentInput;
        let finalResult = eval(inputHistory.replace(/x/g, '*').replace(/÷/g, '/'));
        result.val(finalResult);
        inputHistory = '';
        currentInput = finalResult.toString();
    });

    $('#clear').on('click', function () {
        result.val('');
        currentInput = '';
        inputHistory = '';
    });
});

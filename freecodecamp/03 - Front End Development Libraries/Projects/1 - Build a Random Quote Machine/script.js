$(document).ready(function() {
    function getRandomQuote() {
        return $.ajax({
            url: "https://api.quotable.io/random",
            method: "GET",
            dataType: "json"
        });
    }

    function displayQuote() {
        getRandomQuote().done(function(data) {
            $('#text').text(data.content);
            $('#author').text(`${data.author}`);
            updateTweetButton(data.content, data.author);
        }).fail(function() {
            $('#text').text("An error occurred. Please try again.");
            $('#author').text("");
        });
    }

    function updateTweetButton(quote, author) {
        const tweetUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(`"${quote}" - ${author}`)}`;
        $('#tweet-quote').attr('href', tweetUrl);
    }

    $('#new-quote').click(function() {
        displayQuote();
    });

    $(document).keypress(function(event) {
        if (event.which === 13) {
            displayQuote();
        }
    });

    displayQuote();
});

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
            $('#text').fadeOut(500, function() {
                $(this).text(data.content).fadeIn(500);
            })
            $('#author').fadeOut(500, function() {
                $(this).text(`${data.author}`).fadeIn(500);
            });

            console.log(`${data.content}`)
            updateTweetButton(data.content, data.author);
            updateTumblrButton(data.content, data.author);
        }).fail(function() {
            $('#text').fadeOut(500, function() {
                $(this).text("An error occurred. Please try again.").fadeIn(500);
            });
            $('#author').fadeOut(500, function() {
                $(this).text("").fadeIn(500);
            });
        });
    }

    function updateTweetButton(quote, author) {
        const tweetUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(`"${quote}" - ${author}`)}`;
        $('#tweet-quote').attr('href', tweetUrl);
    }

    function updateTumblrButton(quote, author) {
        const tumblrUrl = `https://www.tumblr.com/share/link?url=${encodeURIComponent(`"${quote}" - ${author}`)}`;
        $('#tumblr-quote').attr('href', tumblrUrl);
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

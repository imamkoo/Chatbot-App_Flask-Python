$(document).ready(function() {
    $('#user-input').keypress(function(event) {
        if (event.which === 13) { // Tombol Enter ditekan
            event.preventDefault();
            $('#send-button').click();
        }
    });

    $('#send-button').click(async function() {
        const userMessage = $('#user-input').val().trim();

        if (userMessage !== '') {
            appendUserMessage(userMessage);
            clearUserInput();
            scrollToBottom();

            await delay(500);
            const botMessage = await getBotResponse(userMessage);
            appendBotMessage(botMessage);
            scrollToBottom();
        }
    });

    function scrollToBottom() {
        $('#chat-container').scrollTop($('#chat-messages').height());
    }

    function clearUserInput() {
        $('#user-input').val('');
    }

    function appendUserMessage(message) {
        $('#chat-messages').append(`<div class="user-message">${message}</div>`);
    }

    function appendBotMessage(message) {
        $('#chat-messages').append(`<div class="bot-message">${message}</div>`);
    }

    function delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    function getBotResponse(userMessage) {
        return new Promise(resolve => {
            $.post('/get_response', { message: userMessage }, function(data) {
                resolve(data.message);
            });
        });
    }
});

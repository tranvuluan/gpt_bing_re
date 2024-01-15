document.addEventListener('DOMContentLoaded', () => {
    const messageInput = document.getElementById('messageInput');
    const responseDiv = document.getElementById('responseDiv');

    document.getElementById('submitButton').addEventListener('click', async () => {
        const message = messageInput.value;
        const response = await sendMessage(message);
        console.log('response: ', response.text);
        responseDiv.innerText = response.text;
    });

    async function sendMessage(message) {
        const response = await fetch('/api/call', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message }),
        }).then(rs => rs.json());

        return response;
    }
});

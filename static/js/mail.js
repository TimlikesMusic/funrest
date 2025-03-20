

document.getElementById("email-form").addEventListener("submit", function(event) {
    event.preventDefault();

    // Formulardaten sammeln
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    // Sendet die Daten an das Backend
    fetch('/send_email', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: name,
            email: email,
            message: message
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert('E-Mail wurde erfolgreich gesendet!');
        } else {
            alert('Fehler beim Senden der E-Mail!');
        }
    })
    .catch(error => {
        alert('Fehler beim Senden der Anfrage.');
    });
});
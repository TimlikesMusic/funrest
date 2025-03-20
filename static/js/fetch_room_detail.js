const pathParts = window.location.pathname.split('/');  // URL in Teile aufteilen
const roomId = pathParts[pathParts.length - 1];  // Der letzte Teil des Pfads ist die ID
console.log(roomId)

fetch(`/get_room/${roomId}`)  // Hole die Details für das Zimmer
    .then(response => response.json())
    .then(hotelroom => {
        // Elemente für die Zimmerdetails erstellen
        const roomDetailContainer = document.querySelector('.room-detail-content');

        const title = document.createElement('h1');
        title.textContent = hotelroom.roomname;  // Titel des Zimmers
        roomDetailContainer.appendChild(title);

        const category = document.createElement('p');
        category.textContent = `Kategorie: ${hotelroom.kategorie}`;
        roomDetailContainer.appendChild(category);

        const price = document.createElement('p');
        price.textContent = `Preis: ${hotelroom.preis} €`;
        roomDetailContainer.appendChild(price);

        const description = document.createElement('p');
        description.textContent = `Beschreibung: ${hotelroom.description || "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."}`;
        roomDetailContainer.appendChild(description);
    })
    .catch(error => {
        console.error('Fehler beim Laden der Zimmerdetails:', error);
        alert('Fehler beim Laden der Zimmerdetails');
    });

// script.js
fetch('/rooms-list')
    .then(response => response.json())
    .then(jsonData => {
        
        jsonData.forEach(hotelroom => {
            const container = document.createElement('div');
            container.classList.add('tile');

            const content = document.createElement('div');
            content.classList.add('tile-content')
            container.appendChild(content);
     
            const image = document.createElement('div');
            if(hotelroom.kategorie === "Standard"){
                image.classList.add('image-standard');
            }else if(hotelroom.kategorie === "Luxus"){
                image.classList.add('image-luxus');
            }else if(hotelroom.kategorie === "Premium"){
                image.classList.add('image-premium');
            }
           
            content.appendChild(image);

            const title = document.createElement('div');
            title.classList.add('title');
            title.textContent = `${hotelroom.roomname} (${hotelroom.kategorie})`;
            content.appendChild(title);

            const price = document.createElement('div');
            price.classList.add('price');
            price.textContent = `${(hotelroom.preis)} €`;
            content.appendChild(price);

            const description = document.createElement('div');
            description.classList.add('description');
            description.textContent = hotelroom.description || "No description available"; 
            content.appendChild(description);

            const buttonContainer = document.createElement('div');
            buttonContainer.classList.add('buttonContainer')
            container.appendChild(buttonContainer);

            const deleteButton = document.createElement('button');
            deleteButton.classList.add('deleteButton');
            deleteButton.textContent = "DeleteButton"; 
            buttonContainer.appendChild(deleteButton);
            deleteButton.addEventListener('click', () => deleteElement(hotelroom.roomid));

            const editButton = document.createElement('button');
            editButton.classList.add('editButton');
            editButton.textContent = "editButton"; 
            buttonContainer.appendChild(editButton);

            document.querySelector('.admin-tile-container').appendChild(container);
        });
    })
    .catch(error => console.error('Fehler beim Laden der JSON-Daten:', error));


function deleteElement(roomid){
    fetch('/remove_room', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ roomid: roomid })
    })
    .then(response => {
        if (response.ok) {
            location.reload();  // Reload the page to reflect changes
        } else {
            alert('Failed to delete room');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while deleting the room');
    });
}
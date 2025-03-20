
fetch('/rooms-list')
    .then(response => response.json())
    .then(jsonData => {
        
        jsonData.forEach(hotelroom => {
            const container = document.createElement('div');
            container.classList.add('tile');

            const content = document.createElement('div');
            content.classList.add('tile-content')
            container.appendChild(content);

            const title = document.createElement('div');
            title.classList.add('title');
            title.textContent = `${hotelroom.roomname} (${hotelroom.kategorie})`;
            content.appendChild(title);

            const price = document.createElement('div');
            price.classList.add('price');
            // price.value = (hotelroom.preis) + '€';
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
            editButton.addEventListener('click', () => editElement(hotelroom.roomid));

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

function editElement(roomid) {
    // Hole die Daten des Zimmers (kannst du auch von deinem Server abrufen)
    console.log("testetsetsetset")
    console.log(roomid)
    fetch(`/get_room/${roomid}`)
        .then(response => response.json())
        .then(hotelroom => {
            // Erstelle das Popup für die Bearbeitung
            const popup = document.createElement('div');
            popup.classList.add('popup');

            const form = document.createElement('div');
            form.classList.add('form');
            popup.appendChild(form);

            const container = document.createElement('div');
            container.classList.add('value-container');
            form.appendChild(container);

            // Title Input
            const titleInput = document.createElement('input');
            titleInput.classList.add('title');
            titleInput.required = true;
            titleInput.placeholder = 'Room Name';
            titleInput.value = hotelroom.roomname;  // Setze den aktuellen Wert des Zimmers
            container.appendChild(titleInput);

            // Price Input
            const priceInput = document.createElement('input');
            priceInput.classList.add('price');
            priceInput.type = 'number';  // Nur Zahlen zulassen
            priceInput.required = true;
            priceInput.placeholder = 'Price (€)';
            priceInput.value = hotelroom.preis;  // Setze den aktuellen Preis
            priceInput.min = 0;  // Verhindere negative Zahlen
            container.appendChild(priceInput);

            // Category Select
            const category = document.createElement('select');
            category.required = true;
            category.classList.add('category');
            container.appendChild(category);

            // Optionen für die Kategorien
            const option1 = document.createElement('option');
            option1.value = 'Luxus';
            option1.textContent = 'Luxus';
            if (hotelroom.kategorie === 'Luxus') option1.selected = true;  // Setze die aktuelle Kategorie
            category.appendChild(option1);

            const option2 = document.createElement('option');
            option2.value = 'Premium';
            option2.textContent = 'Premium';
            if (hotelroom.kategorie === 'Premium') option2.selected = true;
            category.appendChild(option2);

            const option3 = document.createElement('option');
            option3.value = 'Standard';
            option3.textContent = 'Standard';
            if (hotelroom.kategorie === 'Standard') option3.selected = true;
            category.appendChild(option3);

            // Save Button
            const saveBtn = document.createElement('button');
            saveBtn.classList.add('saveBtn');
            saveBtn.textContent = "Save";
            container.appendChild(saveBtn);
            saveBtn.addEventListener('click', () => saveEditElement(roomid, titleInput.value, priceInput.value, category.value));

            // Close Button
            const btnContainer = document.createElement('div');
            btnContainer.classList.add('btnContainer');
            form.appendChild(btnContainer);

            const closeBtn = document.createElement('button');
            closeBtn.classList.add('closeBtn');
            closeBtn.textContent = "X";
            btnContainer.appendChild(closeBtn);
            closeBtn.addEventListener('click', () => closePopup(popup));

            // Füge das Popup zum DOM hinzu
            document.querySelector('.content').appendChild(popup);
        })
        .catch(error => {
            console.error('Error loading room data:', error);
            alert('Failed to load room data for editing');
        });
}


const addBtn = document.getElementById('addBtn');
addBtn.addEventListener("click", addElement);

function addElement() {

    const popup = document.createElement('div');
    popup.classList.add('popup');
    // popup.appendChild()

        const form = document.createElement('div');
        form.classList.add('form');
        popup.appendChild(form);

            const container = document.createElement('div');
            container.classList.add('value-container');
            form.appendChild(container);

            const titleInput = document.createElement('input');
            titleInput.classList.add('title');
            titleInput.required = true;
            titleInput.placeholder = 'Room Name';
            container.appendChild(titleInput);

            const priceInput = document.createElement('input');
            priceInput.classList.add('price');
            priceInput.type = 'number';  // Nur Zahlen zulassen
            priceInput.required = true;
            priceInput.placeholder = 'Price (€)';
            priceInput.min = 0;  // Optional: Um negative Zahlen zu verhindern
            container.appendChild(priceInput);

            const category = document.createElement('select');
            category.required = true;
            category.classList.add('category');
            container.appendChild(category);

            // Füge Optionen hinzu
            const option1 = document.createElement('option');
            option1.value = 'Luxus';
            option1.textContent = 'Luxus';  // Text, der im Dropdown angezeigt wird
            category.appendChild(option1);

            const option2 = document.createElement('option');
            option2.value = 'Premium';
            option2.textContent = 'Premium';  // Text, der im Dropdown angezeigt wird
            category.appendChild(option2);

            const option3 = document.createElement('option');
            option3.value = 'Standard';
            option3.textContent = 'Standard';  // Text, der im Dropdown angezeigt wird
            category.appendChild(option3);


            const saveBtn = document.createElement('button');
            saveBtn.classList.add('saveBtn');
            saveBtn.textContent = "Save"; 
            container.appendChild(saveBtn);
            saveBtn.addEventListener('click', () => saveNewElement(titleInput.value, priceInput.value, category.value));
            
        const btnContainer = document.createElement('div');
        btnContainer.classList.add('btnContainer');
        form.appendChild(btnContainer);

            const closeBtn = document.createElement('button');
            closeBtn.classList.add('closeBtn');
            closeBtn.textContent = "X"; 
            btnContainer.appendChild(closeBtn);
            closeBtn.addEventListener('click', () => closePopup(popup));


 
    document.querySelector('.content').appendChild(popup);
}


function closePopup(popupElement){
    console.log(popupElement);
    popupElement.remove(); // Removes the popup from the DOM
}

function saveNewElement(roomname, price, category) {
    fetch('/add_room', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            roomname: roomname,
            kategorie: category,
            preis: price
        })
    })
    .then(response => {
        if (response.ok) {
            location.reload();  // Reload the page to reflect changes
        } else {
            alert('Failed to add room');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while adding the room');
    });
}

function saveEditElement(roomid, roomname, price, category) {
    fetch('/edit_room', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            roomid: roomid,
            roomname: roomname,
            kategorie: category,
            preis: price
        })
    })
    .then(response => {
        if (response.ok) {
            location.reload();  // Reload the page to reflect changes
        } else {
            alert('Failed to edit room');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while editing the room');
    });
}
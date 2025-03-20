// script.js
fetch('/rooms-list')
    .then(response => response.json())
    .then(jsonData => {
        
        jsonData.forEach(hotelroom => {
            
            const container = document.createElement('div');
            container.classList.add('tile');
            

            const link = document.createElement('a');
            link.classList.add('detail-link')
            link.href = `/room_detail/${hotelroom.roomid}`;

            container.appendChild(link);

     
            const image = document.createElement('div');
            if(hotelroom.kategorie === "Standard"){
                image.classList.add('image-standard');
            }else if(hotelroom.kategorie === "Luxus"){
                image.classList.add('image-luxus');
            }else if(hotelroom.kategorie === "Premium"){
                image.classList.add('image-premium');
            }
           
            link.appendChild(image);

            const title = document.createElement('div');
            title.classList.add('title');
            title.textContent = `${hotelroom.roomname} (${hotelroom.kategorie})`;
            container.appendChild(title);

            const price = document.createElement('div');
            price.classList.add('price');
            price.textContent = `${(hotelroom.preis)} €`;
            container.appendChild(price);

            const description = document.createElement('div');
            description.classList.add('description');
            description.textContent = hotelroom.description || "No description available"; 
            container.appendChild(description);

            document.querySelector('.tile-container').appendChild(container);
        });
    })
    .catch(error => console.error('Fehler beim Laden der JSON-Daten:', error));

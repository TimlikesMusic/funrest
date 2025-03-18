// script.js
fetch('./src/py/data.json')

    .then(response => response.json())
    .then(jsonData => {
        
        // Durchlaufe die "zimmer"-Daten
        Object.values(jsonData.zimmer).forEach(zimmer => {
            const container = document.createElement('div');
            container.classList.add('tile');


            const image = document.createElement('div');
            image.classList.add('image');
            image.textContent = '';
            container.appendChild(image);


            const title = document.createElement('div');
            title.classList.add('title');
            title.textContent = `${zimmer.category} (${zimmer.type})`;
            container.appendChild(title);


            const price = document.createElement('div');
            price.classList.add('price');
            price.textContent = `${zimmer.preis}`;
            container.appendChild(price);

            const description = document.createElement('div');
            description.classList.add('description');
            description.textContent = `${zimmer.desc}`;
            container.appendChild(description);

            document.querySelector('.tile-container').appendChild(container);
        });
    })
    .catch(error => console.error('Fehler beim Laden der JSON-Daten:', error));

// script.js
fetch('./src/py/data.json')

    .then(response => response.json())
    .then(jsonData => {
        
        // Durchlaufe die "zimmer"-Daten
        Object.values(jsonData.rating).forEach(rating => {

            if(rating.approved === 1){
                const container = document.createElement('div');
                container.classList.add('tile');
    
    
                const stars = document.createElement('div');
                stars.classList.add('stars');
                stars.textContent = `${rating.stars}`;
                container.appendChild(stars);
    
    
                const title = document.createElement('div');
                title.classList.add('title');
                title.textContent = `${rating.title}`;
                container.appendChild(title);
    
    
                const description = document.createElement('div');
                description.classList.add('description');
                description.textContent = `${rating.description}`;
                container.appendChild(description);

                document.querySelector('.tile-container').appendChild(container);
            }
           

            //const description = document.createElement('div');
            //description.classList.add('description');
            //description.textContent = `${zimmer.desc}`;
            //container.appendChild(description);

            
        });
    })
    .catch(error => console.error('Fehler beim Laden der JSON-Daten:', error));

// script.js
fetch('/bewertungen')

    .then(response => response.json())
    .then(jsonData => {
        
        // Durchlaufe die "zimmer"-Daten
        jsonData.forEach(review => {

            // if(rating.approved === 1){
                const container = document.createElement('div');
                container.classList.add('review-tile');
    
    
                // const stars = document.createElement('div');
                // stars.classList.add('stars');
                // stars.textContent = `${review.stars}`;
                // container.appendChild(stars);
    
    
                const title = document.createElement('div');
                title.classList.add('title');
                title.textContent = `${review.reviewtitle}`;
                container.appendChild(title);
    
    
                const description = document.createElement('div');
                description.classList.add('description');
                description.textContent = `${review.reviewdescription}`;
                container.appendChild(description);

                document.querySelector('.review-tile-container').appendChild(container);
            // }
           

            //const description = document.createElement('div');
            //description.classList.add('description');
            //description.textContent = `${zimmer.desc}`;
            //container.appendChild(description);

            
        });
    })
    .catch(error => console.error('Fehler beim Laden der JSON-Daten:', error));

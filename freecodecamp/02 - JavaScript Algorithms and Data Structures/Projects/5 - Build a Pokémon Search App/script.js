document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    const previousButton = document.getElementById('previous-button');
    const nextButton = document.getElementById('next-button');

    let currentPokemonId = 1;

    async function fetchPokemonData(pokemon) {
        try {
            const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${String(pokemon).toLowerCase()}`);
            if (!response.ok) {
                throw new Error('Pokémon not found');
            }
            const data = await response.json();
            updateUI(data);
            currentPokemonId = data.id;
            searchInput.value = "";
        } catch (error) {
            console.error(error);
            alert(error.message);
        }
    }

    function updateUI(data) {
        document.getElementById('pokemon-name').textContent = data.name;
        document.getElementById('pokemon-id').textContent = `#${data.id}`;
        document.getElementById('weight').textContent = `Weight: ${data.weight}`;
        document.getElementById('height').textContent = `Height: ${data.height}`;
        document.getElementById('sprite').src = data.sprites.front_default;
        
        const typesContainer = document.getElementById('types');
        typesContainer.innerHTML = '';
        data.types.forEach(typeInfo => {
            const typeSpan = document.createElement('span');
            typeSpan.textContent = typeInfo.type.name;
            typeSpan.classList.add('type', typeInfo.type.name);
            typesContainer.appendChild(typeSpan);
        });
    
        document.getElementById('hp').textContent = data.stats[0].base_stat;
        document.getElementById('attack').textContent = data.stats[1].base_stat;
        document.getElementById('defense').textContent = data.stats[2].base_stat;
        document.getElementById('special-attack').textContent = data.stats[3].base_stat;
        document.getElementById('special-defense').textContent = data.stats[4].base_stat;
        document.getElementById('speed').textContent = data.stats[5].base_stat;
    }

    searchForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const searchTerm = searchInput.value.trim();
        if (searchTerm) {
            fetchPokemonData(searchTerm);
        }
    });

    previousButton.addEventListener('click', () => {
        if (currentPokemonId > 1) {
            fetchPokemonData(currentPokemonId - 1);
        }
    });

    nextButton.addEventListener('click', () => {
        fetchPokemonData(currentPokemonId + 1);
    });

    document.addEventListener('keydown', (event) => {
        if (event.key === 'ArrowLeft' && currentPokemonId > 1) {
            fetchPokemonData(currentPokemonId - 1);
        } else if (event.key === 'ArrowRight') {
            fetchPokemonData(currentPokemonId + 1);
        }
    });
    
    // Fetch initial Pokémon data
    fetchPokemonData(currentPokemonId);
});

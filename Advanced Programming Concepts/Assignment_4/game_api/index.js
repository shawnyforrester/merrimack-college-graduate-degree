/**
 * This is the main file for the game API project.
 * It fetches the games from the API and renders them to the page using an event listener for the DOMContentLoaded event.
 * It also fetches the genres from the API and renders them to the page. (although the UI does not change you can see the genres in the console)
 * 
 */
document.addEventListener("DOMContentLoaded", () => {
  const apiKey = "ff5edaa3258443f8b83d47435f6a8f96";
  const baseUrl = "https://api.rawg.io/api";
  const gameList = document.getElementById("game-grid");

  // fetch the games from the API
  async function getAllGames() {
    try {
      const response = await fetch(`${baseUrl}/games?key=${apiKey}`, {
        method: "GET",
      });
      const data = await response.json();
      return data.results;
    } catch (error) {
      console.error(error);
    }
  }

  // render the games to the page
  async function renderGames(games) {  
    gameList.innerHTML = "";
    games.forEach((game) => {     
      const gameItem = document.createElement("div");
      gameItem.innerHTML = `
          <img src="${game.background_image}" style="width:100%; height:300px"alt="${game.name}">
          <h2 style="color: white">${game.name}</h2>          
              `;
      gameItem.classList.add("game-item");
      gameList.appendChild(gameItem);

      //    append platforms
      let platformItems = document.createElement("div");
      platformItems.classList.add("platform-items");
      const img = `<img src="./assets/discord-icon.svg" style="width:30px; height:30px" alt="Discord">`;
      platformItems.innerHTML += img;

      game.platforms.forEach((platform) => {
        if (
          platform.platform.name === "Xbox" ||
          platform.platform.name === "Xbox One"
        ) {
          const img = `<img src="./assets/Xbox.svg" style="width:30px; height:30px" alt="${platform.platform.name}">`;
          platformItems.innerHTML += img;
        }
        if (
          platform.platform.name === "PlayStation" ||
          platform.platform.name === "PlayStation 4"
        ) {
          const img = `<img src="./assets/playstation.svg" style="width:30px; height:30px" alt="${platform.platform.name}">`;
          platformItems.innerHTML += img;
        }
        if (platform.platform.name === "Android") {
          const img = `<img src="./assets/android.svg" style="width:30px; height:30px" alt="${platform.platform.name}">`;
          platformItems.innerHTML += img;
        }
        if (platform.platform.name === "PC") {
          const img = `<img src="./assets/icons8-windows-10.svg" style="width:30px; height:30px" alt="${platform.platform.name}">`;
          platformItems.innerHTML += img;
        }

        gameItem.appendChild(platformItems);
      });
    });  
  }

  //redner genres
  async function renderGenres() {
    const games = await getAllGames();
    const genres = new Set();
    games.forEach((game) => {
      game.genres.forEach((genre) => {
        genres.add(genre.name);
      });
    });
    const genreList = document.getElementById("genre-list");
    genres.forEach((genre) => {
      const genreItem = document.createElement("div");
      genreItem.classList.add("genre-item");
      genreItem.innerHTML = `${genre}`;
      genreList.appendChild(genreItem);
      genreItem.id = "genre-item";
      genreItem.addEventListener("click", async function () {
        const genreName = genreItem.textContent.trim();
        const gamesByGenre = await searchGames(genreName);  
        //reload the page with the games of the selected genre
        window.location.reload();     
        renderGames(gamesByGenre);
      
      });
    });
  }

  // search for games by genre name
  async function searchGames(genreName) {
    const baseUrl = "https://api.rawg.io/api";
    const response = await fetch(
      `${baseUrl}/games?key=${apiKey}&genre=${genreName}`
    );
    const data = await response.json();
    return data.results;
  }

  // Initially render all games
  async function initializePage() {
    const games = await getAllGames();
    renderGames(games);
    renderGenres();
  }

  initializePage();
});

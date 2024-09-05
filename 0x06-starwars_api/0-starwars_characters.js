  });
};
get(`https://swapi-api.alx-tools.com/api/films/${movieId}/`)
  .then(response => Promise.all(response.characters.map(url => get(url))))
  .then(responses => responses.map(response => response.name))
  .then(names => names.forEach(name => console.log(name)))

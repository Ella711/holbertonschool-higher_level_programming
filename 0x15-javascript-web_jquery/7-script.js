
const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.get(apiUrl, (data) => $('div#character').html(data.name));

$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (resp, status) {
    if (status === 'success') {
      const films = resp.results;
      for (const idx in films) {
        $('#list_movies').append('<li>' + films[idx].title + '</li>');
      }
    }
  });
});

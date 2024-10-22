// Заповнення випадаючих списків
var artistComponet = new MultipleSelectComponent(".artist-box");
var genreComponet = new MultipleSelectComponent(".genre-box");

// Збирання вибраних значень для відправки форми
var form = document.querySelector('form');
form.addEventListener('submit', function(event) {
    var artistIds = [];
    var genreIds = [];

    artistComponet.selectedList.querySelectorAll('div').forEach(function(option) {
        artistIds.push(option.dataset.value);
    });

    genreComponet.selectedList.querySelectorAll('div').forEach(function(option) {
        genreIds.push(option.dataset.value);
    });

    // Додавання вибраних значень до прихованих полів форми
    var artistIdsInput = document.createElement('input');
    artistIdsInput.type = 'hidden';
    artistIdsInput.name = 'artist_ids';
    artistIdsInput.value = artistIds.join(',');
    form.appendChild(artistIdsInput);

    var genreIdsInput = document.createElement('input');
    genreIdsInput.type = 'hidden';
    genreIdsInput.name = 'genre_ids';
    genreIdsInput.value = genreIds.join(',');
    form.appendChild(genreIdsInput);
});
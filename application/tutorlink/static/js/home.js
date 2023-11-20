$(document).ready(function() {
  $('.rectangle').on('click', function() {
    var subjectText = $(this).text().trim();

    // Redirect to the search page for the subject clicked
    window.location.href = '/search/' + encodeURIComponent(subjectText);
  });
});



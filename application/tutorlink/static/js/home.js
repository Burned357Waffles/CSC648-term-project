$(document).ready(function() {
  $('.subject-card').on('click', function() {
    const subjectText = $(this).text().trim();

    // Redirect to the search page for the subject clicked
    window.location.href = '/search/' + encodeURIComponent(subjectText);
  });
});



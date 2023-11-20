$(document).ready(function() {
  // Click event for rectangles within the carousel
  $('.rectangle').on('click', function() {
    // Get the text inside the clicked rectangle
    var subjectText = $(this).text().trim();

    // Redirect to a new page passing the subject text as a query parameter
    window.location.href = '/search/' + encodeURIComponent(subjectText);
    // Replace '/new-page' with the desired page URL
  });
});


